import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QEventLoop

sys.path.append(os.path.abspath(''))
from app.ui.dialogs.signup_ui import Ui_DialogSignUp
from app.models.system import session
from app.models.association import User, Organization, Configuration

class SignUp(Ui_DialogSignUp, QDialog):
    def __init__(self):
        super().__init__()
        self.windowEvent = 'NO_EVENT'
        self.setupUi(self)
        # --
        self.pushButtonCancel.clicked.connect(self.onPushButtonCancelClicked)

    def onPushButtonCancelClicked(self):
        self.windowEvent = 'START_LOGIN'
        self.close()
        
    def closeEvent(self, event):
        event.accept()
        pass