import os, sys, logging, csv
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManageItem_ui import Ui_FormManageItem
from app.views.components.Loading import Loading
from app.views.components.LoadData import LoadData
from app.views.components.EditItem import EditItem
from app.views.components.ManageActionButton import ManageActionButton
from app.views.validator import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.load import LoadThread
from app.controllers.dedicated.remove import RemoveThread

class ManageItem(Ui_FormManageItem, QWidget):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
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
        
        self.dateEditEffectiveDate.setMinimumDate(QDate.currentDate())
        self.dateEditExpireDate.setMinimumDate(QDate.currentDate().addDays(1))
        
        self.refresh()
        
        self.pushButtonFilter.clicked.connect(self._onPushButtonFilterClicked)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)
        self.pushButtonClear.clicked.connect(self._onPushButtonClearClicked)
        self.pushButtonAdd.clicked.connect(self._onPushButtonAddClicked)
        self.pushButtonLoad.clicked.connect(self._onPushButtonLoadClicked)

    def refresh(self):
        self.currentPage = 1
        self.totalPages = 1
        
        self._populateTableWidgetData()
        self._populateComboBoxItemTypeBrandSupplier()

    def _onPushButtonLoadClicked(self):
        filePath, _ = QFileDialog.getOpenFileName(self, 'Open CSV', '', 'CSV Files (*.csv);;All Files (*)')

        if not filePath:
            return  # No file selected, exit the function

        # TODO: decide where to put load data (should be at the init or here)
        confirm = QMessageBox.warning(self, 'Confirm', "Replace current data with new data?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        isReplaceData = False
        if confirm == QMessageBox.StandardButton.Yes:
            isReplaceData = True
            
        self.loadData = LoadData(self.authData)
        self.loadData.show()
        self.loadData.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.currentThread = LoadThread('loadItem', {
            'filePath': filePath,
            'replaceData': isReplaceData
        })
        self.currentThread.running.connect(self._handleOnPushButtonLoadClickedInProgress)
        self.currentThread.finished.connect(self._handleOnPushButtonLoadClickedFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loadData.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _onPushButtonCancelClicked(self):
        # TODO: make sure the self.currentThread is the one being used here when executing LoadThread
        self.currentThread.stop()  # Signal the thread to stop
        
    def _handleOnPushButtonLoadClickedInProgress(self, result):
        self.loadData.progressBarLoad.setValue(result['currentDataCount'])
        self.loadData.progressBarLoad.setMaximum(result['totalDataCount'])
        self.loadData.labelDataRepresentation.setText(f"{result['dataRepresentation']}")
        self.loadData.labelLoadPercentage.setText(f"{result['currentDataCount']}")
        
    def _handleOnPushButtonLoadClickedFinished(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Success', f"{result['message']}")
        self._populateTableWidgetData()

    def _populateComboBoxItemTypeBrandSupplier(self):
        self.fetchThread = FetchThread('fetchAllItemRelatedData')
        self.fetchThread.finished.connect(self._handlePopulateComboBoxItemTypeBrandSupplierFinished)
        self.fetchThread.start()
        
    def _handlePopulateComboBoxItemTypeBrandSupplierFinished(self, result):
        self.comboBoxItemTypeName.clear()
        self.comboBoxBrandName.clear()
        self.comboBoxSupplierName.clear()
        
        listData = result['dictData']
        
        itemTypes = listData['itemTypes'] if 'itemTypes' in listData else []
        brands = listData['brands'] if 'brands' in listData else []
        suppliers = listData['suppliers'] if 'suppliers' in listData else []

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
        self.loading.show()
        self.currentThread = RegisterThread('registerItem', {
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
        self.currentThread.finished.connect(self._handleOnPushButtonAddClickedFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonAddClickedFinished(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Success', f"{result['message']}")
        self._populateTableWidgetData()
        return
        
    def _populateTableWidgetData(self):
        self.loading.show()
        self.currentThread = FetchThread('fetchAllItemPriceRelatedDataByKeywordInPagination', {
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
        self.editItem = EditItem(self.authData, data)
        self.editItem.exec()
        self._populateTableWidgetData()

    def _onPushButtonDeleteClicked(self, data):
        confirm = QMessageBox.warning(self, 'Confirm', f"Delete {data['itemName']}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.loading.show()
            self.currentThread = RemoveThread('removeItemPriceById', {'itemPriceId': data['itemPriceId']})
            self.currentThread.finished.connect(self._handleOnPushButtonDeleteClickedFinished)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.finished.connect(self.loading.close)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)

    def _handleOnPushButtonDeleteClickedFinished(self, result):
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
