import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QEventLoop

sys.path.append(os.path.abspath(''))
from app.ui.dialogs.OrganizationConfig_ui import Ui_DialogOrganizationConfig
from app.utils.helpers import (
    updateOrganization,
    getOneOrganizationWithOrganizationId,
)

class OrganizationConfigController(Ui_DialogOrganizationConfig, QDialog):
    def __init__(self, organizationId):
        super().__init__()
        self.windowEvent = 'NO_EVENT'
        self.setupUi(self)
        
        self.organizationId = organizationId
        # --
        self.pushButtonCancel.clicked.connect(self.onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self.onPushButtonCreateClicked)
        
        self.populateEntryFields()

    def populateEntryFields(self):
        result = getOneOrganizationWithOrganizationId(self, {'organizationId': self.organizationId})
        
        self.lineEditOrganizationName.setText(f"{result['organizationName']}")
        self.lineEditAddress.setText(f"{result['address']}")
        self.lineEditMobileNumber.setText(f"{result['mobileNumber']}")
        self.lineEditTaxId.setText(f"{result['taxId']}")
        self.lineEditAccessCode.setText(f"{result['accessCode']}")

    def onPushButtonCreateClicked(self):
        entry = {
            'organizationId': f"{self.organizationId}",
            'organizationName': f"{self.lineEditOrganizationName.text()}".upper(),
            'address': f"{self.lineEditAddress.text()}".upper(),
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'taxId': f"{self.lineEditTaxId.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
        }
        
        isSuccess = updateOrganization(self, entry)
        
        if isSuccess is True:
            QMessageBox.information(self, 'Success', "Organization updated.")

    def onPushButtonCancelClicked(self):
        self.windowEvent = 'START_LOGIN'
        self.close()
        
    def closeEvent(self, event):
        event.accept()
        pass