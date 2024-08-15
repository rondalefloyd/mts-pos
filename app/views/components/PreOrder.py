import os, sys, logging, json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.components.PreOrderActionButton import PreOrderActionButton
from app.views.templates.PreOrder_ui import Ui_FormPreOrder

class PreOrder(Ui_FormPreOrder, QWidget):
    def __init__(self, manageSales):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.manageSales = manageSales
        
        self.tableWidgetData.clearContents()
        
        self.pushButtonDiscard
        self.pushButtonPark
        self.pushButtonPay
        
        self.labelSubtotal.setText("0.00")
        self.labelDiscount.setText("0.00")
        self.labelTax.setText("0.00")
        self.labelGrandTotal.setText("0.00")
        
        self.tableWidgetData
        self.pushButtonClear.clicked.connect(self._onPushButtonClearClicked)
        
    def _onPushButtonClearClicked(self):
        confirm = QMessageBox.warning(self, 'Confirm', "Delete all items?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            orderItem = self.manageSales.activeOrder[self.manageSales.orderIndex]['orderItem']
            orderItem.clear()
            self.populateTableWidgetData(orderItem)
        
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
            
        self.labelSubtotal.setText(f"{subtotal}")
        self.labelDiscount.setText(f"{discount}")
        self.labelTax.setText(f"{tax}")
        self.labelGrandTotal.setText(f"{grandTotal}")
            
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
        