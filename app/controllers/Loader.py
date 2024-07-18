import os, sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QLineEdit
from PyQt5.QtCore import Qt, QEvent
from machineid import id

sys.path.append(os.path.abspath(''))
from app.ui.Loader_ui import Ui_FormLoader
from app.utils.dbops_helpers import GetDataThread

class LoaderController(Ui_FormLoader, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._setupInitialTask()
        self._setupThreads()
    
    def _setupInitialTask(self):
        self.windowEvent = 'NO_EVENT'
        self.setWindowFlags(Qt.FramelessWindowHint)
        
    def _setupThreads(self):
        pass
    
    def closeEvent(self, event:QEvent):
        event.accept()
        pass