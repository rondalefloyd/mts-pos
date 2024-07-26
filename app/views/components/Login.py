
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.Login_ui import Ui_DialogLogin
from app.views.components.Loading import Loading
from app.controllers.Authenticate import Authenticate

class Login(Ui_DialogLogin, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = None
        
        self.pushButtonLogin.clicked.connect(self.onPushButtonLoginClicked)
        
    def onPushButtonLoginClicked(self):
        self.loading.show()
        self.authenticate = Authenticate('pos/authenticate/user/password', {
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
        })
        self.authenticate.finished.connect(self.handleOnPushButtonLoginClickedResult)
        self.authenticate.start()
    
    def handleOnPushButtonLoginClickedResult(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Invalid', "User not found")
            
            self.loading.close()
            return
        
        self.windowEvent = 'start/manage'
        self.userData = result['data']
        self.loading.close()
        self.close()
        
        return
    
    def closeEvent(self, event):
        event.accept()
        print('closed...')