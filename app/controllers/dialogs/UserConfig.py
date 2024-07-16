import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QEventLoop

sys.path.append(os.path.abspath(''))
from app.ui.dialogs.UserConfig_ui import Ui_DialogUserConfig
from app.utils.database_operation import (
    updateUser,
    getOneUserByUserId,
    getOneOrganizationByOrganizationId,
)

class UserConfigController(Ui_DialogUserConfig, QDialog):
    def __init__(self, userId):
        super().__init__()
        self.setupUi(self)
        
        self.windowEvent = 'NO_EVENT'
        self.userId = userId

        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self._onPushButtonCreateClicked)
        
        self._populateEntryFields()

    def _onPushButtonCancelClicked(self):
        self.windowEvent = 'START_LOGIN'
        self.close()

    def _onPushButtonCreateClicked(self):
        isSuccess = updateUser(self, {
            'userId': f"{self.userId}",
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
            'fullName': f"{self.lineEditFullName.text()}".upper(),
            'birthDate': f"{self.dateEditBirthDate.text()}",
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
        })
        
        if isSuccess is False:
            QMessageBox.critical(self, 'Error', "Failed to update user.")
            return
            
        QMessageBox.information(self, 'Success', "User updated.")

    def _populateEntryFields(self):
        resultA = getOneUserByUserId(self, {'userId': self.userId})
        resultB = getOneOrganizationByOrganizationId(self, {'organizationId': resultA['organizationId']})
        
        self.comboBoxOrganizationName.setCurrentText(f"{resultB['organizationName']}")
        self.lineEditUserName.setText(f"{resultA['userName']}")
        self.lineEditAccessCode.setText(f"{resultA['accessCode']}")
        self.lineEditFullName.setText(f"{resultA['fullName']}")
        self.dateEditBirthDate.setDate(QDate.fromString(resultA['birthDate'], 'yyyy-MM-dd'))
        self.lineEditMobileNumber.setText(f"{resultA['mobileNumber']}")
        self.comboBoxAccessLevel.setCurrentText(f"{resultA['accessLevel']}")

    def closeEvent(self, event):
        event.accept()
        pass