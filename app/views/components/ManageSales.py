import os, sys, logging, json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManageSales_ui import Ui_FormManageSales
from app.views.templates.PreOrder_ui import Ui_FormPreOrder
from app.views.templates.InOrder_ui import Ui_DialogInOrder
from app.views.templates.PostOrder_ui import Ui_DialogPostOrder
from app.views.components.PreOrderActionButton import PreOrderActionButton
from app.views.components.ManageActionButton import ManageActionButton
from app.views.components.Loading import Loading
from app.views.validator import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.purchase import PurchaseThread
   
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
        self.lineEditBarcode.setValidator(nonSpaceTextWithDigitFormatValidator())
        
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
        
        self._populateTableWidgetData()

    def onTabWidgetOrderTabCloseRequested(self, index, confirmation=True):
        orderItem: list = self.activeOrder[self.tabWidgetOrder.currentIndex()]['orderItem']
        
        if len(orderItem) > 0 and confirmation is True:
            confirm = QMessageBox.warning(self, 'Confirm', "Order contains item. Discard order?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
            if confirm != QMessageBox.StandardButton.Yes:
                return
    
        self.tabWidgetOrder.removeTab(index)
        self.activeOrder.pop(index)
        self._populateTableWidgetData()

    def _onLineEditBarcodeReturnPressed(self):
        orderType = self.activeOrder[self.tabWidgetOrder.currentIndex()]['orderType']
        
        self.currentThread = FetchThread('fetch_all_item_price_related_data_by_barcode_order_type', {
            'barcode': f"{self.lineEditBarcode.text()}",
            'orderType': f"{self.comboBoxBarcodeFilter.currentText().upper() if orderType == 'MIXED' else orderType.upper()}",
        })
        self.currentThread.finished.connect(self._handleOnLineEditBarcodeReturnPressedFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handleOnLineEditBarcodeReturnPressedFinished(self, result):
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
            'orderMember': None,
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
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePopulateTableWidgetDataFinished(self, result):
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
        
    def populateTableWidgetData(self):
        orderItem = self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()]['orderItem']
        rowCount = len(orderItem)
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(rowCount)
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
                    
            preOrderActionButton.pushButtonAddExact.clicked.connect(lambda _, index=i, orderItem=orderItem: self._onPushButtonAddExactClicked(index, orderItem))
            preOrderActionButton.pushButtonAddOne.clicked.connect(lambda _, index=i, orderItem=orderItem: self._onPushButtonAddOneClicked(index, orderItem))
            preOrderActionButton.pushButtonDeleteAll.clicked.connect(lambda _, index=i, orderItem=orderItem: self._onPushButtonDeleteAllClicked(index, orderItem))
            preOrderActionButton.pushButtonDeleteOne.clicked.connect(lambda _, index=i, orderItem=orderItem: self._onPushButtonDeleteOneClicked(index, orderItem))
            
        self.labelSubtotal.setText(f"{subtotal:.2f}")
        self.labelDiscount.setText(f"{discount:.2f}")
        self.labelTax.setText(f"{tax:.2f}")
        self.labelGrandTotal.setText(f"{grandTotal:.2f}")

    def _populateComboBoxMemberName(self):
        self.manageSales.currentThread = FetchThread('fetch_all_member_data')
        self.manageSales.currentThread.finished.connect(self._handlePopulateComboBoxMemberNameFinished)
        self.manageSales.currentThread.finished.connect(self.manageSales._cleanupThread)
        self.manageSales.currentThread.start()
        self.manageSales.activeThreads.append(self.manageSales.currentThread)
        
    def _handlePopulateComboBoxMemberNameFinished(self, result):
        self.comboBoxMemberName.clear()
        
        listData = result['listData']
        
        for data in listData:
            self.comboBoxMemberName.addItem(f"{data['memberName']}")        

    def _onComboBoxMemberNameCurrentTextChanged(self):
        self.manageSales.currentThread = FetchThread('fetch_member_data_by_member_name', {'memberName': f"{self.comboBoxMemberName.currentText()}"})
        self.manageSales.currentThread.finished.connect(self._handleOnComboBoxMemberNameCurrentTextChangedFinished)
        self.manageSales.currentThread.finished.connect(self.manageSales._cleanupThread)
        self.manageSales.currentThread.start()
        self.manageSales.activeThreads.append(self.manageSales.currentThread)
     
    def _handleOnComboBoxMemberNameCurrentTextChangedFinished(self, result):
        orderIndex = self.manageSales.tabWidgetOrder.currentIndex()
        dictData = result['dictData']
        points = dictData['points'] if 'points' in dictData else 0
        
        self.lineEditPoints.setText(f"{points:.2f}")
        
        self.manageSales.activeOrder[orderIndex]['orderMember'] = dictData if dictData else None
        
    def _onPushButtonClearClicked(self):
        confirm = QMessageBox.warning(self, 'Confirm', "Delete all items?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.manageSales.activeOrder[self.manageSales.tabWidgetOrder.currentIndex()]['orderItem'].clear()
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
     
class InOrder(Ui_DialogInOrder, QDialog):
    def __init__(self, manageSales, authData, selectedOrder):
        super().__init__()
        self.setupUi(self)
        
        self.manageSales: ManageSales = manageSales
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.organizationData = authData['organization']
        self.authData = authData
        self.userData = authData['user']
        self.selectedOrder = selectedOrder
        self.currentThread = None
        self.activeThreads = []

        self.cashPayment = 0.0
        self.pointsPayment = 0.0
        self.hybridPayment = 0.0

        self.lineEditCash.setValidator(billFormatValidator())

        self.labelCashShortageExcess.setText('0.00')
        self.labelPointsShortageExcess.setText('0.00')
        self.labelHybridShortageExcess.setText('0.00')

        self._populateTableWidgetData()
        self._populateSelectedMemberFields()
        self._populatePaymentEligibilityFields()

        self.lineEditCash.textChanged.connect(self._populatePaymentEligibilityFields)
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
        self.pushButtonPayHybrid.clicked.connect(lambda: self._processOrder('HYBRID'))

    def _processOrder(self, paymentType):
        paymentAmount = 0.0
        paymentChange = 0.0
        
        if paymentType == 'CASH':
            paymentAmount = self.cashPayment
            paymentChange = float(self.labelCashShortageExcess.text())
        if paymentType == 'POINTS':
            paymentAmount = self.pointsPayment
            paymentChange = float(self.labelPointsShortageExcess.text())
        if paymentType == 'HYBRID':
            paymentAmount = self.hybridPayment
            paymentChange = float(self.labelHybridShortageExcess.text())
            
        confirm = QMessageBox.warning(self, 'Confirm', f"Payment amount is <b>{paymentAmount}</b>. Proceed?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.currentThread = PurchaseThread('purchase_item', {
                'organization': self.organizationData,
                'user': self.userData,
                'member': self.selectedOrder['orderMember'],
                'order': {
                    'name': self.selectedOrder['orderName'],
                    'type': self.selectedOrder['orderType'],
                    'item': self.selectedOrder['orderItem'],
                    'status': self.selectedOrder['orderStatus'],
                    'widget': self.selectedOrder['orderWidget'],
                },
                'summary': {
                    'subtotal': float(self.labelSubtotal.text()),
                    'discount': float(self.labelDiscount.text()),
                    'tax': float(self.labelTax.text()),
                    'grandTotal': float(self.labelGrandTotal.text()),
                },
                'payment': {
                    'type': paymentType,
                    'amount': paymentAmount,
                    'change': paymentChange,
                }
            })
            self.currentThread.finished.connect(self._handleOnPushButtonPayCashPointsHybridClickedFinished)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)
        pass
    def _handleOnPushButtonPayCashPointsHybridClickedFinished(self, result):
        self.close()
        self.postOrder = PostOrder(self.manageSales, self.authData, result['dictData'])
        self.postOrder.exec()

    def _populateSelectedMemberFields(self):
        orderMember = self.selectedOrder['orderMember']
        self.lineEditMemberName.setText(f"{orderMember['memberName']}" if orderMember else 'N/A')
        self.lineEditMobileNumber.setText(f"{orderMember['mobileNumber']}" if orderMember else 'N/A')
        self.lineEditPoints.setText(f"{orderMember['points']}" if orderMember else 'N/A')

    def _onPushButtonKeyClicked(self, key):
        if key == 'DEL':
            self.cashPayment = self.lineEditCash.text()
            self.lineEditCash.setText(self.cashPayment[:-1])
            return

        self.cashPayment = self.lineEditCash.text()
        self.cashPayment = self.cashPayment + key
        state, _, _ = billFormatValidator().validate(self.cashPayment, 0)
        
        if state == 2:
            self.lineEditCash.setText(self.cashPayment)

    def _populatePaymentEligibilityFields(self):
        orderMember = self.selectedOrder['orderMember']
        grandTotal = float(self.labelGrandTotal.text())
        
        self.cashPayment = self.lineEditCash.text()
        self.cashPayment = float(self.cashPayment if self.cashPayment else 0.0)
        cashShortageExcess = self.cashPayment - grandTotal
        
        self.labelCashPayment.setText(f"{self.cashPayment}")
        self.labelCashShortageExcess.setText(f"{cashShortageExcess}")
        
        self.pushButtonPayCash.setEnabled(self.cashPayment >= grandTotal)
        
        if orderMember:
            self.pointsPayment = orderMember['points']
            self.hybridPayment = self.cashPayment + self.pointsPayment
            pointsShortageExcess = self.pointsPayment - grandTotal
            hybridShortageExcess = self.hybridPayment - grandTotal
            
            self.labelPointsPayment.setText(f"{self.pointsPayment}")
            self.labelHybridPayment.setText(f"{self.hybridPayment}")
            self.labelPointsShortageExcess.setText(f"{pointsShortageExcess}")
            self.labelHybridShortageExcess.setText(f"{hybridShortageExcess}")
            
            self.pushButtonPayPoints.setEnabled(self.pointsPayment >= grandTotal)
            self.pushButtonPayHybrid.setEnabled(self.hybridPayment == grandTotal)
            return
    
        self.labelPointsPayment.setText('N/A')
        self.labelHybridPayment.setText('N/A')
        self.labelPointsShortageExcess.setText('N/A')
        self.labelHybridShortageExcess.setText('N/A')
        self.pushButtonPayPoints.setEnabled(False)
        self.pushButtonPayHybrid.setEnabled(False)

    def _populateTableWidgetData(self):
        orderItem = self.selectedOrder['orderItem']
        rowCount = len(orderItem)
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(rowCount)
        
        subtotal = 0.00
        discount = 0.00
        tax = 0.00
        customDiscount = 0.00
        grandTotal = 0.00
        
        for i, data in enumerate(orderItem):
            manageActionButton = ManageActionButton(discount=True)
            tableItems = [
                QTableWidgetItem(f"{data['quantity']}"),
                QTableWidgetItem(f"{data['itemName']}"),
                QTableWidgetItem(f"{data['total']}"),
                QTableWidgetItem(f"{data['customDiscount']}"),
            ]
            
            self.tableWidgetData.setCellWidget(i, 0, manageActionButton) 
            
            for j, tableitem in enumerate(tableItems):
                self.tableWidgetData.setItem(i, (j + 1), tableItems[j])
                
                if data['promoName'] is not None:
                    tableitem.setForeground(QColor(255, 0, 0))
                    
            # TODO: add tax and discount and implement it properly and clean
            subtotal += float(data['total'])
            customDiscount = float(data['customDiscount'])
            grandTotal = ((subtotal + tax) - discount) - customDiscount
            
            manageActionButton.pushButtonDiscount.clicked.connect(lambda _, index=i, data=data: self._onPushButtonDiscountClicked(index, data))
            
        self.labelSubtotal.setText(f"{subtotal:.2f}")
        self.labelDiscount.setText(f"{discount:.2f}")
        self.labelTax.setText(f"{tax:.2f}")
        self.labelCustomDiscount.setText(f"{customDiscount:.2f}")
        self.labelGrandTotal.setText(f"{grandTotal:.2f}")

    def _onPushButtonDiscountClicked(self, index, data):
        customDiscount, confirm = QInputDialog.getDouble(self, 'Quantity', "Set custom discount:", 1, 1, 9999999, 2)
        
        if confirm is True:
            self.selectedOrder['orderItem'][index]['customDiscount'] = customDiscount
            
            self._populateTableWidgetData()
        
    def _onPushButtonCancelClicked(self):
        self.close()

    def _cleanupThread(self):
        sender = self.sender()
        if sender in self.activeThreads:
            self.activeThreads.remove(sender)
        self.currentThread = None
        print('active threads:', self.activeThreads)

    def closeEvent(self, event):
        for data in self.selectedOrder['orderItem']:
            data['customDiscount'] = 0.0
        
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
        
        self.manageSales: ManageSales = manageSales
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.selectedOrder = selectedOrder
        self.currentThread = None
        self.activeThreads = []

        self.labelPayment.setText(f"{selectedOrder['amount']}")
        self.labelGrandTotal.setText(f"{selectedOrder['grandTotal']}")
        self.labelChange.setText(f"{selectedOrder['change']}")
        
        self.pushButtonClose.clicked.connect(self._onPushButtonCloseClicked)

    def _onPushButtonCloseClicked(self):
        self.manageSales.onTabWidgetOrderTabCloseRequested(
            index=self.manageSales.tabWidgetOrder.currentIndex(),
            confirmation=False,
        )
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
