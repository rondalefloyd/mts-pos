
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.PreOrder_ui import Ui_FormPreOrder

class PreOrder(Ui_FormPreOrder, QWidget):
    def __init__(self, sourceWidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.tableWidgetData.clearContents()
        
        self.sourceWidget = sourceWidget
        
        self.labelOrderType
        
        self.pushButtonClear
        self.pushButtonDiscard
        self.pushButtonPark
        self.pushButtonPay
        
        self.labelSubtotal
        self.labelDiscount
        self.labelTax
        self.labelGrandTotal
        
        self.tableWidgetData