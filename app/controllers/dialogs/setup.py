import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QEventLoop

sys.path.append(os.path.abspath(''))
from app.ui.dialogs.Setup_ui import Ui_DialogSetup
from app.utils.database_operation import addNewOrganization

class SetupController(Ui_DialogSetup, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.windowEvent = 'NO_EVENT'

        self.pushButtonCancel.clicked.connect(self.onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self.onPushButtonCreateClicked)

    def onPushButtonCancelClicked(self):
        self.windowEvent = 'START_LOGIN'
        self.close()
        
    def onPushButtonCreateClicked(self):
        isSuccess = addNewOrganization(self, {
            'taxId': f"{self.lineEditTaxId.text()}",
            'organizationName': f"{self.lineEditOrganizationName.text()}".upper(),
            'address': f"{self.lineEditAddress.text()}".upper(),
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
        })
        
        if isSuccess is False:
            QMessageBox.information(self, 'Error', "Failed to add organization.")
            
        QMessageBox.information(self, 'Success', "New organization added.")

    def closeEvent(self, event):
        event.accept()
        pass