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
from app.views.components.InOrder import InOrder
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
        
        self.orderNumber = 0
        self.activeOrder = []
        self.parkedOrder = []
        
        self.refresh()
        
        self.tabWidgetOrder.clear()
        self.comboBoxBarcodeFilter.setVisible(False)
        
        self.lineEditBarcode.returnPressed.connect(self._onLineEditBarcodeReturnPressed)
        self.pushButtonAdd.clicked.connect(self._onLineEditBarcodeReturnPressed)
        self.tabWidgetOrder.tabCloseRequested.connect(self.onTabWidgetOrderTabCloseRequested)
        self.tabWidgetOrder.currentChanged.connect(self._onTabWidgetOrderCurrentChanged)
        self.pushButtonFilter.clicked.connect(self._onPushButtonFilterClicked)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)
        self.pushButtonNew.clicked.connect(self._onPushButtonNewClicked)

    def refresh(self):
        self.currentPage = 1
        self.totalPages = 1
        
        self._populateTableWidgetData()

    def onTabWidgetOrderTabCloseRequested(self, index):
        orderItem: list = self.activeOrder[self.tabWidgetOrder.currentIndex()]['orderItem']
        
        if len(orderItem) > 0:
            confirm = QMessageBox.warning(self, 'Confirm', "Order contains item. Discard order?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
            if confirm == QMessageBox.StandardButton.Yes:
                self.tabWidgetOrder.removeTab(index)
                self.activeOrder.pop(index)
                self._populateTableWidgetData()
            else:
                return

    def _onLineEditBarcodeReturnPressed(self):
        orderType = self.activeOrder[self.tabWidgetOrder.currentIndex()]['orderType']
        
        self.currentThread = FetchThread('fetch_all_item_price_related_data_by_barcode_order_type', {
            'barcode': f"{self.lineEditBarcode.text()}",
            'orderType': f"{self.comboBoxBarcodeFilter.currentText().upper() if orderType == 'MIXED' else orderType.upper()}",
        })
        self.currentThread.finished.connect(self._handleOnLineEditBarcodeReturnPressedResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handleOnLineEditBarcodeReturnPressedResult(self, result):
        if len(result['listData']) <= 0:
            QMessageBox.information(self, 'Success', 'Item not found')
        
        for data in result['listData']:
            self._populateOrderItem(data)

    def _onTabWidgetOrderCurrentChanged(self):
        orderIndex = self.tabWidgetOrder.currentIndex()
        orderType = self.activeOrder[orderIndex]['orderType']
        
        self.comboBoxBarcodeFilter.setVisible(orderType == 'MIXED')
        self.labelOrderName.setText(f"{self.tabWidgetOrder.tabText(orderIndex)}")
        
        self._populateTableWidgetData()

    def _onPushButtonNewClicked(self):
        self.orderNumber += 1
        
        self.activeOrder.append({
            'orderName': f"Order {self.orderNumber}", 
            'orderType': f"{self.comboBoxOrderType.currentText().upper()}",
            'orderItem': [], 
            'orderWidget': PreOrder(self),
            'orderStatus': 1,
            'orderMember': {
                'memberName': None,
                'points': None,
            }
        })
        
        orderIndex = len(self.activeOrder) - 1
        
        self.tabWidgetOrder.addTab(
            self.activeOrder[orderIndex]['orderWidget'], 
            self.activeOrder[orderIndex]['orderName'],
        )
        
        self.tabWidgetOrder.setCurrentIndex(orderIndex)
        
    def _onOrderWidgetPushButtonDiscardClicked(self):
        self.onTabWidgetOrderTabCloseRequested(self.tabWidgetOrder.currentIndex())
        
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
            'orderType': f"{self.activeOrder[self.tabWidgetOrder.currentIndex()]['orderType'].upper() if len(self.activeOrder) > 0 else ''}",
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
            
        activeOrderCount = len(self.activeOrder)
        self.lineEditBarcode.setEnabled(activeOrderCount > 0)
        self.comboBoxBarcodeFilter.setEnabled(activeOrderCount > 0)
        self.pushButtonAdd.setEnabled(activeOrderCount > 0)
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)

    def _onPushButtonAddClicked(self, data):
        self._populateOrderItem(data)

    def _populateOrderItem(self, data):
        orderIndex = self.tabWidgetOrder.currentIndex()
        orderWidget: PreOrder = self.activeOrder[orderIndex]['orderWidget']
        
        if self.activeOrder[orderIndex]['orderStatus'] == 2:
            confirm = QMessageBox.warning(self, 'Confirm', 'Order is currently parked. Unpark order?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
            if confirm == QMessageBox.StandardButton.Yes:
                self.activeOrder[orderIndex]['orderStatus'] = 1
                orderWidget.pushButtonPark.setChecked(False)
                orderWidget.onPushButtonParkClicked()
            else:
                return
        
        itemId = data['itemId']
        itemName = data['itemName']
        promoName = data['promoName']
        price = data['price']
        discount = data['discount']
        available = data['available']
        stockBypass = False
        
        orderIndex = self.tabWidgetOrder.currentIndex()
        orderItem: list = self.activeOrder[orderIndex]['orderItem']
        orderWidget: PreOrder = self.activeOrder[orderIndex]['orderWidget']
        isItemExist = False
        
        for item in orderItem:
            if item['itemId'] != itemId:
                continue

            if not item['stockBypass'] and available is not None and item['quantity'] >= available:
                confirm = QMessageBox.warning(self, 'Error', "Item out of stock. Bypass stock?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if confirm == QMessageBox.StandardButton.Yes:
                    item['stockBypass'] = True
                else:
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
        
        self.comboBoxMemberName.currentTextChanged.connect(self._onComboBoxMemberNameCurrentTextChanged)
        self.pushButtonClear.clicked.connect(self._onPushButtonClearClicked)
        self.pushButtonDiscard.clicked.connect(self._onPushButtonDiscardClicked)
        self.pushButtonPark.clicked.connect(self.onPushButtonParkClicked)
        self.pushButtonPay.clicked.connect(self._onPushButtonPayClicked)
        
        self._populateComboBoxMemberName()
        
    def onPushButtonParkClicked(self):
        orderIndex = self.manageSales.tabWidgetOrder.currentIndex()
        orderStatus = 2 if self.pushButtonPark.isChecked() else 1
        self.manageSales.activeOrder[orderIndex]['orderStatus'] = orderStatus
        
        self.tableWidgetData.setEnabled(orderStatus == 1)
        self.pushButtonPark.setText('PARK' if orderStatus == 1 else 'UNPARK')
        self.pushButtonPay.setEnabled(orderStatus == 1)
        
    def populateTableWidgetData(self, entry):
        rowCount = len(entry)
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(rowCount)
        self.pushButtonClear.setEnabled(rowCount > 0)
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

    def _populateComboBoxMemberName(self):
        self.manageSales.currentThread = FetchThread('fetch_all_member_data')
        self.manageSales.currentThread.finished.connect(self._handlePopulateComboBoxMemberNameResult)
        self.manageSales.currentThread.finished.connect(self.manageSales._cleanupThread)
        self.manageSales.currentThread.start()
        self.manageSales.activeThreads.append(self.manageSales.currentThread)
        
    def _handlePopulateComboBoxMemberNameResult(self, result):
        self.comboBoxMemberName.clear()
        print('check this result:', result)
        listData = result['listData']
        
        for data in listData:
            self.comboBoxMemberName.addItem(f"{data['memberName']}")        

    def _onComboBoxMemberNameCurrentTextChanged(self):
        self.manageSales.currentThread = FetchThread('fetch_member_data_by_member_name', {'memberName': f"{self.comboBoxMemberName.currentText()}"})
        self.manageSales.currentThread.finished.connect(self._handleOnComboBoxMemberNameCurrentTextChangedResult)
        self.manageSales.currentThread.finished.connect(self.manageSales._cleanupThread)
        self.manageSales.currentThread.start()
        self.manageSales.activeThreads.append(self.manageSales.currentThread)
     
    def _handleOnComboBoxMemberNameCurrentTextChangedResult(self, result):
        # TODO: finish this function
        dictData = result['dictData']
        points = dictData['points'] if 'points' in dictData else 0
        
        self.lineEditPoints.setText(f"{points:.2f}")
     
    def _onPushButtonClearClicked(self):
        confirm = QMessageBox.warning(self, 'Confirm', "Delete all items?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            orderItem: list = self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()]['orderItem']
            orderItem.clear()
            self.populateTableWidgetData(orderItem)
        
    def _onPushButtonDiscardClicked(self):
        self.manageSales.onTabWidgetOrderTabCloseRequested(self.manageSales.tabWidgetOrder.currentIndex())

    def _onPushButtonPayClicked(self):
        # TODO: continue doing InOrder
        self.inOrder = InOrder(
            self.manageSales.userData, 
            self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()]
        )
        self.inOrder.exec()
        pass
               
    def _onPushButtonAddExactClicked(self, index, entry):
        orderItem = self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()]['orderItem']
        price = float(entry[index]['price'])
        
        item = orderItem[index]
        
        quantity, confirm = QInputDialog.getInt(self, 'Quantity', "Set quantity:", item['quantity'], 1, 9999999)
        
        if confirm is True:
            item['quantity'] = quantity
            item['total'] = price * quantity
            
            self.populateTableWidgetData(orderItem)

    def _onPushButtonAddOneClicked(self, index, entry):
        orderItem = self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()]['orderItem']
        available = entry[index]['available']
        price = float(entry[index]['price'])
        
        item = orderItem[index]
        item['quantity'] += 1
        item['total'] += price
        
        self.populateTableWidgetData(orderItem)

    def _onPushButtonDeleteAllClicked(self, index, entry):
        orderItem = self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()]['orderItem']
        confirm = QMessageBox.warning(self, 'Confirm', "Delete all quantity?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            available = entry[index]['available']
            
            orderItem.pop(index)
            self.populateTableWidgetData(orderItem)

    def _onPushButtonDeleteOneClicked(self, index, entry):
        orderItem = self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()]['orderItem']
        available = entry[index]['available']
        price = float(entry[index]['price'])
        
        item = orderItem[index]
        item['quantity'] -= 1
        item['total'] -= price
        
        if item['quantity'] <= 0:
            orderItem.pop(index)
        
        self.populateTableWidgetData(orderItem)
     