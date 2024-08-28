
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.PreOrderActionButton_ui import Ui_FormPreOrderActionButton

class PreOrderActionButton(Ui_FormPreOrderActionButton, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)