import os
import sys
import logging
from PyQt5.QtWidgets import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.ManageItem_ui import Ui_FormManageItem
from app.views.components.Loading import Loading
from app.views.validator import *
from app.views.components.EditItem import EditItem
from app.views.components.ManageActionButton import ManageActionButton
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

class ManageItems(Ui_FormManageItem, QWidget):
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
        self._populateComboBoxItemTypeBrandSupplierSalesGroup()

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
        pass
        
    def _onPushButtonAddClicked(self):
        self.loading.show()
        self.currentThread = RegisterThread('registerItem', {
            'itemName': self.lineEditItemName.text().upper(),
            'barcode': self.lineEditBarcode.text(),
            'expireDate': self.dateEditExpireDate.text(),
            'itemTypeName': self.comboBoxItemTypeName.currentText().upper(),
            'brandName': self.comboBoxBrandName.currentText().upper(),
            'supplierName': self.comboBoxSupplierName.currentText().upper(),
            'salesGroupName': self.comboBoxSalesGroupName.currentText().upper(),
        })
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
        
    def _populateComboBoxItemTypeBrandSupplierSalesGroup(self):
        self.fetchThread = FetchThread('fetchAllItemRelatedData')
        self.fetchThread.finished.connect(self._handlePopulateComboBoxItemTypeBrandSupplierSalesGroupFinished)
        self.fetchThread.start()
        
    def _handlePopulateComboBoxItemTypeBrandSupplierSalesGroupFinished(self, result):
        self.comboBoxItemTypeName.clear()
        self.comboBoxBrandName.clear()
        self.comboBoxSupplierName.clear()
        self.comboBoxSalesGroupName.clear()
        
        listData = result['dictData']
        
        itemTypes = listData['itemTypes'] if 'itemTypes' in listData else []
        brands = listData['brands'] if 'brands' in listData else []
        suppliers = listData['suppliers'] if 'suppliers' in listData else []
        salesGroups = listData['salesGroups'] if 'salesGroups' in listData else []

        for itemType in itemTypes:
            self.comboBoxItemTypeName.addItem(f"{itemType['itemTypeName']}")
        for brand in brands:
            self.comboBoxBrandName.addItem(f"{brand['brandName']}")
        for supplier in suppliers:
            self.comboBoxSupplierName.addItem(f"{supplier['supplierName']}")
        for salesGroup in salesGroups:
            self.comboBoxSalesGroupName.addItem(f"{salesGroup['salesGroupName']}")
        
    def _populateTableWidgetData(self):
        self.loading.show()
        self.currentThread = FetchThread('fetchAllItemDataByKeywordInPagination', {
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
                QTableWidgetItem(f"{data['itemName']}"),
                QTableWidgetItem(f"{data['barcode']}"),
                QTableWidgetItem(f"{data['expireDate']}"),
                QTableWidgetItem(f"{data['itemTypeName']}"),
                QTableWidgetItem(f"{data['brandName']}"),
                QTableWidgetItem(f"{data['supplierName']}"),
                QTableWidgetItem(f"{data['salesGroupName']}"),
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
        self.editItem = EditItem(self.authData, data)
        self.editItem.exec()
        self._populateTableWidgetData()

    def _onPushButtonDeleteClicked(self, data):
        confirm = QMessageBox.warning(self, 'Confirm', f"Delete {data['itemName']}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.loading.show()
            self.currentThread = RemoveThread('removeItemById', {'id': data['id']})
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
