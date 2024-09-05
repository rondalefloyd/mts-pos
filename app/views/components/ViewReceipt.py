import os, sys, logging, json 
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
from app.controllers.dedicated.print import PrintThread

class ViewReceipt(Ui_DialogViewReceipt, QDialog):
    def __init__(self, authData, selectedData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.userData = authData['user']
        self.organizationData = authData['organization']
        self.selectedData = selectedData
        self.currentThread = None
        self.activeThreads = []
        
        self._populateTableWidgetData()
        self._populateReceipt()

        self.pushButtonClose.clicked.connect(self._onPushButtonCloseClicked)
        self.pushButtonPrint.clicked.connect(self._onPushButtonPrintClicked)

    def _onPushButtonPrintClicked(self):
        confirm = QMessageBox.warning(self, 'Confirm', f"Print receipt?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            billing = self.selectedData['billing']
            
            self.currentThread = PrintThread('print_receipt', {
                'organizationId': self.organizationData['id'],
                'userId': self.userData['id'],
                'order': {
                    'referenceId': self.selectedData['referenceId'],
                    'machineId': self.selectedData['machineId'],
                    'cart': self.cart,
                },
                'billing': {
                    'subtotal': billing['subtotal'],
                    'discount': billing['discount'],
                    'tax': billing['tax'],
                    'grandTotal': billing['grandTotal'],
                    'paymentType': billing['paymentType'],
                    'payment': billing['payment'],
                    'change': billing['change'],
                }
            })
            self.currentThread.running.connect(self._handleOnPushButtonPrintClickedRunning)
            self.currentThread.finished.connect(self._handleOnPushButtonPrintClickedFinished)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)
            pass

    def _handleOnPushButtonPrintClickedRunning(self, status):
        # TODO: FINISH THIS
        print(status)
        print('receipt is printing')
        
    def _handleOnPushButtonPrintClickedFinished(self, result):
        # TODO: FINISH THIS
        print(result)
        print('receipt is done printing')
        
    def _onPushButtonCloseClicked(self):
        self.close()
        
    def _populateReceipt(self):
        self.currentThread = FetchThread('fetch_receipt_data_by_receipt_id', {'receiptId': self.selectedData['id']})
        self.currentThread.finished.connect(self._handleOnPopulateReceiptResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPopulateReceiptResult(self, result):
        dictData = result['dictData']
        self.labelMemberName.setText(f"{dictData['memberName']}")
        self.labelMobileNumber.setText(f"{dictData['mobileNumber']}")
        
        billing = dictData['billing']
        self.labelSubtotal.setText(f"{billing['subtotal']}")
        self.labelDiscount.setText(f"{billing['discount']}")
        self.labelTax.setText(f"{billing['tax']}")
        self.labelGrandTotal.setText(f"{billing['grandTotal']}")
        self.labelAmount.setText(f"{billing['payment']}")
        self.labelChange.setText(f"{billing['change']}")
        
    def _populateTableWidgetData(self):
        self.currentThread = FetchThread('fetch_all_item_sold_data', {'receiptId': self.selectedData['id']})
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handlePopulateTableWidgetDataFinished(self, result):
        dictData = result['dictData']
        listData = result['listData']
        
        self.cart = listData
        
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(listData))
        
        self.totalPages = dictData['totalPages'] if 'totalPages' in dictData else 1
        
        for i, data in enumerate(listData):
            manageActionButton = ManageActionButton(void=True)
            tableItems = [
                QTableWidgetItem(f"{data['itemName']}"),
                QTableWidgetItem(f"{data['quantity']}"),
                QTableWidgetItem(f"{data['total']}"),
                QTableWidgetItem(f"{data['voidReason']}"),
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
        self._populateReceipt()
        
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
