import os
import sys
import logging
from PyQt5.QtWidgets import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.ManageBrand_ui import Ui_FormManageBrand
from app.views.components.Loading import Loading
from app.utils.helpers.formatter import *
from app.views.components.EditBrand import EditBrand
from app.views.components.ManageActionButton import ManageActionButton
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

class ManageBrands(Ui_FormManageBrand, QWidget):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.currentThread = None
        self.activeThreads = []
        
        self.refresh()
        
        self.pushButtonFilter.clicked.connect(self._onPushButtonFilterClicked)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)
        self.pushButtonClear.clicked.connect(self._onPushButtonClearClicked)
        self.pushButtonAdd.clicked.connect(self._onPushButtonAddClicked)

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
        
    def _onPushButtonClearClicked(self):
        self.lineEditBrandName.setText("")
        pass
        
    def _onPushButtonAddClicked(self):
        self.loading.show()
        self.currentThread = RegisterThread('registerBrand', {'brandName': self.lineEditBrandName.text().upper()})
        self.currentThread.finished.connect(self._handleOnPushButtonAddClickedFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonAddClickedFinished(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Information', f"{result['message']}")
        self._populateTableWidgetData()
        return
        
    def _populateTableWidgetData(self):
        self.loading.show()
        self.currentThread = FetchThread('fetchAllBrandDataByKeywordInPagination', {
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text().upper()}",
        })
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePopulateTableWidgetDataFinished(self, result):
        dictData = result['dictData']
        listData = result['listData']
        
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(listData))
        
        self.totalPages = dictData['totalPages'] if 'totalPages' in dictData else 1
        
        for i, data in enumerate(listData):
            manageActionButton = ManageActionButton(edit=True, delete=True)
            tableItems = [
                QTableWidgetItem(f"{data['brandName']}"),
                QTableWidgetItem(f"{data['updateTs']}"),
            ]
            
            self.tableWidgetData.setCellWidget(i, 0, manageActionButton)
            
            for j, tableitem in enumerate(tableItems):
                tableitem.setToolTip(tableitem.text())
                self.tableWidgetData.setItem(i, (j + 1), tableItems[j])
        
            manageActionButton.pushButtonEdit.clicked.connect(lambda _=i, data=data: self._onPushButtonEditClicked(data))
            manageActionButton.pushButtonDelete.clicked.connect(lambda _, data=data: self._onPushButtonDeleteClicked(data))
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)

    def _onPushButtonEditClicked(self, data):
        self.setGraphicsEffect(QGraphicsBlurEffect())
        self.editBrand = EditBrand(self.authData, data)
        self.editBrand.exec()
        self.setGraphicsEffect(None)
        self._populateTableWidgetData()

    def _onPushButtonDeleteClicked(self, data):
        confirm = QMessageBox.warning(self, 'Confirm', f"Delete {data['brandName']}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.loading.show()
            self.currentThread = RemoveThread('removeBrandById', {'id': data['id']})
            self.currentThread.finished.connect(self._handleOnPushButtonDeleteClickedFinished)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.finished.connect(self.loading.close)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)

    def _handleOnPushButtonDeleteClickedFinished(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
        
        QMessageBox.information(self, 'Information', f"{result['message']}")
        self.currentPage = 1
        self._populateTableWidgetData()

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
