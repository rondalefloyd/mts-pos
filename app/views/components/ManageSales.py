import os, sys, logging
from PyQt5.QtWidgets import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManageSales_ui import Ui_FormManageSales
from app.views.components.ManageActionButton import ManageActionButton
from app.views.components.PreOrder import PreOrder
from app.views.components.PreOrderActionButton import PreOrderActionButton
from app.views.components.Loading import Loading
from app.controllers.dedicated.fetch import FetchThread

class ManageSales(Ui_FormManageSales, QWidget):
    def __init__(self, userData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.userData = userData
        self.currentThread = None
        self.activeThreads = []
        
        self.refresh()
        
        self.tabWidgetOrder.clear()
        
        self.pushButtonFilter.clicked.connect(self._onPushButtonFilterClicked)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)
        self.pushButtonNew.clicked.connect(self._onPushButtonNewClicked)

    def refresh(self):
        self.currentPage = 1
        self.totalPages = 1
        
        self._populateTableWidgetData()

    def _onPushButtonNewClicked(self):
        self.preOrder = PreOrder()
        self.orderNumber = f"Order " # TODO: add iterating value
        self.tabWidgetOrder.addTab(self.preOrder, self.orderNumber)
        
        self.preOrder.labelOrderType.setText(f"{self.comboBoxOrderType.currentText()}")

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
        # TODO: add fetcher for item displays
        self.currentThread = FetchThread('fetch_all_item_price_related_data_by_keyword_in_pagination', {
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text()}",
        })
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePopulateTableWidgetDataResult(self, result):
        oneData = result['dictData']
        manyData = result['listData']
        
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(manyData))
        
        self.totalPages = oneData['totalPages'] if 'totalPages' in oneData else 1
        
        for i, data in enumerate(manyData):
            manageActionButton = ManageActionButton(add=True)
            tableItems = [
                QTableWidgetItem(f"{data['salesName']}"),
                QTableWidgetItem(f"{data['discountRate']}"),
                QTableWidgetItem(f"{data['description']}"),
                QTableWidgetItem(f"{data['updateTs']}"),
            ]
            
            self.tableWidgetData.setCellWidget(i, 0, manageActionButton)
            self.tableWidgetData.setItem(i, 1, tableItems[0])
            self.tableWidgetData.setItem(i, 2, tableItems[1])
            self.tableWidgetData.setItem(i, 3, tableItems[2])
            self.tableWidgetData.setItem(i, 4, tableItems[3])
        
            # TODO: add function
            manageActionButton.pushButtonAdd.clicked.connect(lambda _=i, data=data: self._onPushButtonEditClicked(data))
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)

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
        
        event.accept()
        
        print('closed...')
