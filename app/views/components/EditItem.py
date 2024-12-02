import os, sys, logging

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.EditItem_ui import Ui_DialogEditItem
from app.views.components.Loading import Loading
from app.utils.helpers.formatter import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.edit import EditThread

class EditItem(Ui_DialogEditItem, QDialog):
    def __init__(self, authData, selectedData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.selectedData = selectedData
        self.currentThread = None
        self.activeThreads = []
        
        self.lineEditItemName.setText(f"{self.selectedData['itemName']}")
        self.lineEditBarcode.setText(f"{self.selectedData['barcode']}")
        self.dateEditExpireDate.setDate(QDate.fromString(f"{self.selectedData['expireDate']}", 'yyyy-MM-dd'))

        self._populateComboBoxItemTypeBrandSupplierSalesGroup()
        
        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonSave.clicked.connect(self._onPushButtonSaveClicked)

    def _onPushButtonCancelClicked(self):
        self.close()
        
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
        
    def _onPushButtonSaveClicked(self):
        self.loading.show()
        self.currentThread = EditThread('editItemDataById', {
            'id': self.selectedData['id'],
            'itemName': self.lineEditItemName.text().upper(),
            'barcode': self.lineEditBarcode.text(),
            'expireDate': self.dateEditExpireDate.text(),
            'itemTypeName': self.comboBoxItemTypeName.currentText().upper(),
            'brandName': self.comboBoxBrandName.currentText().upper(),
            'supplierName': self.comboBoxSupplierName.currentText().upper(),
            'salesGroupName': self.comboBoxSalesGroupName.currentText().upper(),
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
