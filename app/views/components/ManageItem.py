import os, sys, logging
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.views.templates.ManageItem_ui import Ui_FormManageItem
from app.views.components.Loading import Loading
from app.views.components.EditItem import EditItem
from app.views.components.ManageActionButton import ManageActionButton
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

class ManageItem(Ui_FormManageItem, QWidget):
    def __init__(self, userData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = userData
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
        self._populateComboBoxItemTypeBrandSupplier()

    def _populateComboBoxItemTypeBrandSupplier(self):
        self.fetchThread = FetchThread('pos/fetch/itemtype-brand-supplier-salesgroup/all')
        self.fetchThread.finished.connect(self._handlePopulateComboBoxItemTypeBrandSupplierResult)
        self.fetchThread.start()
        
    def _handlePopulateComboBoxItemTypeBrandSupplierResult(self, result):
        self.comboBoxItemTypeName.clear()
        self.comboBoxBrandName.clear()
        self.comboBoxSupplierName.clear()

        print('-thissss-result:', result)

        for itemType in result['data']['itemTypes']:
            self.comboBoxItemTypeName.addItem(f"{itemType['itemTypeName']}")
        for brand in result['data']['brands']:
            self.comboBoxBrandName.addItem(f"{brand['brandName']}")
        for supplier in result['data']['suppliers']:
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
        self.currentThread = RegisterThread('pos/register/item', {
            'itemName': f"{self.lineEditItemName.text()}".upper(),
            'barcode': f"{self.lineEditBarcode.text()}",
            'expireDate': f"{self.dateEditExpireDate.text()}",
            'itemTypeName': f"{self.comboBoxItemTypeName.currentText()}".upper(),
            'brandName': f"{self.comboBoxBrandName.currentText()}".upper(),
            'supplierName': f"{self.comboBoxSupplierName.currentText()}".upper(),
            'capital': f"{self.lineEditCapital.text()}",
            'retailPrice': f"{self.lineEditRetailPrice.text()}",
            'wholesalePrice': f"{self.lineEditWholesalePrice.text()}",
            'effectiveDate': f"{self.dateEditEffectiveDate.text()}",
            'trackInventory': f"{self.checkBoxTrackInventory.isChecked()}"
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
        self.currentThread = FetchThread('pos/fetch/items/all/keyword/paginated', {
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text()}",
        })
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePopulateTableWidgetDataResult(self, result):
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(result['data']))
        
        self.totalPages = result['totalPages']
        
        for i, data in enumerate(result['data']):
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
            self.tableWidgetData.setItem(i, 1, tableItems[0])
            self.tableWidgetData.setItem(i, 2, tableItems[1])
            self.tableWidgetData.setItem(i, 3, tableItems[2])
            self.tableWidgetData.setItem(i, 4, tableItems[3])
            self.tableWidgetData.setItem(i, 5, tableItems[4])
            self.tableWidgetData.setItem(i, 6, tableItems[5])
            self.tableWidgetData.setItem(i, 7, tableItems[6])
            self.tableWidgetData.setItem(i, 8, tableItems[7])
            self.tableWidgetData.setItem(i, 9, tableItems[8])
            self.tableWidgetData.setItem(i, 10, tableItems[9])
            self.tableWidgetData.setItem(i, 11, tableItems[10])
            self.tableWidgetData.setItem(i, 12, tableItems[11])
            self.tableWidgetData.setItem(i, 13, tableItems[12])
            
            if data['promoName'] is not None:
                for j, tableitem in enumerate(tableItems):
                    tableitem.setForeground(QColor(255, 0, 0))
        
            manageActionButton.pushButtonEdit.clicked.connect(lambda _=i, data=data: self._onPushButtonEditClicked(data))
            manageActionButton.pushButtonDelete.clicked.connect(lambda _=i, data=data: self._onPushButtonDeleteClicked(data))
            
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
            self.currentThread = RemoveThread('pos/remove/item-price/id', {'id': f"{data['id']}"})
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
        
        event.accept()
        
        print('closed...')
