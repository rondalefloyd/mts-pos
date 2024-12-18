
import os, sys

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.views.templates.PreOrderActionButton_ui import Ui_FormPreOrderActionButton

class PreOrderActionButton(Ui_FormPreOrderActionButton, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButtonAddOne.setText("")
        self.pushButtonAddExact.setText("")
        self.pushButtonDeleteOne.setText("")
        self.pushButtonDeleteAll.setText("")
        
        self.setWindowFlags(Qt.FramelessWindowHint)