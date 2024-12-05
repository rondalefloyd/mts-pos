import os, sys, logging, json, uuid
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.ManageSales_ui import Ui_FormManageSales
from app.views.templates.PreOrder_ui import Ui_FormPreOrder
from app.views.templates.InOrder_ui import Ui_DialogInOrder
from app.views.templates.PostOrder_ui import Ui_DialogPostOrder
from app.views.components.PreOrderActionButton import PreOrderActionButton
from app.views.components.ManageActionButton import ManageActionButton
from app.views.components.Loading import Loading
from app.utils.helpers.formatter import *
from app.views.components.LoadData import LoadData
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.purchase import PurchaseThread
from app.controllers.dedicated.print import PrintThread
   
class ManageSales(Ui_FormManageSales, QWidget):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.currentThread = None
        self.activeThreads = []
        
        self.orderNumber = 0
        self.activeOrder = []
        self.parkedOrder = []
        
        self.tabWidgetOrder.clear()
        self.comboBoxBarcodeFilter.setVisible(False)
        self.labelOrderName.setText(f"N/A")
        
        self._initializeShortcutKeys()
        self.refresh()
        
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
        
        self._populateCurrencySymbol()
        self._populateTableWidgetData()
        
        if len(self.activeOrder):
            orderIndex = self.tabWidgetOrder.currentIndex()
            orderWidget: PreOrder = self.activeOrder[orderIndex]['widget']
            orderWidget.refresh()

    def onTabWidgetOrderTabCloseRequested(self, index, confirmation=True):
        orderItem: list = self.activeOrder[self.tabWidgetOrder.currentIndex()]['cart']
        
        if len(orderItem) > 0 and confirmation is True:
            confirm = QMessageBox.warning(self, 'Confirm', "Order contains item. Discard order?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
            if confirm != QMessageBox.StandardButton.Yes:
                return
            
        self.tabWidgetOrder.removeTab(index)
        self.activeOrder.pop(index)
        
        if len(self.activeOrder) <= 0:
            self.labelOrderName.setText(f"N/A")
            
        self._populateTableWidgetData()

    def _initializeShortcutKeys(self):
        self.pushButtonNewShortcutKey = 'F4'
        
        self.pushButtonNewShortcut = QShortcut(QKeySequence(self.pushButtonNewShortcutKey), self)
        
        self.pushButtonNew.setText(f"[{self.pushButtonNewShortcutKey}] New")
        
        self.pushButtonNewShortcut.activated.connect(self._onPushButtonNewShortcutActivated)

    def _onPushButtonNewShortcutActivated(self):
        if self.pushButtonNew.isEnabled():
            self._onPushButtonNewClicked()

    def _populateCurrencySymbol(self):
        self.loading.show()
        self.currentThread = FetchThread('fetchPOSConfigDataByOrganizationId', {'organizationId': f"{self.authData['organization']['id']}"})
        self.currentThread.finished.connect(self._handlePopulateCurrencySymbolFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handlePopulateCurrencySymbolFinished(self, result):
        self.currencySymbol = result['dictData']['config']['currency_symbol']
        self.loading.close()

    def _onLineEditBarcodeReturnPressed(self):
        orderType = self.activeOrder[self.tabWidgetOrder.currentIndex()]['type']
        
        self.loading.show()
        self.currentThread = FetchThread('fetchAllItemPriceRelatedDataByBarcodeOrderType', {
            'barcode': f"{self.lineEditBarcode.text()}",
            'orderType': f"{self.comboBoxBarcodeFilter.currentText().upper() if orderType == 'MIXED' else orderType.upper()}",
        })
        self.currentThread.finished.connect(self._handleOnLineEditBarcodeReturnPressedFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handleOnLineEditBarcodeReturnPressedFinished(self, result):
        if len(result['listData']) <= 0:
            QMessageBox.information(self, 'Information', 'Item not found')
        
        for data in result['listData']:
            self._populateOrderItem(data)

    def _onTabWidgetOrderCurrentChanged(self):
        orderIndex = self.tabWidgetOrder.currentIndex()
        orderType = self.activeOrder[orderIndex]['type']
        
        self.comboBoxBarcodeFilter.setVisible(orderType == 'MIXED')
        self.labelOrderName.setText(f"{self.tabWidgetOrder.tabText(orderIndex)}")
        
        self._populateTableWidgetData()

    def _onPushButtonNewClicked(self):
        self.orderNumber += 1
        orderType = self.comboBoxOrderType.currentText().upper()
        orderTypeInitial = 'R' if orderType == 'RETAIL' else 'W' if orderType == 'WHOLESALE' else 'M'
        
        self.activeOrder.append({
            'name': f"{orderTypeInitial} - Order {self.orderNumber}", 
            'type': orderType,
            'cart': [], 
            'widget': PreOrder(self, self.authData),
            'status': 1,
            'member': None,
        })
        
        orderIndex = len(self.activeOrder) - 1
        
        self.tabWidgetOrder.addTab(
            self.activeOrder[orderIndex]['widget'], 
            self.activeOrder[orderIndex]['name'],
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
        self.loading.show()
        self.currentThread = FetchThread('fetchAllItemPriceRelatedDataByKeywordOrderTypeInPagination', {
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text().upper()}",
            'orderType': f"{self.activeOrder[self.tabWidgetOrder.currentIndex()]['type'].upper() if len(self.activeOrder) > 0 else ''}",
        })
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePopulateTableWidgetDataFinished(self, result):
        dictData = result['dictData']
        listData = result['listData']
        activeOrderCount = len(self.activeOrder)

        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(listData) if activeOrderCount > 0 else 0)
        self.lineEditBarcode.setEnabled(activeOrderCount > 0)
        self.comboBoxBarcodeFilter.setEnabled(activeOrderCount > 0)
        self.pushButtonAdd.setEnabled(activeOrderCount > 0)
        
        self.totalPages = 1
        
        if activeOrderCount > 0:
            self.totalPages = dictData['totalPages'] if 'totalPages' in dictData else 1
        
            for i, data in enumerate(listData):
                manageActionButton = ManageActionButton(add=True)
                tableItems = [
                    QTableWidgetItem(f"{data['itemName']}"),
                    QTableWidgetItem(f"{data['barcode']}"),
                    QTableWidgetItem(f"{data['brandName']}"),
                    QTableWidgetItem(f"{billFormat(self.currencySymbol, data['price'])}"),
                    QTableWidgetItem(f"{data['available']}"),
                    QTableWidgetItem(f"{data['promoName']}"),
                ]
                self.tableWidgetData.setCellWidget(i, 0, manageActionButton)
                
                for j, tableitem in enumerate(tableItems):
                    tableitem.setToolTip(tableitem.text())
                    self.tableWidgetData.setItem(i, (j + 1), tableitem)
                    
                    if data['promoName'] is not None:
                        manageActionButton.pushButtonEdit.setVisible(False)
                        tableitem.setForeground(QColor(255, 0, 0))
            
                manageActionButton.pushButtonAdd.clicked.connect(lambda _=i, data=data: self._onPushButtonAddClicked(data))
                
            self.lineEditBarcode.setFocus()
        
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)

    def _onPushButtonAddClicked(self, data):
        self._populateOrderItem(data)

    def _populateOrderItem(self, data):
        orderIndex = self.tabWidgetOrder.currentIndex()
        orderWidget: PreOrder = self.activeOrder[orderIndex]['widget']
        
        if self.activeOrder[orderIndex]['status'] == 2:
            confirm = QMessageBox.warning(self, 'Confirm', 'Order is currently parked. Unpark order?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
            if confirm == QMessageBox.StandardButton.Yes:
                self.activeOrder[orderIndex]['status'] = 1
                orderWidget.pushButtonPark.setChecked(False)
                orderWidget.onPushButtonParkClicked()
            else:
                return
        
        itemPriceId = data['itemPriceId']
        itemId = data['itemId']
        itemName = data['itemName']
        promoName = data['promoName']
        price = data['price']
        discount = data['discount'] or 0.00
        available = data['available']
        stockBypass = 0
        
        orderIndex = self.tabWidgetOrder.currentIndex()
        orderItem: list = self.activeOrder[orderIndex]['cart']
        orderWidget: PreOrder = self.activeOrder[orderIndex]['widget']
        isItemExist = False
        
        for item in orderItem:
            if item['itemPriceId'] != itemPriceId:
                continue

            if item['stockBypass'] == 0 and available is not None and item['quantity'] >= available:
                confirm = QMessageBox.warning(self, 'Error', "Item out of stock. Bypass stock?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if confirm == QMessageBox.StandardButton.Yes:
                    item['stockBypass'] = 1
                else:
                    return

            item['quantity'] += 1
            item['total'] += price
            item['discount'] += discount
            isItemExist = True
            break
        
        if not isItemExist:
            orderItem.append({
                'itemPriceId': itemPriceId,
                'itemId': itemId,
                'price': price,
                'discount': discount,
                'available': available,
                'stockBypass': stockBypass,
                'quantity': 1,
                'itemName': itemName,
                'promoName': promoName,
                'total': price,
                'customDiscount': 0,
            })
        
        orderWidget.populateTableWidgetData()
        
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

class PreOrder(Ui_FormPreOrder, QWidget):
    def __init__(self, manageSales, authData):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.manageSales: ManageSales = manageSales
        self.loading = Loading()
        
        self.currencySymbol = ''
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.currentThread = None
        self.activeThreads = []
        
        self.tableWidgetPreOrderItem.clearContents()
        self.labelOrderType.setText(self.manageSales.comboBoxOrderType.currentText())
        
        # shortcut key assignment
        self._initializeShortcutKeys()
        self.refresh()
        
        self.comboBoxMemberName.currentTextChanged.connect(self._onComboBoxMemberNameCurrentTextChanged)
        self.pushButtonClear.clicked.connect(self._onPushButtonClearClicked)
        self.pushButtonDiscard.clicked.connect(self._onPushButtonDiscardClicked)
        self.pushButtonPark.clicked.connect(self.onPushButtonParkClicked)
        self.pushButtonPay.clicked.connect(self._onPushButtonPayClicked)

    def refresh(self):
        self._populateCurrencySymbol()    
        self._populateComboBoxMemberName()
                
    def onPushButtonParkClicked(self):
        print('your clicking this now')
        orderItem = self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()]['cart']
        orderIndex = self.manageSales.tabWidgetOrder.currentIndex()
        orderStatus = 2 if self.pushButtonPark.isChecked() else 1
        
        print('look for orderStatus:', orderStatus)
        
        orderName = self.manageSales.tabWidgetOrder.tabText(orderIndex)
        orderName = orderName.replace(" (P)", "") if orderStatus == 1 else f"{orderName} (P)"
        self.manageSales.activeOrder[orderIndex]['status'] = orderStatus
        self.manageSales.tabWidgetOrder.setTabText(orderIndex, orderName)
        self.manageSales.labelOrderName.setText(orderName)
        
        self.pushButtonClear.setEnabled(orderStatus == 1)
        self.pushButtonPark.setText(f'[{self.pushButtonParkShortcutKey}] Park' if orderStatus == 1 else f'[{self.pushButtonParkShortcutKey}] Unpark')
        self.pushButtonPay.setEnabled(orderStatus == 1 and len(orderItem) > 0)
        self.comboBoxMemberName.setEnabled(orderStatus == 1)
        self.tableWidgetPreOrderItem.setEnabled(orderStatus == 1)
        self.manageSales.lineEditBarcode.setFocus()
        
    def populateTableWidgetData(self):
        orderItem = self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()]['cart']
        rowCount = len(orderItem)
        self.tableWidgetPreOrderItem.clearContents()
        self.tableWidgetPreOrderItem.setRowCount(rowCount)
        self.pushButtonClear.setEnabled(rowCount > 0)
        self.pushButtonPay.setEnabled(rowCount > 0)
        
        subtotal = 0.00
        discount = 0.00
        tax = 0.00
        grandTotal = 0.00
        
        for i, data in enumerate(orderItem):
            preOrderActionButton = PreOrderActionButton()
            tableItems = [
                QTableWidgetItem(f"{data['quantity']}"),
                QTableWidgetItem(f"{data['itemName']}"),
                QTableWidgetItem(f"{billFormat(self.currencySymbol, data['total'])}"),
            ]
            
            self.tableWidgetPreOrderItem.setCellWidget(i, 0, preOrderActionButton) 
            
            for j, tableitem in enumerate(tableItems):
                tableitem.setToolTip(tableitem.text())
                self.tableWidgetPreOrderItem.setItem(i, (j + 1), tableItems[j])
                
                if data['promoName'] is not None:
                    tableitem.setForeground(QColor(255, 0, 0))
                    
            # TODO: add tax and discount and implement it properly and clean
            subtotal += float(data['total'])
            discount += float(data['discount'])
            grandTotal = (subtotal + tax) - discount
                    
            preOrderActionButton.pushButtonAddExact.clicked.connect(lambda _, index=i, orderItem=orderItem: self._onPushButtonAddExactClicked(index, orderItem))
            preOrderActionButton.pushButtonAddOne.clicked.connect(lambda _, index=i, orderItem=orderItem: self._onPushButtonAddOneClicked(index, orderItem))
            preOrderActionButton.pushButtonDeleteAll.clicked.connect(lambda _, index=i, orderItem=orderItem: self._onPushButtonDeleteAllClicked(index, orderItem))
            preOrderActionButton.pushButtonDeleteOne.clicked.connect(lambda _, index=i, orderItem=orderItem: self._onPushButtonDeleteOneClicked(index, orderItem))
            
        self.labelSubtotal.setText(f"{billFormat(self.currencySymbol, subtotal)}")
        self.labelDiscount.setText(f"{billFormat(self.currencySymbol, discount)}")
        self.labelTax.setText(f"{billFormat(self.currencySymbol, tax)}")
        self.labelGrandtotal.setText(f"{billFormat(self.currencySymbol, grandTotal)}")
        self.pushButtonPay.setText(f"[{self.pushButtonPayShortcutKey}] Pay {billFormat(self.currencySymbol, grandTotal)}")
        self.manageSales.lineEditBarcode.setFocus()

    def _initializeShortcutKeys(self):
        self.pushButtonPayShortcutKey = 'F1'
        self.pushButtonDiscardShortcutKey = 'F2'
        self.pushButtonParkShortcutKey = 'F3'
        
        self.pushButtonPayShortcut = QShortcut(QKeySequence(self.pushButtonPayShortcutKey), self)
        self.pushButtonDiscardShortcut = QShortcut(QKeySequence(self.pushButtonDiscardShortcutKey), self)
        self.pushButtonParkShortcut = QShortcut(QKeySequence(self.pushButtonParkShortcutKey), self)
        
        self.pushButtonPay.setText(f"[{self.pushButtonPayShortcutKey}] Pay {self.currencySymbol}0.00")
        self.pushButtonDiscard.setText(f"[{self.pushButtonDiscardShortcutKey}] Discard")
        self.pushButtonPark.setText(f"[{self.pushButtonParkShortcutKey}] Park")
        
        self.pushButtonPayShortcut.activated.connect(self._onPushButtonPayShortcutActivated)
        self.pushButtonDiscardShortcut.activated.connect(self._onPushButtonDiscardShortcutActivated)
        self.pushButtonParkShortcut.activated.connect(self._onPushButtonParkShortcutActivated)

    def _onPushButtonPayShortcutActivated(self):
        if self.pushButtonPay.isEnabled():
            self._onPushButtonPayClicked()
            
    def _onPushButtonDiscardShortcutActivated(self):
        if self.pushButtonDiscard.isEnabled():
            self._onPushButtonDiscardClicked()
            
    def _onPushButtonParkShortcutActivated(self):
        self.pushButtonPark.setChecked(False if self.pushButtonPark.isChecked() else True)
        if self.pushButtonPark.isEnabled():
            self.onPushButtonParkClicked()

    def _populateCurrencySymbol(self):
        self.loading.show()
        self.currentThread = FetchThread('fetchPOSConfigDataByOrganizationId', {'organizationId': f"{self.authData['organization']['id']}"})
        self.currentThread.finished.connect(self._handlePopulateCurrencySymbolFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handlePopulateCurrencySymbolFinished(self, result):
        self.currencySymbol = result['dictData']['config']['currency_symbol']
        
        self.labelSubtotal.setText(f"{self.currencySymbol}0.00")
        self.labelDiscount.setText(f"{self.currencySymbol}0.00")
        self.labelTax.setText(f"{self.currencySymbol}0.00")
        self.labelGrandtotal.setText(f"{self.currencySymbol}0.00")
        self.pushButtonPay.setText(f"[{self.pushButtonPayShortcutKey}] Pay {self.currencySymbol}0.00")
        
        self.loading.close()

    def _populateComboBoxMemberName(self):
        self.manageSales.currentThread = FetchThread('fetchAllMemberData')
        self.manageSales.currentThread.finished.connect(self._handlePopulateComboBoxMemberNameFinished)
        self.manageSales.currentThread.finished.connect(self.manageSales._cleanupThread)
        self.manageSales.currentThread.start()
        self.manageSales.activeThreads.append(self.manageSales.currentThread)
        
    def _handlePopulateComboBoxMemberNameFinished(self, result):
        self.comboBoxMemberName.clear()
        
        listData = result['listData']
        
        for data in listData:
            self.comboBoxMemberName.addItem(f"{data['memberName']}")        

        self.comboBoxMemberName.clearEditText()

    def _onComboBoxMemberNameCurrentTextChanged(self):
        self.manageSales.currentThread = FetchThread('fetchMemberDataByMemberName', {'memberName': f"{self.comboBoxMemberName.currentText()}"})
        self.manageSales.currentThread.finished.connect(self._handleOnComboBoxMemberNameCurrentTextChangedFinished)
        self.manageSales.currentThread.finished.connect(self.manageSales._cleanupThread)
        self.manageSales.currentThread.start()
        self.manageSales.activeThreads.append(self.manageSales.currentThread)
     
    def _handleOnComboBoxMemberNameCurrentTextChangedFinished(self, result):
        orderIndex = self.manageSales.tabWidgetOrder.currentIndex()
        dictData = result['dictData']
        points = dictData['points'] if 'points' in dictData else 0
        
        self.lineEditPoints.setText(f"{billFormat('', points)}")
        
        self.manageSales.activeOrder[orderIndex]['member'] = dictData if dictData else None
        
    def _onPushButtonClearClicked(self):
        confirm = QMessageBox.warning(self, 'Confirm', "Delete all items?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()]['cart'].clear()
            self.populateTableWidgetData()
        
    def _onPushButtonDiscardClicked(self):
        self.manageSales.onTabWidgetOrderTabCloseRequested(self.manageSales.tabWidgetOrder.currentIndex())

    def _onPushButtonPayClicked(self):
        self.inOrder = InOrder(
            self.manageSales,
            self.manageSales.authData, 
            self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()],
        )
        self.inOrder.exec()
        
        self.manageSales.lineEditBarcode.setFocus()       
               
    def _onPushButtonAddExactClicked(self, index, orderItem):
        item = orderItem[index]
        price = float(item['price'])
        
        quantity, confirm = QInputDialog.getInt(self, 'Quantity', "Set quantity:", item['quantity'], 1, 9999999)
        
        if confirm is True:
            item['quantity'] = quantity
            item['total'] = price * quantity
            
            self.populateTableWidgetData()

    def _onPushButtonAddOneClicked(self, index, orderItem):
        item = orderItem[index]
        available = item['available']

        if not item['stockBypass'] and available is not None and item['quantity'] >= available:
            confirm = QMessageBox.warning(self, 'Error', "Item out of stock. Bypass stock?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                item['stockBypass'] = True
            else:
                return
        
        item['quantity'] += 1
        item['total'] += float(item['price'])
        
        self.populateTableWidgetData()

    def _onPushButtonDeleteAllClicked(self, index, orderItem):
        confirm = QMessageBox.warning(self, 'Confirm', "Delete all quantity?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            orderItem.pop(index)
            
            self.populateTableWidgetData()

    def _onPushButtonDeleteOneClicked(self, index, orderItem):
        item = orderItem[index]
        item['quantity'] -= 1
        item['total'] -= float(item['price'])
        
        if item['quantity'] <= 0:
            orderItem.pop(index)
            
        self.populateTableWidgetData()
        
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
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            event.ignore()
            return
        
        event.accept() # for pressing keys
     
class InOrder(Ui_DialogInOrder, QDialog):
    def __init__(self, manageSales, authData, selectedOrder):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.manageSales: ManageSales = manageSales
        self.loading = Loading()
        
        self.manageSales.setGraphicsEffect(QGraphicsBlurEffect())
        
        self.currencySymbol = ''
        self.windowEvent = EVENT_NO_EVENT
        self.organizationData = authData['organization']
        self.authData = authData
        self.userData = authData['user']
        self.selectedOrder = selectedOrder
        self.currentThread = None
        self.activeThreads = []

        self.subtotal = 0.00
        self.discount = 0.00
        self.tax = 0.00
        self.customDiscount = 0.00
        self.grandTotal = 0.00

        self.cashPayment = 0.00
        self.pointsPayment = 0.00
        self.comboPayment = 0.00
        
        self.lineEditCash.selectAll()
        
        self.labelSubtotal.setText(f'{self.currencySymbol}0.00')
        self.labelDiscount.setText(f'{self.currencySymbol}0.00')
        self.labelTax.setText(f'{self.currencySymbol}0.00')
        self.labelCustomDiscount.setText(f'{self.currencySymbol}0.00')
        self.labelGrandtotal.setText(f'{self.currencySymbol}0.00')
        
        self.labelCashPayment.setText(f'{self.currencySymbol}0.00')
        self.labelPointsPayment.setText(f'{self.currencySymbol}0.00')
        self.labelComboCashPayment.setText(f'{self.currencySymbol}0.00')
        self.labelComboPointsPayment.setText(f'{self.currencySymbol}0.00')
        
        self.labelCashShortageExcess.setText(f'{self.currencySymbol}0.00')
        self.labelPointsShortageExcess.setText(f'{self.currencySymbol}0.00')
        self.labelComboShortageExcess.setText(f'{self.currencySymbol}0.00')
        
        self._initializeShortcutKeys()
        self._populateCurrencySymbol()
        self._populateSelectedMemberFields()

        self.pushButtonKeyOne.clicked.connect(lambda: self._onPushButtonKeyClicked('1'))
        self.pushButtonKeyTwo.clicked.connect(lambda: self._onPushButtonKeyClicked('2'))
        self.pushButtonKeyThree.clicked.connect(lambda: self._onPushButtonKeyClicked('3'))
        self.pushButtonKeyFour.clicked.connect(lambda: self._onPushButtonKeyClicked('4'))
        self.pushButtonKeyFive.clicked.connect(lambda: self._onPushButtonKeyClicked('5'))
        self.pushButtonKeySix.clicked.connect(lambda: self._onPushButtonKeyClicked('6'))
        self.pushButtonKeySeven.clicked.connect(lambda: self._onPushButtonKeyClicked('7'))
        self.pushButtonKeyEight.clicked.connect(lambda: self._onPushButtonKeyClicked('8'))
        self.pushButtonKeyNine.clicked.connect(lambda: self._onPushButtonKeyClicked('9'))
        self.pushButtonKeyZero.clicked.connect(lambda: self._onPushButtonKeyClicked('0'))
        self.pushButtonKeyDecimal.clicked.connect(lambda: self._onPushButtonKeyClicked('.'))
        self.pushButtonKeyDelete.clicked.connect(lambda: self._onPushButtonKeyClicked('DEL'))
        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonPayCash.clicked.connect(lambda: self._processOrder('CASH'))
        self.pushButtonPayPoints.clicked.connect(lambda: self._processOrder('POINTS'))
        self.pushButtonPayCombo.clicked.connect(lambda: self._processOrder('COMBO'))

    def _initializeShortcutKeys(self):
        self.pushButtonPayCashShortcutKey = 'F1'
        self.pushButtonPayPointsShortcutKey = 'F2'
        self.pushButtonPayComboShortcutKey = 'F3'
        self.pushButtonCancelShortcutKey = 'F4'
        
        self.pushButtonPayCashShortcut = QShortcut(QKeySequence(self.pushButtonPayCashShortcutKey), self)
        self.pushButtonPayPointsShortcut = QShortcut(QKeySequence(self.pushButtonPayPointsShortcutKey), self)
        self.pushButtonPayComboShortcut = QShortcut(QKeySequence(self.pushButtonPayComboShortcutKey), self)
        self.pushButtonCancelShortcut = QShortcut(QKeySequence(self.pushButtonCancelShortcutKey), self)
        
        self.pushButtonPayCash.setText(f"[{self.pushButtonPayCashShortcutKey}] Cash")
        self.pushButtonPayPoints.setText(f"[{self.pushButtonPayPointsShortcutKey}] Points")
        self.pushButtonPayCombo.setText(f"[{self.pushButtonPayComboShortcutKey}] Combo")
        self.pushButtonCancel.setText(f"[{self.pushButtonCancelShortcutKey}] Cancel")
        
        
        self.pushButtonPayCashShortcut.activated.connect(self._onPushButtonPayCashShortcutActivated)
        self.pushButtonPayPointsShortcut.activated.connect(self._onPushButtonPayPointsShortcutActivated)
        self.pushButtonPayComboShortcut.activated.connect(self._onPushButtonPayComboShortcutActivated)
        self.pushButtonCancelShortcut.activated.connect(self._onPushButtonCancelShortcutActivated)

    def _onPushButtonPayCashShortcutActivated(self):
        if self.pushButtonPayCash.isEnabled():
            self._processOrder('CASH')
            
    def _onPushButtonPayPointsShortcutActivated(self):
        if self.pushButtonPayPoints.isEnabled():
            self._processOrder('POINTS')
            
    def _onPushButtonPayComboShortcutActivated(self):
        if self.pushButtonPayCombo.isEnabled():
            self._processOrder('COMBO')
            
    def _onPushButtonCancelShortcutActivated(self):
        if self.pushButtonCancel.isEnabled():
            self._onPushButtonCancelClicked()

    def _populateCurrencySymbol(self):
        self.loading.show()
        self.currentThread = FetchThread('fetchPOSConfigDataByOrganizationId', {'organizationId': f"{self.authData['organization']['id']}"})
        self.currentThread.finished.connect(self._handlePopulateCurrencySymbolFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handlePopulateCurrencySymbolFinished(self, result):
        self.currencySymbol = result['dictData']['config']['currency_symbol']
        
        self._populateTableWidgetData()
        self._populatePaymentEligibilityFields()
        
        self.lineEditCash.selectAll()

        self.lineEditCash.textChanged.connect(self._populatePaymentEligibilityFields)
        
        self.loading.close()

    def _processOrder(self, paymentType):
        subtotal = float(self.labelSubtotal.text().replace(self.currencySymbol, ''))
        discount = float(self.labelDiscount.text().replace(self.currencySymbol, ''))
        tax = float(self.labelTax.text().replace(self.currencySymbol, ''))
        grandtotal = float(self.labelGrandtotal.text().replace(self.currencySymbol, ''))

        cashPayment = 0.0
        pointsPayment = 0.0
        payment = 0.00
        change = 0.00
        
        if paymentType == 'CASH':
            cashPayment = self.cashPayment
            payment = self.cashPayment
            change = float(self.labelCashShortageExcess.text().replace(self.currencySymbol, ''))
            confirm = QMessageBox.warning(self, 'Confirm', f"Cash amount tendered is <b>{payment}</b>. Proceed?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if paymentType == 'POINTS':
            pointsPayment = self.pointsPayment
            payment = self.pointsPayment
            change = float(self.labelPointsShortageExcess.text().replace(self.currencySymbol, ''))
            confirm = QMessageBox.warning(self, 'Confirm', f"Points amount tendered is <b>{grandtotal}</b>. Proceed?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if paymentType == 'COMBO':
            cashPayment = self.cashPayment
            pointsPayment = float(self.labelGrandtotal.text().replace(self.currencySymbol, '')) - self.cashPayment
            payment = self.comboPayment
            change = float(self.labelComboShortageExcess.text().replace(self.currencySymbol, ''))
            confirm = QMessageBox.warning(self, 'Confirm', f"Combo amount tendered is <b>{billFormat(self.currencySymbol, cashPayment)} (cash) + {billFormat(self.currencySymbol, pointsPayment)} (points)</b>. Proceed?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
        
        if confirm == QMessageBox.StandardButton.Yes:
            orderMember = self.selectedOrder['member']
            
            self.loading.show()
            self.entry = {
                'organizationId': self.organizationData['id'],
                'userId': self.userData['id'],
                'memberId': orderMember['id'] if orderMember else None,
                'order': {
                    'referenceId': f"{orderMember['memberName'] if orderMember is not None else 'GUEST'}{self.selectedOrder['type']}{self.organizationData['id']}{self.userData['id']}{datetime.now().strftime('%m%d%Y%H%M')}",
                    'machineId': f"{uuid.uuid1()}",
                    'name': self.selectedOrder['name'],
                    'type': self.selectedOrder['type'],
                    'cart': self.selectedOrder['cart'],
                    'status': self.selectedOrder['status'],
                    'widget': self.selectedOrder['widget'],
                },
                'billing': {
                    'subtotal': subtotal,
                    'discount': discount,
                    'tax': tax,
                    'grandtotal': grandtotal,
                    'paymentType': paymentType,
                    'cashPaid': cashPayment,
                    'pointsPaid': pointsPayment,
                    'payment': payment,
                    'change': change,
                }
            }
            self.currentThread = PurchaseThread('purchaseItem', self.entry)
            self.currentThread.finished.connect(self._handleOnPushButtonPayCashPointsComboClickedFinished)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.finished.connect(self.loading.close)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)
            
    
    def _handleOnPushButtonPayCashPointsComboClickedFinished(self, result):
        self.close()
        self.postOrder = PostOrder(self.manageSales, self.authData, result['dictData'])
        self.postOrder.show()
        self.loading = Loading()
        self.loading.labelMessage.setText(f"Printing receipt...")
        self.loading.show()
        self.currentThread = PrintThread('printReceipt', self.entry)
        self.currentThread.finished.connect(self._handlePrintReceiptFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePrintReceiptFinished(self, result):
        QMessageBox.information(self, 'Information', f"{result['message']}")

    def _populateSelectedMemberFields(self):
        orderMember = self.selectedOrder['member']
        self.lineEditMemberName.setText(f"{orderMember['memberName']}" if orderMember else 'N/A')
        self.lineEditMobileNumber.setText(f"{orderMember['mobileNumber']}" if orderMember else 'N/A')
        self.lineEditPoints.setText(f"{billFormat('', orderMember['points'])}" if orderMember else 'N/A')

    def _onPushButtonKeyClicked(self, key):
        self.lineEditCash.setFocus()
        if key == 'DEL':
            self.cashPayment = self.lineEditCash.text()
            self.lineEditCash.backspace()
            return

        self.cashPayment = self.lineEditCash.text()
        self.cashPayment = self.cashPayment + key
        state, _, _ = floatFormatValidator().validate(self.cashPayment, 0)
        
        if state == 2:
            self.lineEditCash.setText(self.cashPayment)

    def _populatePaymentEligibilityFields(self):
        orderMember = self.selectedOrder['member']
        grandTotal = float(self.labelGrandtotal.text().replace(self.currencySymbol, ''))
        
        self.cashPayment = self.lineEditCash.text().replace(self.currencySymbol, '')
        self.cashPayment = float(self.cashPayment if self.cashPayment else 0.00) if self.cashPayment != '.' else 0.00
        cashShortageExcess = self.cashPayment - grandTotal
        
        self.labelCashPayment.setText(f"{billFormat(self.currencySymbol, self.cashPayment)}")
        self.labelCashShortageExcess.setText(f"{billFormat(self.currencySymbol, cashShortageExcess)}")
        
        self.pushButtonPayCash.setEnabled(self.cashPayment >= grandTotal)
        
        if orderMember:
            self.labelPoints.show()
            self.labelCombo.show()
            self.labelPointsPayment.show()
            self.labelComboCashPayment.show()
            self.labelPlusSymbol.show()
            self.labelComboPointsPayment.show()
            self.labelPointsShortageExcess.show()
            self.labelComboShortageExcess.show()
            
            self.pointsPayment = min(grandTotal, orderMember['points'])
            comboPointsPayment = min(self.pointsPayment, (grandTotal - self.cashPayment))
            self.comboPayment = self.cashPayment + comboPointsPayment
            pointsShortageExcess = self.pointsPayment - grandTotal
            comboShortageExcess = self.comboPayment - grandTotal
            
            self.labelPointsPayment.setText(f"{billFormat(self.currencySymbol, self.pointsPayment)}")
            self.labelComboCashPayment.setText(f"{billFormat(self.currencySymbol, self.cashPayment)}")
            self.labelComboPointsPayment.setText(f"{billFormat(self.currencySymbol, comboPointsPayment)}")
            self.labelPointsShortageExcess.setText(f"{billFormat(self.currencySymbol, pointsShortageExcess)}")
            self.labelComboShortageExcess.setText(f"{billFormat(self.currencySymbol, comboShortageExcess)}")
            
            self.pushButtonPayPoints.setEnabled(self.pointsPayment >= grandTotal)
            self.pushButtonPayCombo.setEnabled(self.comboPayment >= grandTotal)
            return
    
        self.labelPoints.hide()
        self.labelCombo.hide()
        self.labelPointsPayment.hide()
        self.labelComboCashPayment.hide()
        self.labelPlusSymbol.hide()
        self.labelComboPointsPayment.hide()
        self.labelPointsShortageExcess.hide()
        self.labelComboShortageExcess.hide()
        
        self.pushButtonPayPoints.setEnabled(False)
        self.pushButtonPayCombo.setEnabled(False)

    def _populateTableWidgetData(self):
        orderCart = self.selectedOrder['cart']
        rowCount = len(orderCart)
        self.tableWidgetInOrderItem.clearContents()
        self.tableWidgetInOrderItem.setRowCount(rowCount)
        
        self.subtotal = 0.00
        self.discount = 0.00
        self.tax = 0.00
        self.customDiscount = 0.00
        self.grandTotal = 0.00
        
        for i, data in enumerate(orderCart):
            manageActionButton = ManageActionButton(discount=True)
            tableItems = [
                QTableWidgetItem(f"{data['quantity']}"),
                QTableWidgetItem(f"{data['itemName']}"),
                QTableWidgetItem(f"{billFormat(self.currencySymbol, data['total'])}"),
                QTableWidgetItem(f"{billFormat(self.currencySymbol, data['customDiscount'])}"),
            ]
            
            self.tableWidgetInOrderItem.setCellWidget(i, 0, manageActionButton) 
            
            for j, tableitem in enumerate(tableItems):
                tableitem.setToolTip(tableitem.text())
                self.tableWidgetInOrderItem.setItem(i, (j + 1), tableItems[j])
                
                if data['promoName'] is not None:
                    tableitem.setForeground(QColor(255, 0, 0))
                    
            # TODO: add tax and discount and implement it properly and clean
            self.subtotal += float(data['total'])
            self.discount += float(data['discount'])
            self.customDiscount = float(data['customDiscount'])
            self.grandTotal = ((self.subtotal + self.tax) - self.discount) - self.customDiscount
            
            manageActionButton.pushButtonDiscount.clicked.connect(lambda _, index=i, data=data: self._onPushButtonDiscountClicked(index, data))
            
        self.labelSubtotal.setText(f"{billFormat(self.currencySymbol, self.subtotal)}")
        self.labelDiscount.setText(f"{billFormat(self.currencySymbol, self.discount)}")
        self.labelTax.setText(f"{billFormat(self.currencySymbol, self.tax)}")
        self.labelCustomDiscount.setText(f"{billFormat(self.currencySymbol, self.customDiscount)}")
        self.labelGrandtotal.setText(f"{billFormat(self.currencySymbol, self.grandTotal)}")
        self.lineEditCash.setText(f"{self.grandTotal}")
        self.lineEditCash.setFocus()

    def _onPushButtonDiscountClicked(self, index, data):
        customDiscount, confirm = QInputDialog.getDouble(self, 'Quantity', "Set custom discount:", 1, 1, 9999999, 2)
        
        if confirm is True:
            self.selectedOrder['cart'][index]['customDiscount'] = customDiscount
            
            self._populateTableWidgetData()
        self.lineEditCash.setFocus()
        
    def _onPushButtonCancelClicked(self):
        self.manageSales.setGraphicsEffect(None)
        self.close()

    def _cleanupThread(self):
        sender = self.sender()
        if sender in self.activeThreads:
            self.activeThreads.remove(sender)
        self.currentThread = None
        print('active threads:', self.activeThreads)

    def closeEvent(self, event):
        for data in self.selectedOrder['cart']:
            data['customDiscount'] = 0.00
        
        for thread in self.activeThreads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        
        self.activeThreads.clear()
        
        event.accept() # for closing the window
        
        print('closed...')
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            event.ignore()
            return
        
        event.accept() # for pressing keys

class PostOrder(Ui_DialogPostOrder, QDialog):
    def __init__(self, manageSales, authData, selectedOrder):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.manageSales: ManageSales = manageSales
        self.loading = Loading()
        
        self.manageSales.setGraphicsEffect(QGraphicsBlurEffect())
        
        self.currencySymbol = ''
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.selectedOrder = selectedOrder
        self.currentThread = None
        self.activeThreads = []

        self._initializeShortcutKeys()
        self._populateCurrencySymbol()
        
        self.pushButtonClose.clicked.connect(self._onPushButtonCloseClicked)

    def _initializeShortcutKeys(self):
        self.pushButtonCloseShortcutKey = 'F1'
        
        self.pushButtonCloseShortcut = QShortcut(QKeySequence(self.pushButtonCloseShortcutKey), self)
        
        self.pushButtonClose.setText(f"[{self.pushButtonCloseShortcutKey}] Close")
        
        self.pushButtonCloseShortcut.activated.connect(self._onPushButtonCloseShortcutActivated)

    def _onPushButtonCloseShortcutActivated(self):
        if self.pushButtonClose.isEnabled():
            self._onPushButtonCloseClicked()

    def _populateCurrencySymbol(self):
        self.loading.show()
        self.currentThread = FetchThread('fetchPOSConfigDataByOrganizationId', {'organizationId': f"{self.authData['organization']['id']}"})
        self.currentThread.finished.connect(self._handlePopulateCurrencySymbolFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handlePopulateCurrencySymbolFinished(self, result):
        self.currencySymbol = result['dictData']['config']['currency_symbol']
        
        billing = self.selectedOrder['billing']
        self.labelPayment.setText(f"{billFormat(self.currencySymbol, billing['payment'])}")
        self.labelGrandtotal.setText(f"{billFormat(self.currencySymbol, billing['grandtotal'])}")
        self.labelChange.setText(f"{billFormat(self.currencySymbol, billing['change'])}")
        
        self.loading.close()

    def _onPushButtonCloseClicked(self):
        self.manageSales.onTabWidgetOrderTabCloseRequested(
            index=self.manageSales.tabWidgetOrder.currentIndex(),
            confirmation=False,
        )
        self.manageSales.setGraphicsEffect(None)
        self.close()

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
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            event.ignore()
            return
        
        event.accept() # for pressing keys
