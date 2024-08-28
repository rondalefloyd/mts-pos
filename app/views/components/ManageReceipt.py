import os
import sys
import logging
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManageReceipt_ui import Ui_FormManageReceipt
from app.views.components.Loading import Loading
from app.views.components.ManageActionButton import ManageActionButton
from app.views.components.ViewReceipt import ViewReceipt
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

class ManageReceipt(Ui_FormManageReceipt, QWidget):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.organizationData = authData['organization']
        self.currentThread = None
        self.activeThreads = []
        
        self.refresh()
        
        self.pushButtonFilter.clicked.connect(self._onPushButtonFilterClicked)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)

    def refresh(self):
        self.currentPage = 1
        self.totalPages = 1
        
        self._populateTableWidgetData()

    def _onPushButtonFilterClicked(self):
        self.currentPage = 1
        self._populateTableWidgetData()

    def _onPushButtonPrevClicked(self):
        if self.currentPage > 1:
            self.currentPage -= 1
            self._populateTableWidgetData()
            
    def _onPushButtonNextClicked(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
            self._populateTableWidgetData()
        
    def _populateTableWidgetData(self):
        self.currentThread = FetchThread('fetch_all_receipt_data_by_keyword_in_pagination', {
            'organizationName': self.organizationData['organizationName'],
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text()}",
        })
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePopulateTableWidgetDataFinished(self, result):
        dictData = result['dictData']
        listData = result['listData']
        
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(listData))
        
        self.totalPages = dictData['totalPages'] if 'totalPages' in dictData else 1
        
        for i, data in enumerate(listData):
            manageActionButton = ManageActionButton(view=True)
            tableItems = [
                QTableWidgetItem(f"{data['referenceId']}"),
                QTableWidgetItem(f"{data['orderName']}"),
                QTableWidgetItem(f"{data['orderTypeName']}"),
                QTableWidgetItem(f"{data['userName']}"),
                QTableWidgetItem(f"{data['memberName']}"),
                QTableWidgetItem(f"{data['dateValue']}"),
                QTableWidgetItem(f"{data['updateTs']}"),
            ]
            
            self.tableWidgetData.setCellWidget(i, 0, manageActionButton)
            
            for j, tableitem in enumerate(tableItems):
                self.tableWidgetData.setItem(i, (j + 1), tableItems[j])
        
            manageActionButton.pushButtonView.clicked.connect(lambda _, data=data: self._onPushButtonViewClicked(data))
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)

    def _onPushButtonViewClicked(self, data):
        viewReceipt = ViewReceipt(self.authData, data)
        viewReceipt.exec()

    def _cleanupThread(self):
        sender = self.sender()
        if sender in self.activeThreads:
            self.activeThreads.remove(sender)
        self.currentThread = None
        print('active threads:', self.activeThreads)

    def closeEvent(self, event):
        for thread in self.activeThreads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        
        self.activeThreads.clear()
        
        event.accept() # for closing the window
        
        print('closed...')
