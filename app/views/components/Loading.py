
import os, sys

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.views.templates.Loading_ui import Ui_FormLoading

class Loading(Ui_FormLoading, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            event.ignore()
            return
        
        event.accept() # for pressing keys