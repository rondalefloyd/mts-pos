import os, sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from PyQt5.QtCore import QEvent
from machineid import id

sys.path.append(os.path.abspath(''))
from app.ui.Manage_ui import Ui_MainWindowManage
from app.utils.dbops_helpers import status, GetDataThread

class ManageController(Ui_MainWindowManage, QMainWindow):
    def __init__(self, currentUserData):
        super().__init__()
        self.setupUi(self)
        self._setupInitialTask(currentUserData)
        self._setupThreads()
    
    def _setupInitialTask(self, currentUserData):
        self.windowEvent = 'NO_EVENT'
        self.currentUserData = currentUserData
        
        self.labelFullName.setText(f"{self.currentUserData['fullName']}")
        self.labelMobileNumber.setText(f"{self.currentUserData['mobileNumber']}")
        self.labelDatabaseSource.setText(f"{status}")
        
    def _setupThreads(self):
        pass
    
    def closeEvent(self, event:QEvent):
        self.currentUserData = None
        event.accept()
        pass