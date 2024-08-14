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
        
        self.pushButtonClear
        self.pushButtonDiscard
        self.pushButtonPark
        self.pushButtonPay
        
        self.labelSubtotal
        self.labelDiscount
        self.labelTax
        self.labelGrandTotal
        
        self.tableWidgetData
        
    def populateTableWidgetData(self, entry):
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(entry))
        
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
                    
            preOrderActionButton.pushButtonAddExact.clicked.connect(lambda _, index=i, entry=entry: self._onPushButtonAddExactClicked(index, entry))
            preOrderActionButton.pushButtonAddOne.clicked.connect(lambda _, index=i, entry=entry: self._onPushButtonAddOneClicked(index, entry))
            preOrderActionButton.pushButtonDeleteAll.clicked.connect(lambda _, index=i, entry=entry: self._onPushButtonDeleteAllClicked(index, entry))
            preOrderActionButton.pushButtonDeleteOne.clicked.connect(lambda _, index=i, entry=entry: self._onPushButtonDeleteOneClicked(index, entry))
            
    def _onPushButtonAddExactClicked(self, index, entry):
        print('entry:', json.dumps(entry, indent=4, default=str))
        pass
    def _onPushButtonAddOneClicked(self, index, entry):
        # TODO: FINALIZE THIS
        itemId = f"{entry[index]['itemId']}"
        itemName = f"{entry[index]['itemName']}"
        promoName = f"{entry[index]['promoName']}"
        price = float(entry[index]['price'])
        
        item = self.manageSales.activeOrder[self.manageSales.orderIndex]['orderItem'][index]
        item['quantity'] += 1
        item['total'] += price
        print('entry:', json.dumps(entry, indent=4, default=str))
        pass
    def _onPushButtonDeleteAllClicked(self, index, entry):
        print('entry:', json.dumps(entry, indent=4, default=str))
        pass
    def _onPushButtonDeleteOneClicked(self, index, entry):
        print('entry:', json.dumps(entry, indent=4, default=str))
        pass