import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit
from PyQt5.QtCore import QEvent
from machineid import id

sys.path.append(os.path.abspath(''))
from app.ui.Login_ui import Ui_DialogLogin
from app.utils.crud import CRUDThread

class LoginController(Ui_DialogLogin, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.windowEvent = 'NO_EVENT'
        self.currentUserData = None
        
        self.pushButtonAccessCodeVisibility.setText('Show')

        self.pushButtonAccessCodeVisibility.clicked.connect(self._onPushButtonAccessCodeVisibilityClicked)
        self.pushButtonSignUp.clicked.connect(self._onPushButtonSignUpClicked)
        self.pushButtonSetup.clicked.connect(self._onPushButtonSetupClicked)
        self.pushButtonLogin.clicked.connect(self._onPushButtonLoginClicked)

    def _onPushButtonAccessCodeVisibilityClicked(self):
        accessCodeVisibility = self.pushButtonAccessCodeVisibility.isChecked()
        
        self.lineEditAccessCode.setEchoMode(QLineEdit.Normal if accessCodeVisibility else QLineEdit.Password)
        self.pushButtonAccessCodeVisibility.setText('Hide' if accessCodeVisibility else 'Show')

    def _onPushButtonSetupClicked(self):
        self.windowEvent = 'START_SETUP'
        self.close()

    def _onPushButtonSignUpClicked(self):
        self.windowEvent = 'START_SIGNUP'
        self.close()

    def _onPushButtonLoginClicked(self):
        self.crudThread = CRUDThread()
        self.crudThread.setRequirements(self, 'getOneUserByUserNameAccessCode', {
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
        })
        
    def _handleOnPushButtonLoginClickedResult(self, result):
        if result['userId'] == None:
            QMessageBox.critical(self, 'Error', "User not found.")
            return
            
        self.windowEvent = 'START_MANAGE'
        self.currentUserData = result
        self.close()

    def closeEvent(self, event:QEvent):
        event.accept()
        pass