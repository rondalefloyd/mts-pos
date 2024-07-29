import os
import sys
import logging
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QDate

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.views.templates.EditItem_ui import Ui_DialogEditItem
from app.views.components.Loading import Loading
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.edit import EditThread

class EditItem(Ui_DialogEditItem, QDialog):
    def __init__(self, userData, selectedData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = userData
        self.selectedData = selectedData
        self.currentThread = None
        self.activeThreads = []
        
        self.lineEditItemName.setText(f"{self.selectedData['itemName']}")
        self.lineEditBarcode.setText(f"{self.selectedData['barcode']}")
        self.dateEditExpireDate.setDate(QDate.fromString(f"{self.selectedData['expireDate']}", 'yyyy-MM-dd'))
        self.comboBoxItemTypeName.setCurrentText(f"{self.selectedData['itemType']}")
        self.comboBoxBrandName.setCurrentText(f"{self.selectedData['brand']}")
        self.comboBoxSupplierName.setCurrentText(f"{self.selectedData['supplier']}")
        self.comboBoxSalesGroupName.setCurrentText(f"{self.selectedData['salesGroup']}")
        self.lineEditCapital.setText(f"{self.selectedData['capital']}")
        self.lineEditPrice.setText(f"{self.selectedData['price']}")
        self.dateEditEffectiveDate.setDate(QDate.fromString(f"{self.selectedData['effectiveDate']}", 'yyyy-MM-dd'))

        self.lineEditPrice.textChanged.connect(self._computeNewPriceByDiscountRate)
        self.comboBoxPromoName.currentTextChanged.connect(self._computeNewPriceByDiscountRate)
        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonSave.clicked.connect(self._onPushButtonSaveClicked)

        self._populateComboBoxPromoName()

    # private methods
    def _computeNewPriceByDiscountRate(self):
        try:
            price = float(self.lineEditPrice.text().strip())
            discountRate = float(self.lineEditDiscountRate.text()) / 100.0  # Assuming the discount rate is given as a percentage

            discount = price * discountRate
            newPrice = price - discount

            self.lineEditDiscount.setText(f"{discount:.2f}")
            self.lineEditNewPrice.setText(f"{newPrice:.2f}")
            
        except ValueError:
            self.lineEditDiscount.setText("")
            self.lineEditNewPrice.setText("")
    
    def _populateComboBoxPromoName(self):
        self.fetchThread = FetchThread('pos/fetch/promo/all')
        self.fetchThread.finished.connect(self._handlePopulateComboBoxPromoNameResult)
        self.fetchThread.start()
        
    def _handlePopulateComboBoxPromoNameResult(self, result):
        for data in result['data']:
            self.comboBoxPromoName.addItem(f"{data['promoName']}")
            
            

    def _onPushButtonCancelClicked(self):
        self.close()
        
    def _onPushButtonSaveClicked(self):
        self.currentThread = EditThread('pos/edit/item', {
            'id': f"{self.selectedData['id']}",
            'itemName': f"{self.lineEditItemName.text()}".upper(),
            'barcode': f"{self.lineEditBarcode.text()}",
            'expireDate': f"{self.dateEditExpireDate.text()}",
            'itemTypeName': f"{self.comboBoxItemTypeName.currentText()}".upper(),
            'brandName': f"{self.comboBoxBrandName.currentText()}".upper(),
            'supplierName': f"{self.comboBoxSupplierName.currentText()}".upper(),
            'salesGroupName': f"{self.comboBoxSalesGroupName.currentText()}".upper(),
            'capital': f"{self.lineEditCapital.text()}",
            'price': f"{self.lineEditPrice.text()}",
            'effectiveDate': f"{self.dateEditEffectiveDate.text()}",
            'promoName': f"{self.comboBoxPromoName.currentText()}",
            'discountRate': f"{self.lineEditDiscountRate.text()}",
            'discount': f"{self.lineEditDiscount.text()}",
            'price': f"{self.lineEditPrice.text()}",
            'newPrice': f"{self.lineEditNewPrice.text()}",
            'startDate': f"{self.dateEditStartDate.text()}",
            'endDate': f"{self.dateEditEndDate.text()}",
        })
        self.currentThread.finished.connect(self._handleOnPushButtonSaveClickedResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonSaveClickedResult(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Success', f"{result['message']}")
        self.close()
        return
        
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
