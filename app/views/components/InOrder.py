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
from app.controllers.dedicated.edit import EditThread

class InOrder(Ui_DialogInOrder, QDialog):
    def __init__(self, userData, selectedOrder):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.userData = userData
        self.selectedOrder = selectedOrder
        self.currentThread = None
        self.activeThreads = []

        self.lineEditCash.setValidator(billFormatValidator())

        orderMember = self.selectedOrder['orderMember']
        if orderMember is not None:
            self.lineEditMemberName.setText(f"{orderMember['memberName']}")
            self.lineEditMobileNumber.setText(f"{orderMember['mobileNumber']}")
            self.lineEditPoints.setText(f"{orderMember['points']}")

        self._populateTableWidgetData()

        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonKeyOne
        self.pushButtonKeyTwo
        self.pushButtonKeyThree
        self.pushButtonKeyFour
        self.pushButtonKeyFive
        self.pushButtonKeySix
        self.pushButtonKeySeven
        self.pushButtonKeyEight
        self.pushButtonKeyNine

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
