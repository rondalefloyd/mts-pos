import os, sys, logging
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ViewReceipt_ui import Ui_DialogViewReceipt
from app.views.components.ManageActionButton import ManageActionButton
from app.views.components.VoidItemSold import VoidItemSold
from app.views.components.Loading import Loading
from app.views.validator import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.void import VoidThread

class ViewReceipt(Ui_DialogViewReceipt, QDialog):
    def __init__(self, authData, selectedData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.selectedData = selectedData
        self.currentThread = None
        self.activeThreads = []

        self._populateTableWidgetData()
        self._populateOrderSummary()

        self.pushButtonClose.clicked.connect(self._onPushButtonCloseClicked)

    def _populateOrderSummary(self):
        orderSummary = self.selectedData['orderSummary']
        orderPayment = self.selectedData['orderPayment']
        
        self.labelSubtotal.setText(f"{orderSummary['subtotal']}")
        self.labelDiscount.setText(f"{orderSummary['discount']}")
        self.labelTax.setText(f"{orderSummary['tax']}")
        self.labelGrandTotal.setText(f"{orderSummary['grandTotal']}")
        
        self.labelPaymentType.setText(f"{orderPayment['type']}")
        self.labelPayment.setText(f"{orderPayment['amount']}")

    def _onPushButtonCloseClicked(self):
        self.close()
        
    def _populateTableWidgetData(self):
        self.currentThread = FetchThread('fetch_all_item_sold_data', {'receiptId': self.selectedData['id']})
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handlePopulateTableWidgetDataFinished(self, result):
        oneData = result['dictData']
        manyData = result['listData']
        
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(manyData))
        
        self.totalPages = oneData['totalPages'] if 'totalPages' in oneData else 1
        
        for i, data in enumerate(manyData):
            manageActionButton = ManageActionButton(void=True)
            tableItems = [
                QTableWidgetItem(f"{data['itemName']}"),
                QTableWidgetItem(f"{data['quantity']}"),
                QTableWidgetItem(f"{data['total']}"),
                QTableWidgetItem(f"{data['reasonId']}"),
                QTableWidgetItem(f"{data['status']}"),
                QTableWidgetItem(f"{data['updateTs']}"),
            ]
            
            self.tableWidgetData.setCellWidget(i, 0, manageActionButton)
            
            for j, tableitem in enumerate(tableItems):
                self.tableWidgetData.setItem(i, (j + 1), tableItems[j])
        
                if data['status'] is not None:
                    manageActionButton.pushButtonVoid.setVisible(data['status'] != 1)
        
            manageActionButton.pushButtonVoid.clicked.connect(lambda _, data=data: self._onPushButtonVoidClicked(data))
        
    def _onPushButtonVoidClicked(self, data):
        self.voidItemSold = VoidItemSold(self.authData, data)
        self.voidItemSold.exec()
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
