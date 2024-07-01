import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit
from PyQt5.QtCore import QEvent
from sqlalchemy.sql import func
from machineid import id

sys.path.append(os.path.abspath(''))
from app.ui.dialogs.login_ui import Ui_DialogLogin
from app.models.system import session
from app.models.association import User, Organization, Configuration

class Login(Ui_DialogLogin, QDialog):
    def __init__(self):
        super().__init__()
        self.windowEvent = 'NO_EVENT'
        self.setupUi(self)

        self.userId = None
        # --
        self.pushButtonAccessCodeVisibility.setText('Show')

        self.pushButtonAccessCodeVisibility.clicked.connect(self.onPushButtonVisibilityIndicator)
        self.pushButtonSignUp.clicked.connect(self.onPushButtonSignUpClicked)

    def onPushButtonVisibilityIndicator(self):
        accessCodeVisibility = self.pushButtonAccessCodeVisibility.isChecked()
        
        self.lineEditAccessCode.setEchoMode(QLineEdit.Normal if accessCodeVisibility else QLineEdit.Password)
        self.pushButtonAccessCodeVisibility.setText('Hide' if accessCodeVisibility else 'Show')

    def onPushButtonSignUpClicked(self):
        self.windowEvent = 'START_SIGNUP'
        self.close()

    def closeEvent(self, event:QEvent):
        event.accept()
        pass