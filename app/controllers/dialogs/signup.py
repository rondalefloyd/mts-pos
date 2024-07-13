import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QEventLoop

sys.path.append(os.path.abspath(''))
from app.ui.dialogs.SignUp_ui import Ui_DialogSignUp
from app.utils.helpers import (
    addNewUser, 
    getAllOrganization
)

class SignUpController(Ui_DialogSignUp, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.windowEvent = 'NO_EVENT'

        self.pushButtonCancel.clicked.connect(self.onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self.onPushButtonCreateClicked)
        
        self.populateComboBoxOrganizationName()

    def onPushButtonCancelClicked(self):
        self.windowEvent = 'START_LOGIN'
        self.close()

    def onPushButtonCreateClicked(self):
        isSuccess = addNewUser(self, {
            'organizationName': f"{self.comboBoxOrganizationName.currentText()}".upper(),
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
            'fullName': f"{self.lineEditFullName.text()}".upper(),
            'birthDate': f"{self.dateEditBirthDate.text()}",
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessLevel': f"{self.comboBoxAccessLevel.currentText()}",
        })
        
        if isSuccess is False:
            QMessageBox.information(self, 'Error', "Failed to add user.")
            
        QMessageBox.information(self, 'Success', "New user added.")

    def populateComboBoxOrganizationName(self):
        self.comboBoxOrganizationName.clear()
        for result in getAllOrganization(self):
            self.comboBoxOrganizationName.addItem(f"{result['organizationName']}")

    def closeEvent(self, event):
        event.accept()
        pass