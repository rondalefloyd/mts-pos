import os, sys, logging, json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManageSales_ui import Ui_FormManageSales
from app.views.templates.PreOrder_ui import Ui_FormPreOrder
from app.views.components.PreOrderActionButton import PreOrderActionButton
from app.views.components.ManageActionButton import ManageActionButton
from app.views.components.Loading import Loading
from app.controllers.dedicated.fetch import FetchThread
   
class ManageSales(Ui_FormManageSales, QWidget):
    def __init__(self, userData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.userData = userData
        self.currentThread = None
        self.activeThreads = []
        
        self.orderIndex = 0
        self.orderNumber = 0
        self.orderType = "N/A"
        self.orderName = "N/A"
        self.activeOrder = []
        self.parkedOrder = []
        
        self.refresh()
        
        self.tabWidgetOrder.clear()
        self.comboBoxBarcodeFilter.setVisible(False)
        
        self.lineEditBarcode.returnPressed.connect(self._onLineEditBarcodeReturnPressed)
        self.tabWidgetOrder.tabCloseRequested.connect(self._onTabWidgetOrderTabCloseRequested)
        self.tabWidgetOrder.currentChanged.connect(self._onTabWidgetOrderCurrentChanged)
        self.pushButtonFilter.clicked.connect(self._onPushButtonFilterClicked)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)
        self.pushButtonNew.clicked.connect(self._onPushButtonNewClicked)

    def refresh(self):
        self.currentPage = 1
        self.totalPages = 1
        
        self._populateTableWidgetData()

    def _onLineEditBarcodeReturnPressed(self):
        # TODO: fix this where the filterer should base on the barcode filter and not ordertype
        if self.orderType == 'MIXED':
            self.currentThread = FetchThread('fetch_all_item_price_related_data_by_barcode_order_type', {
                'barcode': f"{self.lineEditBarcode.text()}",
                'orderType': f"{self.comboBoxBarcodeFilter.currentText().upper()}",
            })
        else:
            self.currentThread = FetchThread('fetch_all_item_price_related_data_by_barcode_order_type', {
                'barcode': f"{self.lineEditBarcode.text()}",
                'orderType': f"{self.orderType.upper()}",
            })

        self.currentThread.finished.connect(self._handleOnLineEditBarcodeReturnPressedResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handleOnLineEditBarcodeReturnPressedResult(self, result):
        for data in result['listData']:
            self._populateOrderItem(data)
        print('check this result out result:', json.dumps(result, indent=4, default=str))

    def _onTabWidgetOrderTabCloseRequested(self, index):
        self.tabWidgetOrder.removeTab(index)
        self.activeOrder.pop(index)
        print('self.activeOrder:', json.dumps(self.activeOrder, indent=4, default=str))

    def _onTabWidgetOrderCurrentChanged(self):
        self.orderIndex = self.tabWidgetOrder.currentIndex()
        self.orderType = self.activeOrder[self.orderIndex]['orderType']
        self.comboBoxBarcodeFilter.setVisible(self.orderType == 'MIXED')
        
        print('self.orderIndex:', self.orderIndex)
        print('self.orderType:', self.orderType)
        
        print('you clickin this')
        self._populateTableWidgetData()
        # TODO: finish this
        pass

    def _onPushButtonNewClicked(self):
        self.orderNumber += 1
        self.orderName = f"Order {self.orderNumber}"
        
        self.activeOrder.append({
            'orderName': f"{self.orderName}", 
            'orderType': f"{self.comboBoxOrderType.currentText()}".upper(),
            'orderItem': [], 
            'orderWidget': PreOrder(self),
        })
        
        self.orderIndex = len(self.activeOrder) - 1
        
        self.tabWidgetOrder.addTab(
            self.activeOrder[self.orderIndex]['orderWidget'], 
            self.activeOrder[self.orderIndex]['orderName'],
        )
        
        self.tabWidgetOrder.setCurrentIndex(self.orderIndex)
        
        print('self.activeOrder:', json.dumps(self.activeOrder, indent=4, default=str))
    
    def _onOrderWidgetPushButtonDiscardClicked(self):
        self._onTabWidgetOrderTabCloseRequested(self.orderIndex)
        
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
        
    def _populateTableWidgetData(self):
        self.currentThread = FetchThread('fetch_all_item_price_related_data_by_keyword_order_type_in_pagination', {
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text()}",
            'orderType': f"{self.orderType.upper()}",
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
            manageActionButton = ManageActionButton(add=True)
            tableItems = [
                QTableWidgetItem(f"{data['itemName']}"),
                QTableWidgetItem(f"{data['barcode']}"),
                QTableWidgetItem(f"{data['brandName']}"),
                QTableWidgetItem(f"{data['price']}"),
                QTableWidgetItem(f"{data['available']}"),
                QTableWidgetItem(f"{data['promoName']}"),
            ]
            
            self.tableWidgetData.setCellWidget(i, 0, manageActionButton)
            for j, tableitem in enumerate(tableItems):
                self.tableWidgetData.setItem(i, (j + 1), tableItems[j])
                
                if data['promoName'] is not None:
                    manageActionButton.pushButtonEdit.setVisible(False)
                    tableitem.setForeground(QColor(255, 0, 0))
        
            manageActionButton.pushButtonAdd.clicked.connect(lambda _=i, data=data: self._onPushButtonAddClicked(data))
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)

    def _onPushButtonAddClicked(self, data):
        self._populateOrderItem(data)

    def _populateOrderItem(self, data):
        itemId = data['itemId']
        itemName = data['itemName']
        promoName = data['promoName']
        price = data['price']
        discount = data['discount']
        available = data['available']
        stockBypass = False
        
        # TODO: add error handler when the tab is empty should not be able to add item
        orderItem: list = self.activeOrder[self.orderIndex]['orderItem']
        orderWidget: PreOrder = self.activeOrder[self.orderIndex]['orderWidget']
        isItemExist = False
        
        # TODO: make a clean method of this instead of too much nested if else
        for item in orderItem:
            if item['itemId'] == itemId:
                if item['stockBypass'] is False and available is not None:
                    if item['quantity'] >= available:
                        confirm = QMessageBox.warning(self, 'Error', "Item out of stock. Bypass stock?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                        
                        if confirm == QMessageBox.StandardButton.Yes:
                            item['stockBypass'] = True
                        if confirm == QMessageBox.StandardButton.No:
                            return
                
                item['quantity'] += 1
                item['total'] += price
                isItemExist = True
                break
        
        if not isItemExist:
            orderItem.append({
                'itemId': itemId,
                'price': price,
                'discount': discount,
                'available': available,
                'stockBypass': stockBypass,
                'quantity': 1,
                'itemName': itemName,
                'promoName': promoName,
                'total': price,
            })
        
        orderWidget.populateTableWidgetData(orderItem)
        
        print('orderItem:', json.dumps(orderItem, indent=4, default=str))

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

class PreOrder(Ui_FormPreOrder, QWidget):
    def __init__(self, manageSales):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.manageSales: ManageSales = manageSales
        
        self.tableWidgetData.clearContents()
        
        self.labelOrderType.setText(self.manageSales.comboBoxOrderType.currentText())
        
        self.labelSubtotal.setText("0.00")
        self.labelDiscount.setText("0.00")
        self.labelTax.setText("0.00")
        self.labelGrandTotal.setText("0.00")
        
        self.tableWidgetData
        self.pushButtonClear.clicked.connect(self._onPushButtonClearClicked)
        self.pushButtonDiscard.clicked.connect(self._onPushButtonDiscardClicked)
        self.pushButtonPark.clicked.connect(self._onPushButtonParkClicked)
        self.pushButtonPay.clicked.connect(self._onPushButtonPayClicked)
        
    def _onPushButtonClearClicked(self):
        confirm = QMessageBox.warning(self, 'Confirm', "Delete all items?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            orderItem = self.manageSales.activeOrder[self.manageSales.orderIndex]['orderItem']
            orderItem.clear()
            self.populateTableWidgetData(orderItem)
        
    def _onPushButtonDiscardClicked(self):
        pass
    def _onPushButtonParkClicked(self):
        pass
    def _onPushButtonPayClicked(self):
        pass
        
    def populateTableWidgetData(self, entry):
        rowCount = len(entry)
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(rowCount)
        self.pushButtonPay.setEnabled(rowCount > 0)
        
        subtotal = 0.00
        discount = 0.00
        tax = 0.00
        grandTotal = 0.00
        
        for i, data in enumerate(entry):
            preOrderActionButton = PreOrderActionButton()
            tableItems = [
                QTableWidgetItem(f"{data['quantity']}"),
                QTableWidgetItem(f"{data['itemName']}"),
                QTableWidgetItem(f"{data['total']}"),
            ]
            
            self.tableWidgetData.setCellWidget(i, 0, preOrderActionButton) 
            
            for j, tableitem in enumerate(tableItems):
                self.tableWidgetData.setItem(i, (j + 1), tableItems[j])
                
                if data['promoName'] is not None:
                    tableitem.setForeground(QColor(255, 0, 0))
                    
            # TODO: add tax and discount and implement it properly and clean
            subtotal += float(data['total'])
            grandTotal = (subtotal + tax) - discount
                    
            preOrderActionButton.pushButtonAddExact.clicked.connect(lambda _, index=i, entry=entry: self._onPushButtonAddExactClicked(index, entry))
            preOrderActionButton.pushButtonAddOne.clicked.connect(lambda _, index=i, entry=entry: self._onPushButtonAddOneClicked(index, entry))
            preOrderActionButton.pushButtonDeleteAll.clicked.connect(lambda _, index=i, entry=entry: self._onPushButtonDeleteAllClicked(index, entry))
            preOrderActionButton.pushButtonDeleteOne.clicked.connect(lambda _, index=i, entry=entry: self._onPushButtonDeleteOneClicked(index, entry))
            
        self.labelSubtotal.setText(f"{subtotal:.2f}")
        self.labelDiscount.setText(f"{discount:.2f}")
        self.labelTax.setText(f"{tax:.2f}")
        self.labelGrandTotal.setText(f"{grandTotal:.2f}")
            
        print('entry:', json.dumps(entry, indent=4, default=str))


    def _onPushButtonAddExactClicked(self, index, entry):
        orderItem = self.manageSales.activeOrder[self.manageSales.orderIndex]['orderItem']
        price = float(entry[index]['price'])
        
        item = orderItem[index]
        
        quantity, confirm = QInputDialog.getInt(self, 'Quantity', "Set quantity:", item['quantity'], 1, 9999999)
        
        if confirm is True:
            item['quantity'] = quantity
            item['total'] = price * quantity
            
            self.populateTableWidgetData(orderItem)

    def _onPushButtonAddOneClicked(self, index, entry):
        orderItem = self.manageSales.activeOrder[self.manageSales.orderIndex]['orderItem']
        available = entry[index]['available']
        price = float(entry[index]['price'])
        
        item = orderItem[index]
        item['quantity'] += 1
        item['total'] += price
        
        self.populateTableWidgetData(orderItem)

    def _onPushButtonDeleteAllClicked(self, index, entry):
        orderItem = self.manageSales.activeOrder[self.manageSales.orderIndex]['orderItem']
        confirm = QMessageBox.warning(self, 'Confirm', "Delete all quantity?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            available = entry[index]['available']
            
            orderItem.pop(index)
            self.populateTableWidgetData(orderItem)

    def _onPushButtonDeleteOneClicked(self, index, entry):
        orderItem = self.manageSales.activeOrder[self.manageSales.orderIndex]['orderItem']
        available = entry[index]['available']
        price = float(entry[index]['price'])
        
        item = orderItem[index]
        item['quantity'] -= 1
        item['total'] -= price
        
        if item['quantity'] <= 0:
            orderItem.pop(index)
        
        self.populateTableWidgetData(orderItem)
     