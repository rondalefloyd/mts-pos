import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QEventLoop

sys.path.append(os.path.abspath(''))
from app.ui.dialogs.UserConfig_ui import Ui_DialogUserConfig
from app.utils.helpers import (
    updateUser,
    getOneUserWithUserId,
    getOneOrganizationWithOrganizationId,
)

class UserConfigController(Ui_DialogUserConfig, QDialog):
    def __init__(self, userId):
        super().__init__()
        self.windowEvent = 'NO_EVENT'
        self.setupUi(self)
        
        self.userId = userId
        # --
        self.pushButtonCancel.clicked.connect(self.onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self.onPushButtonCreateClicked)
        
        self.populateEntryFields()

    def populateEntryFields(self):
        resultA = getOneUserWithUserId(self, {'userId': self.userId})
        resultB = getOneOrganizationWithOrganizationId(self, {'organizationId': resultA['organizationId']})
        
        self.comboBoxOrganizationName.setCurrentText(f"{resultB['organizationName']}")
        self.lineEditUserName.setText(f"{resultA['userName']}")
        self.lineEditAccessCode.setText(f"{resultA['accessCode']}")
        self.lineEditFullName.setText(f"{resultA['fullName']}")
        self.dateEditBirthDate.setDate(QDate.fromString(resultA['birthDate'], 'yyyy-MM-dd'))
        self.lineEditMobileNumber.setText(f"{resultA['mobileNumber']}")
        self.comboBoxAccessLevel.setCurrentText(f"{resultA['accessLevel']}")

    def onPushButtonCreateClicked(self):
        entry = {
            'userId': f"{self.userId}",
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
            'fullName': f"{self.lineEditFullName.text()}".upper(),
            'birthDate': f"{self.dateEditBirthDate.text()}",
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
        }
        
        isSuccess = updateUser(self, entry)
        
        if isSuccess is True:
            QMessageBox.information(self, 'Success', "User updated.")

    def onPushButtonCancelClicked(self):
        self.windowEvent = 'START_LOGIN'
        self.close()
        
    def closeEvent(self, event):
        event.accept()
        pass