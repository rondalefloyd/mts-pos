import os, sys, logging
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManageItem_ui import Ui_FormManageItem
from app.views.components.Loading import Loading
from app.views.components.EditItem import EditItem
from app.views.components.ManageActionButton import ManageActionButton
from app.views.validator import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

class ManageItem(Ui_FormManageItem, QWidget):
    def __init__(self, userData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.userData = userData
        self.currentThread = None
        self.activeThreads = []
        
        self.lineEditItemName.setValidator(withSpaceTextDigitFormatValidator())
        self.lineEditBarcode.setValidator(nonSpaceTextWithDigitFormatValidator())
        self.comboBoxItemTypeName.setValidator(withSpaceTextDigitFormatValidator())
        self.comboBoxBrandName.setValidator(withSpaceTextDigitFormatValidator())
        self.comboBoxSupplierName.setValidator(withSpaceTextDigitFormatValidator())
        self.lineEditCapital.setValidator(billFormatValidator())
        self.lineEditRetailPrice.setValidator(billFormatValidator())
        self.lineEditWholesalePrice.setValidator(billFormatValidator())
        
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
        self._populateComboBoxItemTypeBrandSupplier()

    def _populateComboBoxItemTypeBrandSupplier(self):
        self.fetchThread = FetchThread('fetch_all_item_related_data')
        self.fetchThread.finished.connect(self._handlePopulateComboBoxItemTypeBrandSupplierResult)
        self.fetchThread.start()
        
    def _handlePopulateComboBoxItemTypeBrandSupplierResult(self, result):
        self.comboBoxItemTypeName.clear()
        self.comboBoxBrandName.clear()
        self.comboBoxSupplierName.clear()
        
        manyData = result['dictData']
        
        itemTypes = manyData['itemTypes'] if 'itemTypes' in manyData else []
        brands = manyData['brands'] if 'brands' in manyData else []
        suppliers = manyData['suppliers'] if 'suppliers' in manyData else []

        for itemType in itemTypes:
            self.comboBoxItemTypeName.addItem(f"{itemType['itemTypeName']}")
        for brand in brands:
            self.comboBoxBrandName.addItem(f"{brand['brandName']}")
        for supplier in suppliers:
            self.comboBoxSupplierName.addItem(f"{supplier['supplierName']}")
            

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
        self.lineEditItemName.setText("")
        self.lineEditBarcode.setText("")
        self.lineEditCapital.setText("")
        self.lineEditRetailPrice.setText("")
        self.lineEditWholesalePrice.setText("")
        pass
        
    def _onPushButtonAddClicked(self):
        self.currentThread = RegisterThread('register_item', {
            'itemName': self.lineEditItemName.text().upper(),
            'barcode': self.lineEditBarcode.text(),
            'expireDate': self.dateEditExpireDate.text(),
            'itemTypeName': self.comboBoxItemTypeName.currentText().upper(),
            'brandName': self.comboBoxBrandName.currentText().upper(),
            'supplierName': self.comboBoxSupplierName.currentText().upper(),
            'capital': self.lineEditCapital.text(),
            'retailPrice': self.lineEditRetailPrice.text(),
            'wholesalePrice': self.lineEditWholesalePrice.text(),
            'effectiveDate': self.dateEditEffectiveDate.text(),
            'trackInventory': self.checkBoxTrackInventory.isChecked()
        })
        self.currentThread.finished.connect(self._handleOnPushButtonAddClickedResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonAddClickedResult(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Success', f"{result['message']}")
        self._populateTableWidgetData()
        return
        
    def _populateTableWidgetData(self):
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
            manageActionButton = ManageActionButton(edit=True, delete=True)
            tableItems = [
                QTableWidgetItem(f"{data['itemName']}"),
                QTableWidgetItem(f"{data['barcode']}"),
                QTableWidgetItem(f"{data['expireDate']}"),
                QTableWidgetItem(f"{data['itemTypeName']}"),
                QTableWidgetItem(f"{data['brandName']}"),
                QTableWidgetItem(f"{data['supplierName']}"),
                QTableWidgetItem(f"{data['salesGroupName']}"),
                QTableWidgetItem(f"{data['capital']}"),
                QTableWidgetItem(f"{data['price']}"),
                QTableWidgetItem(f"{data['discount']}"),
                QTableWidgetItem(f"{data['effectiveDate']}"),
                QTableWidgetItem(f"{data['promoName']}"),
                QTableWidgetItem(f"{data['updateTs']}"),
            ]
            
            self.tableWidgetData.setCellWidget(i, 0, manageActionButton)
            
            for j, tableitem in enumerate(tableItems):
                self.tableWidgetData.setItem(i, (j + 1), tableItems[j])
                
                if data['promoName'] is not None:
                    manageActionButton.pushButtonEdit.setVisible(False)
                    tableitem.setForeground(QColor(255, 0, 0))
        
            manageActionButton.pushButtonEdit.clicked.connect(lambda _=i, data=data: self._onPushButtonEditClicked(data))
            manageActionButton.pushButtonDelete.clicked.connect(lambda _, data=data: self._onPushButtonDeleteClicked(data))
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)

    def _onPushButtonEditClicked(self, data):
        self.editItem = EditItem(self.userData, data)
        self.editItem.exec()
        self._populateTableWidgetData()

    def _onPushButtonDeleteClicked(self, data):
        confirm = QMessageBox.warning(self, 'Confirm', f"Delete {data['itemName']}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.currentThread = RemoveThread('remove_item_price_by_id', {'itemPriceId': data['itemPriceId']})
            self.currentThread.finished.connect(self._handleOnPushButtonDeleteClickedResult)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)

    def _handleOnPushButtonDeleteClickedResult(self, result):
        QMessageBox.information(self, 'Success', f"{result['message']}")
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
