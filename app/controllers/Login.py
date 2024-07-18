import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit
from PyQt5.QtCore import QEvent
from machineid import id

sys.path.append(os.path.abspath(''))
from app.ui.Login_ui import Ui_DialogLogin
from app.controllers.Loader import LoaderController
from app.utils.dbops_helpers import GetDataThread

class LoginController(Ui_DialogLogin, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._setupInitialTask()
        self._setupThreads()
    
    def _setupInitialTask(self):
        self.windowEvent = 'NO_EVENT'
        self.currentUserData = None
    
        self.pushButtonAccessCodeVisibility.clicked.connect(self._onPushButtonAccessCodeVisibilityClicked)
        self.pushButtonSetup.clicked.connect(self._onPushButtonSetupClicked)
        self.pushButtonSignUp.clicked.connect(self._onPushButtonSignUpClicked)
        self.pushButtonLogin.clicked.connect(self._onPushButtonLoginClicked)
        
    def _setupThreads(self):
        self.getDataThread = GetDataThread()
        pass
        
    def _onPushButtonAccessCodeVisibilityClicked(self):
        pass
    
    def _onPushButtonSetupClicked(self):
        pass

    def _onPushButtonSignUpClicked(self):
        pass

    def _onPushButtonLoginClicked(self):
        self.loaderController = LoaderController()
        self.loaderController.show()
        self.getDataThread.finished.connect(self._handleLoginResult)
        self.getDataThread.setRequirements(self, '_getOneUserByUserNameAccessCode', {
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
        })
        self.getDataThread.start()
        pass

    def _handleLoginResult(self, result):
        self.currentUserData = result
        self.getDataThread.finished.disconnect()
        self.loaderController.close()
        self.windowEvent = 'START_MANAGE'
        self.close()
    
    def closeEvent(self, event:QEvent):
        event.accept()
        pass