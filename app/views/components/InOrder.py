import os
import sys
import logging
import json
import copy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.InOrder_ui import Ui_DialogInOrder
from app.views.components.Loading import Loading
from app.views.components.ManageActionButton import ManageActionButton
from app.views.validator import *
from app.controllers.dedicated.purchase import PurchaseThread

class InOrder(Ui_DialogInOrder, QDialog):
    def __init__(self, authData, selectedOrder):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.organizationData = authData['organization']
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
        payment = 0.0
        change = 0.0
        
        if paymentType == 'CASH':
            payment = self.cashPayment
            change = float(self.labelCashShortageExcess.text())
        if paymentType == 'POINTS':
            payment = self.pointsPayment
            change = float(self.labelPointsShortageExcess.text())
        if paymentType == 'HYBRID':
            payment = self.hybridPayment
            change = float(self.labelHybridShortageExcess.text())
            
        confirm = QMessageBox.warning(self, 'Confirm', f"Payment amount is <b>{payment}</b>. Proceed?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            # TODO: add thread here where it registers all of the items in the cart
            # TODO: THIS IS THE PRIORITY. FINISH THIS FIRST
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
                    'amount': payment,
                    'change': change,
                }
            })
            self.currentThread.finished.connect(self._handleOnPushButtonPayCashPointsHybridClickedResult)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)
        pass
    def _handleOnPushButtonPayCashPointsHybridClickedResult(self, result):
        print('result:', result)
        pass

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
