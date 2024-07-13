import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QEventLoop

sys.path.append(os.path.abspath(''))
from app.ui.dialogs.OrganizationConfig_ui import Ui_DialogOrganizationConfig
from app.utils.helpers import (
    updateOrganization,
    getOneOrganizationByOrganizationId,
)

class OrganizationConfigController(Ui_DialogOrganizationConfig, QDialog):
    def __init__(self, organizationId):
        super().__init__()
        self.setupUi(self)
        
        self.windowEvent = 'NO_EVENT'
        self.organizationId = organizationId

        self.pushButtonCancel.clicked.connect(self.onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self.onPushButtonCreateClicked)
        
        self.populateEntryFields()

    def onPushButtonCancelClicked(self):
        self.windowEvent = 'START_LOGIN'
        self.close()

    def onPushButtonCreateClicked(self):
        isSuccess = updateOrganization(self, {
            'organizationId': f"{self.organizationId}",
            'organizationName': f"{self.lineEditOrganizationName.text()}".upper(),
            'address': f"{self.lineEditAddress.text()}".upper(),
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'taxId': f"{self.lineEditTaxId.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
        })
        
        if isSuccess is False:
            QMessageBox.information(self, 'Error', "Failed to update organization.")
            
        QMessageBox.information(self, 'Success', "Organization updated.")

    def populateEntryFields(self):
        result = getOneOrganizationByOrganizationId(self, {'organizationId': self.organizationId})
        
        self.lineEditOrganizationName.setText(f"{result['organizationName']}")
        self.lineEditAddress.setText(f"{result['address']}")
        self.lineEditMobileNumber.setText(f"{result['mobileNumber']}")
        self.lineEditTaxId.setText(f"{result['taxId']}")
        self.lineEditAccessCode.setText(f"{result['accessCode']}")
    
    def closeEvent(self, event):
        event.accept()
        pass