import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QEventLoop

sys.path.append(os.path.abspath(''))
from app.ui.Setup_ui import Ui_DialogSetup
from app.utils.crud import addNewOrganization

class SetupController(Ui_DialogSetup, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.windowEvent = 'NO_EVENT'

        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self._onPushButtonCreateClicked)

    def _onPushButtonCancelClicked(self):
        self.windowEvent = 'START_LOGIN'
        self.close()
        
    def _onPushButtonCreateClicked(self):
        result = addNewOrganization(self, {
            'taxId': f"{self.lineEditTaxId.text()}",
            'organizationName': f"{self.lineEditOrganizationName.text()}".upper(),
            'address': f"{self.lineEditAddress.text()}".upper(),
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
        })
        
        if result is False:
            QMessageBox.critical(self, 'Error', "Failed to add organization.")
            return
            
        QMessageBox.information(self, 'Success', "New organization added.")

    def closeEvent(self, event):
        event.accept()
        pass