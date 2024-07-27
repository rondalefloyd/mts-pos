
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.Manage_ui import Ui_MainWindowManage
from app.views.components.Loading import Loading
from app.controllers.authenticate import AuthenticateThread

class Manage(Ui_MainWindowManage, QMainWindow):
    def __init__(self, userData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = userData
        
        self.actionLogout.triggered.connect(self._onActionLogoutTriggered)
        
    def _onActionLogoutTriggered(self):
        confirm = QMessageBox.warning(self, 'Confirm', f"Logout {self.userData['userName']}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.loading.show()
            self.authenticateThread = AuthenticateThread('pos/unauthenticate/user/id', {'userId': self.userData['id']})
            self.authenticateThread.finished.connect(self._handleOnActionLogoutTriggeredResult)
            self.authenticateThread.start()
        pass
        
    def _handleOnActionLogoutTriggeredResult(self, result):
        self.loading.close()
        
        if result['success'] is False:
            QMessageBox.critical(self, 'Invalid', f"{result['message']}")
            return
        
        self.windowEvent = 'start/login'
        self.userData = None
        self.close()
        pass
        
    def closeEvent(self, event):
        event.accept()
        self.windowEvent = 'start/login'
        print('closed...')