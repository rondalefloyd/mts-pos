# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.Login_ui import Ui_DialogLogin
from app.views.components.Loading import Loading
from app.controllers.dedicated.authenticate import AuthenticateThread

# class definition
class Login(Ui_DialogLogin, QDialog):
    # initialization method (__init__)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = None
        self.currentThread = None
        self.activeThreads = []
        
        self.pushButtonAccessCodeVisibility.setText('Show')
        
        self.pushButtonSetup.clicked.connect(self._onPushButtonSetupClicked)
        self.pushButtonSignUp.clicked.connect(self._onPushButtonSignUpClicked)
        self.pushButtonLogin.clicked.connect(self._onPushButtonLoginClicked)
        self.pushButtonAccessCodeVisibility.clicked.connect(self._onPushButtonAccessCodeVisibilityClicked)
    
    # private methods
    def _onPushButtonAccessCodeVisibilityClicked(self):
        pushButtonAccessCodeVisibilityIsChecked = self.pushButtonAccessCodeVisibility.isChecked() is True
        self.pushButtonAccessCodeVisibility.setText('Hide' if pushButtonAccessCodeVisibilityIsChecked else 'Show')
        self.lineEditAccessCode.setEchoMode(QLineEdit.Normal if pushButtonAccessCodeVisibilityIsChecked else QLineEdit.Password)
        
    def _onPushButtonSetupClicked(self):
        self.windowEvent = 'start/setup'
        self.close()
    
    def _onPushButtonSignUpClicked(self):
        self.windowEvent = 'start/sign-up'
        self.close()
        
        
    def _onPushButtonLoginClicked(self):
        self.currentThread = AuthenticateThread('pos/authenticate/user/username/accesscode', {
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
        })
        self.currentThread.finished.connect(self._handleOnPushButtonLoginClickedResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
    
    def _handleOnPushButtonLoginClickedResult(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
        
        self.windowEvent = 'start/manage'
        self.userData = result['data']
        self.close()
        return


    def _cleanupThread(self):
        sender = self.sender()
        if sender in self.activeThreads:
            self.activeThreads.remove(sender)
        self.currentThread = None
        print('active threads:', self.activeThreads)

    # overridden methods
    def closeEvent(self, event):
        for thread in self.activeThreads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        
        self.activeThreads.clear()
        
        event.accept()
        
        print('closed...')