
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.Login_ui import Ui_DialogLogin
from app.views.components.Loading import Loading
from app.controllers.authenticate import AuthenticateThread

class Login(Ui_DialogLogin, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = None
        
        self.pushButtonSetup.clicked.connect(self._onPushButtonSetupClicked)
        self.pushButtonSignUp.clicked.connect(self._onPushButtonSignUpClicked)
        self.pushButtonLogin.clicked.connect(self._onPushButtonLoginClicked)
        
    def _onPushButtonSetupClicked(self):
        self.windowEvent = 'start/setup'
        self.close()
        pass
    
    def _onPushButtonSignUpClicked(self):
        self.windowEvent = 'start/sign-up'
        self.close()
        pass
        
    def _onPushButtonLoginClicked(self):
        self.loading.show()
        self.authenticateThread = AuthenticateThread('pos/authenticate/user/username/accesscode', {
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
        })
        self.authenticateThread.finished.connect(self._handleOnPushButtonLoginClickedResult)
        self.authenticateThread.start()
    
    def _handleOnPushButtonLoginClickedResult(self, result):
        self.loading.close()
        
        if result['success'] is False:
            QMessageBox.critical(self, 'Invalid', f"{result['message']}")
            return
        
        self.windowEvent = 'start/manage'
        self.userData = result['data']
        self.close()
        
        return
    
    def closeEvent(self, event):
        event.accept()
        print('closed...')