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
        self.lineEditCapital.setText(f"{self.selectedData['capital']}")
        self.lineEditPrice.setText(f"{self.selectedData['price']}")
        self.dateEditEffectiveDate.setDate(QDate.fromString(f"{self.selectedData['effectiveDate']}", 'yyyy-MM-dd'))

        self._populateComboBoxItemTypeBrandSupplierSalesGroup()
        self._populateComboBoxPromoName()
        self._populateLineEditDiscountRate()
        
        self.lineEditPrice.textChanged.connect(self._populateLineEditDiscountRate)
        self.comboBoxPromoName.currentTextChanged.connect(self._populateLineEditDiscountRate)
        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonSave.clicked.connect(self._onPushButtonSaveClicked)


    # private methods
    def _populateComboBoxItemTypeBrandSupplierSalesGroup(self):
        self.fetchThread = FetchThread('pos/fetch/itemtype-brand-supplier-salesgroup/all')
        self.fetchThread.finished.connect(self._handlePopulateComboBoxItemTypeBrandSupplierSalesGroupResult)
        self.fetchThread.start()
        
    def _handlePopulateComboBoxItemTypeBrandSupplierSalesGroupResult(self, result):
        self.comboBoxItemTypeName.clear()
        self.comboBoxBrandName.clear()
        self.comboBoxSupplierName.clear()
        self.comboBoxSalesGroupName.clear()

        for itemType in result['data']['itemTypes']:
            self.comboBoxItemTypeName.addItem(f"{itemType['itemTypeName']}")
        for brand in result['data']['brands']:
            self.comboBoxBrandName.addItem(f"{brand['brandName']}")
        for supplier in result['data']['suppliers']:
            self.comboBoxSupplierName.addItem(f"{supplier['supplierName']}")
        for salesGroup in result['data']['salesGroups']:
            self.comboBoxSalesGroupName.addItem(f"{salesGroup['salesGroupName']}")
            
        self.comboBoxItemTypeName.setCurrentText(f"{self.selectedData['itemTypeName']}")
        self.comboBoxBrandName.setCurrentText(f"{self.selectedData['brandName']}")
        self.comboBoxSupplierName.setCurrentText(f"{self.selectedData['supplierName']}")
        self.comboBoxSalesGroupName.setCurrentText(f"{self.selectedData['salesGroupName']}")
    
    def _populateComboBoxPromoName(self):
        self.currentThread = FetchThread('pos/fetch/promo/all')
        self.currentThread.finished.connect(self._handlePopulateComboBoxPromoNameResult)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handlePopulateComboBoxPromoNameResult(self, result):
        self.comboBoxPromoName.clear()
        self.comboBoxPromoName.addItem("N/A")
        
        for data in result['data']:
            self.comboBoxPromoName.addItem(f"{data['promoName']}")
            
        if data['promoName'] is None:
            self.comboBoxPromoName.setCurrentText("N/A")
            return
        
        self.comboBoxPromoName.setCurrentText(f"{self.selectedData['promoName']}")        
    
    def _populateLineEditDiscountRate(self):
        self.dateEditEffectiveDate.setDisabled(self.comboBoxPromoName.currentText() != "N/A")
        self.dateEditStartDate.setEnabled(self.comboBoxPromoName.currentText() != "N/A")
        self.dateEditEndDate.setEnabled(self.comboBoxPromoName.currentText() != "N/A")
        
        if self.comboBoxPromoName.currentText() == "N/A":
            self.lineEditDiscountRate.setText("0.0")
            self.lineEditDiscount.setText("0.0")
            self.lineEditNewPrice.setText(f"{self.selectedData['price']}")
            return
        
        self.currentThread = FetchThread('pos/fetch/promo/promo-name', {'promoName': f"{self.comboBoxPromoName.currentText()}"})
        self.currentThread.finished.connect(self._handlePopulateLineEditDiscountRateResult)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    # TODO: fix the formula where the lineEditPrice should have the old value when editing an item with applied promo/ the new price isnt being stored properly. it has still the old price
    # TODO: instead of fixing it, just add a warning for the users when they're editing an item that has an applied promo
    def _handlePopulateLineEditDiscountRateResult(self, result):
        discountRate = result['data']['discountRate']
        self.lineEditDiscountRate.setText(f"{0.0 if discountRate is None else discountRate}")
        
        price = float(self.lineEditPrice.text())
        discountRate = float(self.lineEditDiscountRate.text()) / 100.0  # Assuming the discount rate is given as a percentage

        discount = price * discountRate
        newPrice = price - discount

        self.lineEditDiscount.setText(f"{discount:.2f}")
        self.lineEditNewPrice.setText(f"{newPrice:.2f}")
        
        originalPrice = float(self.selectedData['price']) + float(self.lineEditDiscount.text())   

    def _onPushButtonCancelClicked(self):
        self.close()
        
    def _onPushButtonSaveClicked(self):
        self.currentThread = EditThread('pos/edit/item/id', {
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
