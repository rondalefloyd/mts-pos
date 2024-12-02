import os, sys, logging

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.EditProduct_ui import Ui_DialogEditProduct
from app.views.components.Loading import Loading
from app.utils.helpers.formatter import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.remove import RemoveThread
from app.controllers.dedicated.edit import EditThread

class EditProduct(Ui_DialogEditProduct, QDialog):
    def __init__(self, authData, selectedData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.selectedData = selectedData
        self.currentThread = None
        self.activeThreads = []
        
        self.dateEditEffectiveDate.setMinimumDate(QDate.currentDate())
        self.dateEditExpireDate.setMinimumDate(QDate.currentDate().addDays(1))
        self.dateEditStartDate.setMinimumDate(QDate.currentDate())
        self.dateEditEndDate.setMinimumDate(QDate.currentDate().addDays(1))

        self.checkBoxTrackInventory.setDisabled(self.selectedData['stockId'] is not None)
        self.checkBoxTrackInventory.setChecked(self.selectedData['stockId'] is not None)
        self.lineEditItemName.setText(f"{self.selectedData['itemName']}")
        self.lineEditBarcode.setText(f"{self.selectedData['barcode']}")
        self.dateEditExpireDate.setDate(QDate.fromString(f"{self.selectedData['expireDate']}", 'yyyy-MM-dd'))
        self.lineEditCost.setText(f"{self.selectedData['cost']}")
        self.lineEditPrice.setText(f"{self.selectedData['price']}")
        self.dateEditEffectiveDate.setDate(QDate.fromString(f"{self.selectedData['effectiveDate']}", 'yyyy-MM-dd'))
        self.comboBoxPromoName.setCurrentText("N/A")
        self.lineEditDiscountRate.setText("0.00")
        self.lineEditDiscount.setText("0.00")
        self.lineEditNewPrice.setText(f"{billFormat('', self.selectedData['price'])}")

        self._populateComboBoxItemTypeBrandSupplierSalesGroup()
        
        self.dateEditStartDate.dateChanged.connect(self._onDateEditEndDateDateChanged)
        self.checkBoxApplyPromo.stateChanged.connect(self._onCheckBoxApplyPromoStateChanged)
        self.lineEditPrice.textChanged.connect(self._populateLineEditDiscountRate)
        self.comboBoxPromoName.currentTextChanged.connect(self._populateLineEditDiscountRate)
        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonSave.clicked.connect(self._onPushButtonSaveClicked)


    # private methods
    def _onDateEditEndDateDateChanged(self, date):
        self.dateEditEndDate.setMinimumDate(date.addDays(1))
    
    def _handleOnCheckBoxTrackInventoryStateChangedFinished(self, result):
        QMessageBox.information(self, 'Information', f"{result['message']}")
        
    def _onCheckBoxApplyPromoStateChanged(self):
        self.dateEditEffectiveDate.setEnabled(self.checkBoxApplyPromo.isChecked() is False)
        self.comboBoxPromoName.setEnabled(self.checkBoxApplyPromo.isChecked() is True)
        self.dateEditStartDate.setEnabled(self.checkBoxApplyPromo.isChecked() is True)
        self.dateEditEndDate.setEnabled(self.checkBoxApplyPromo.isChecked() is True)

        if self.checkBoxApplyPromo.isChecked() is False:
            self.comboBoxPromoName.setCurrentText("N/A")        
            self.lineEditDiscountRate.setText("0.00")
            self.lineEditDiscount.setText("0.00")
            self.lineEditNewPrice.setText(f"{billFormat('', self.selectedData['price'])}")
            return
            
        self._populateComboBoxPromoName()
        self._populateLineEditDiscountRate()
    
    def _populateComboBoxItemTypeBrandSupplierSalesGroup(self):
        self.fetchThread = FetchThread('fetchAllItemRelatedData')
        self.fetchThread.finished.connect(self._handlePopulateComboBoxItemTypeBrandSupplierSalesGroupFinished)
        self.fetchThread.start()
        
    def _handlePopulateComboBoxItemTypeBrandSupplierSalesGroupFinished(self, result):
        self.comboBoxItemTypeName.clear()
        self.comboBoxBrandName.clear()
        self.comboBoxSupplierName.clear()
        self.comboBoxSalesGroupName.clear()

        dictData = result['dictData']

        for itemType in dictData['itemTypes']:
            self.comboBoxItemTypeName.addItem(f"{itemType['itemTypeName']}")
        for brand in dictData['brands']:
            self.comboBoxBrandName.addItem(f"{brand['brandName']}")
        for supplier in dictData['suppliers']:
            self.comboBoxSupplierName.addItem(f"{supplier['supplierName']}")
        for salesGroup in dictData['salesGroups']:
            self.comboBoxSalesGroupName.addItem(f"{salesGroup['salesGroupName']}")
            
        self.comboBoxItemTypeName.setCurrentText(f"{self.selectedData['itemTypeName']}")
        self.comboBoxBrandName.setCurrentText(f"{self.selectedData['brandName']}")
        self.comboBoxSupplierName.setCurrentText(f"{self.selectedData['supplierName']}")
        self.comboBoxSalesGroupName.setCurrentText(f"{self.selectedData['salesGroupName']}")
    
    def _populateComboBoxPromoName(self):
        self.loading.show()
        self.currentThread = FetchThread('fetchAllPromoData')
        self.currentThread.finished.connect(self._handlePopulateComboBoxPromoNameFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handlePopulateComboBoxPromoNameFinished(self, result):
        self.comboBoxPromoName.clear()
        
        listData = result['listData']
        
        self.checkBoxApplyPromo.setDisabled(len(listData) <= 0)
            
        for data in listData:
            self.comboBoxPromoName.addItem(f"{data['promoName']}")
            
    def _populateLineEditDiscountRate(self):
        self.loading.show()
        self.currentThread = FetchThread('fetchPromoDataByPromoName', {'promoName': f"{self.comboBoxPromoName.currentText()}"})
        self.currentThread.finished.connect(self._handlePopulateLineEditDiscountRateFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handlePopulateLineEditDiscountRateFinished(self, result):
        dictData = result['dictData']
        discountRate = dictData['discountRate'] if 'discountRate' in dictData else 0
        
        self.lineEditDiscountRate.setText(f"{billFormat('', 0.00 if discountRate is None else discountRate)}")
        
        price = float(self.lineEditPrice.text())
        discountRate = float(self.lineEditDiscountRate.text()) / 100.00  

        discount = price * discountRate
        newPrice = price - discount

        self.lineEditDiscount.setText(f"{billFormat('', discount)}")
        self.lineEditNewPrice.setText(f"{billFormat('', newPrice)}")
        
        if self.selectedData['promoName'] is not None:
            originalPrice = float(self.selectedData['price']) + float(self.lineEditDiscount.text())
            self.lineEditPrice.setText(f"{billFormat('', originalPrice)}")

    def _onPushButtonCancelClicked(self):
        self.close()
        
    def _onPushButtonSaveClicked(self):
        self.loading.show()
        self.currentThread = EditThread('editProductRelatedDataById', {
            'itemPriceId': self.selectedData['itemPriceId'],
            'itemId': self.selectedData['itemId'],
            'itemTypeId': self.selectedData['itemTypeId'],
            'brandId': self.selectedData['brandId'],
            'supplierId': self.selectedData['supplierId'],
            'salesGroupId': self.selectedData['salesGroupId'],
            'promoId': self.selectedData['promoId'],
            'stockId': self.selectedData['stockId'],
            
            'itemName': self.lineEditItemName.text().upper(),
            'barcode': self.lineEditBarcode.text(),
            'expireDate': self.dateEditExpireDate.text(),
            'itemTypeName': self.comboBoxItemTypeName.currentText().upper(),
            'brandName': self.comboBoxBrandName.currentText().upper(),
            'supplierName': self.comboBoxSupplierName.currentText().upper(),
            'salesGroupName': self.comboBoxSalesGroupName.currentText().upper(),
            'cost': self.lineEditCost.text(),
            'price': self.lineEditPrice.text(),
            'effectiveDate': self.dateEditEffectiveDate.text(),
            'promoName': self.comboBoxPromoName.currentText(),
            'discountRate': self.lineEditDiscountRate.text(),
            'discount': self.lineEditDiscount.text(),
            'newPrice': self.lineEditNewPrice.text(),
            'startDate': self.dateEditStartDate.text(),
            'endDate': self.dateEditEndDate.text(),
            'applyPromo': self.checkBoxApplyPromo.isChecked(),
            'trackInventory': self.checkBoxTrackInventory.isChecked(),
        })
        self.currentThread.finished.connect(self._handleOnPushButtonSaveClickedFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonSaveClickedFinished(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Information', f"{result['message']}")
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
        
        event.accept() # for closing the window
        
        print('closed...')
