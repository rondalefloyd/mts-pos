import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QEventLoop

sys.path.append(os.path.abspath(''))
from app.ui.dialogs.setup_ui import Ui_DialogSetup
from app.models.system import session
from app.models.association import User, Organization, Configuration

class Setup(Ui_DialogSetup, QDialog):
    def __init__(self):
        super().__init__()
        self.windowEvent = 'NO_EVENT'
        self.setupUi(self)

        self.pushButtonCancel.clicked.connect(self.onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self.onPushButtonCreateClicked)
        pass

    def onPushButtonCancelClicked(self):
        self.windowEvent = 'START_LOGIN'
        self.close()

    def onPushButtonCreateClicked(self):
        try:
            organizationName = f"{self.lineEditOrganizationName.text()}".upper()
            address = f"{self.lineEditAddress.text()}".upper()
            mobileNumber = f"{self.lineEditMobileNumber.text()}"
            taxId = f"{self.lineEditTaxId.text()}"
            accessCode = f"{self.lineEditAccessCode.text()}"
            
            if any(entry == "" for entry in (organizationName, address, mobileNumber, taxId, accessCode)):
                QMessageBox.critical(self, 'Invalid', f"Please fill the field with missing entry.")
                return

            existingData = session.query(Organization)
            existingData = existingData.filter(
                (Organization.OrganizationName == organizationName) & 
                (Organization.Address == address)
            ).first()
            
            if existingData:
                QMessageBox.critical(self, 'Invalid', "Organization branch already exists")
                session.rollback()
                return

            else:
                organization = Organization()
                organization.OrganizationName = organizationName
                organization.Address = address
                organization.MobileNumber = mobileNumber
                organization.TaxId = taxId
                organization.AccessCode = accessCode
                
                session.add(organization)
                session.commit()
                
                QMessageBox.information(self, 'Success', "Organization succussfully created.")

        except Exception as error:
            session.rollback()
            QMessageBox.critical(self, 'Error', f"Error: {error}")
            print('error at onPushButtonCreate:', error)

        finally:
            session.close()
            print('session closed')

    def closeEvent(self, event):
        event.accept()
        pass