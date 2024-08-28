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
from app.controllers.dedicated.fetch import *
from app.controllers.dedicated.purchase import *
   
class ManageSales(Ui_FormManageSales, QWidget):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        self.window_event = EVENT_NO_EVENT

class PreOrder(Ui_FormPreOrder, QWidget):
    def __init__(self, manageSales):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.manageSales: ManageSales = manageSales
     
class InOrder(Ui_DialogInOrder, QDialog):
    def __init__(self, manageSales, authData, selectedOrder):
        super().__init__()
        self.setupUi(self)
        self.manageSales: ManageSales = manageSales
        self.window_event = EVENT_NO_EVENT
        

class PostOrder(Ui_DialogPostOrder, QDialog):
    def __init__(self, manageSales, authData, selectedOrder):
        super().__init__()
        self.setupUi(self)
        self.manageSales: ManageSales = manageSales
        self.window_event = EVENT_NO_EVENT
        
