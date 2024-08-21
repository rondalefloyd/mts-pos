import os
import sys
import logging
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManageItemSold_ui import Ui_FormManageItemSold
from app.views.components.Loading import Loading
from app.views.components.ManageActionButton import ManageActionButton
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

class ManageItemSold(Ui_FormManageItemSold, QWidget):
    def __init__(self, userData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.userData = userData
        self.currentThread = None
        self.activeThreads = []
        
        self.refresh()
        
        self.pushButtonFilter.clicked.connect(self._onPushButtonFilterClicked)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)

    def refresh(self):
        self.currentPage = 1
        self.totalPages = 1
        
        self._populateTableWidgetDataA()

    def _onPushButtonFilterClicked(self):
        self.currentPage = 1
        self._populateTableWidgetDataA()

    def _onPushButtonPrevClicked(self):
        if self.currentPage > 1:
            self.currentPage -= 1
            self._populateTableWidgetDataA()
            
    def _onPushButtonNextClicked(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
            self._populateTableWidgetDataA()
        
    def _populateTableWidgetDataA(self):
        self.currentThread = FetchThread('fetch_all_item_sold_data_by_keyword_in_pagination', {
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text()}",
        })
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataAResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePopulateTableWidgetDataAResult(self, result):
        oneData = result['dictData']
        manyData = result['listData']
        
        self.tableWidgetDataA.clearContents()
        self.tableWidgetDataA.setRowCount(len(manyData))
        
        self.totalPages = oneData['totalPages'] if 'totalPages' in oneData else 1
        
        for i, data in enumerate(manyData):
            manageActionButton = ManageActionButton(void=True)
            tableItems = [
                QTableWidgetItem(f"{data['receiptId']}"),
                QTableWidgetItem(f"{data['itemName']}"),
                QTableWidgetItem(f"{data['quantity']}"),
                QTableWidgetItem(f"{data['total']}"),
                QTableWidgetItem(f"{data['reasonId']}"),
                QTableWidgetItem(f"{data['status']}"),
                QTableWidgetItem(f"{data['updateTs']}"),
            ]
            
            self.tableWidgetDataA.setCellWidget(i, 0, manageActionButton)
            
            for j, tableitem in enumerate(tableItems):
                self.tableWidgetDataA.setItem(i, (j + 1), tableItems[j])
        
            manageActionButton.pushButtonVoid.clicked.connect(lambda _, data=data: self._onPushButtonVoidClicked(data))
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)

    def _onPushButtonVoidClicked(self, data):
        confirm = QMessageBox.warning(self, 'Confirm', f"Void {data['itemName']} from {data['receiptId']}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            # TODO: change this from remove to update (updates status from 0 to 1)
            self.currentThread = RemoveThread('remove_stock_by_id', {'id': data['id']})
            self.currentThread.finished.connect(self._handleOnPushButtonVoidClickedResult)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)

    def _handleOnPushButtonVoidClickedResult(self, result):
        QMessageBox.information(self, 'Success', f"{result['message']}")
        self.currentPage = 1
        self._populateTableWidgetDataA()
            
            
    def _populateTableWidgetDataB(self):
        self.currentThread = FetchThread('fetch_all_receipt_data_by_keyword_in_pagination', {
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text()}",
        })
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataBResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handlePopulateTableWidgetDataBResult(self, result):
        oneData = result['dictData']
        manyData = result['listData']
        
        self.tableWidgetDataB.clearContents()
        self.tableWidgetDataB.setRowCount(len(manyData))
        
        self.totalPages = oneData['totalPages'] if 'totalPages' in oneData else 1
        
        for i, data in enumerate(manyData):
            manageActionButton = ManageActionButton(view=True)
            tableItems = [
                QTableWidgetItem(f"{data['orderName']}"),
                QTableWidgetItem(f"{data['orderTypeName']}"),
                QTableWidgetItem(f"{data['referenceId']}"),
                QTableWidgetItem(f"{data['userName']}"),
                QTableWidgetItem(f"{data['memberName']}"),
                QTableWidgetItem(f"{data['dateValue']}"),
                QTableWidgetItem(f"{data['updateTs']}"),
            ]
            
            self.tableWidgetDataB.setCellWidget(i, 0, manageActionButton)
            
            for j, tableitem in enumerate(tableItems):
                self.tableWidgetDataB.setItem(i, (j + 1), tableItems[j])
        
            manageActionButton.pushButtonView.clicked.connect(lambda _, data=data: self._onPushButtonViewClicked(data))
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)

    def _onPushButtonViewClicked(self, data):
        # TODO: add a dialog that shows the orderItem, orderSummary, orderPayment that has a feature to go to the itemsold
        pass

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
