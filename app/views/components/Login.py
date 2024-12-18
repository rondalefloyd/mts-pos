# import
import os, sys, json

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.Login_ui import Ui_DialogLogin
from app.views.components.Loading import Loading
from app.utils.helpers.formatter import *
from app.controllers.dedicated.authenticate import AuthenticateThread

# class definition
class Login(Ui_DialogLogin, QDialog):
    # initialization method (__init__)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = None
        self.currentThread = None
        self.activeThreads = []
        
        self.pushButtonPasswordVisibility.setText('Show')
        
        self.pushButtonSetup.clicked.connect(self._onPushButtonSetupClicked)
        self.pushButtonSignUp.clicked.connect(self._onPushButtonSignUpClicked)
        self.pushButtonLogin.clicked.connect(self._onPushButtonLoginClicked)
        self.pushButtonPasswordVisibility.clicked.connect(self._onPushButtonPasswordVisibilityClicked)
    
    # private methods
    def _onPushButtonPasswordVisibilityClicked(self):
        pushButtonPasswordVisibilityIsChecked = self.pushButtonPasswordVisibility.isChecked() is True
        self.pushButtonPasswordVisibility.setText('Hide' if pushButtonPasswordVisibilityIsChecked else 'Show')
        self.lineEditPassword.setEchoMode(QLineEdit.Normal if pushButtonPasswordVisibilityIsChecked else QLineEdit.Password)
        
    def _onPushButtonSetupClicked(self):
        self.windowEvent = EVENT_START_SETUP
        self.close()
    
    def _onPushButtonSignUpClicked(self):
        self.windowEvent = EVENT_START_SIGNUP
        self.close()
        
        
    def _onPushButtonLoginClicked(self):
        self.loading.show()
        self.currentThread = AuthenticateThread('authenticateUserByUserNameAccessCode', {
            'userName': self.lineEditUserName.text(),
            'password': self.lineEditPassword.text(),
        })
        self.currentThread.finished.connect(self._handleOnPushButtonLoginClickedFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
    
    def _handleOnPushButtonLoginClickedFinished(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
        
        self.windowEvent = EVENT_START_MANAGE
        self.authData = result['dictData']
        
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
        
        event.accept() # for closing the window
        
        print('closed...')