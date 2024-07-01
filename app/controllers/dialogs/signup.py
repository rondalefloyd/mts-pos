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

        self.pushButtonCancel.clicked.connect(self.onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self.onPushButtonCreateClicked)
        pass

        self.populateComboBoxOrganizationName()

    def populateComboBoxOrganizationName(self):
        allOrganizationName = session.query(Organization.OrganizationName).all()
        self.comboBoxOrganizationName.addItems([organizationName[0] for organizationName in allOrganizationName])

    def onPushButtonCancelClicked(self):
        self.windowEvent = 'START_LOGIN'
        self.close()

    def onPushButtonCreateClicked(self):
        try:
            fullName = f"{self.lineEditFullName.text()}".upper()
            birthDate = f"{self.dateEditBirthDate.text()}"
            mobileNumber = f"{self.lineEditMobileNumber.text()}"
            userName = f"{self.lineEditUserName.text()}"
            accessCode = f"{self.lineEditAccessCode.text()}"
            accessLevel = f"{self.comboBoxAccessLevel.currentText()}"
            organizationName = f"{self.comboBoxOrganizationName.currentText()}"
            
            selectedOrganization = session.query(Organization)
            selectedOrganization = selectedOrganization.filter(Organization.OrganizationName == organizationName).first()
            
            print('--selectedOrganization.OrganizationId:', selectedOrganization.OrganizationId)
            
            if any(entry == "" for entry in (fullName, birthDate, mobileNumber, userName, accessCode, accessLevel, organizationName)):
                QMessageBox.critical(self, 'Invalid', f"Please fill the field with missing entry.")
                return

            if selectedOrganization == None:
                QMessageBox.critical(self, 'Invalid', f"{organizationName} not found")
                return
                
            existingData = session.query(User)
            existingData = existingData.filter(
                (User.FullName == fullName) |
                (User.UserName == userName)
            ).first()

            if existingData:
                if existingData.FullName == fullName:
                    QMessageBox.critical(self, 'Invalid', "Full name already exists")
                    session.rollback()
                    return
      
                if existingData.UserName == userName:
                    QMessageBox.critical(self, 'Invalid', "Username already exists")
                    session.rollback()
                    return

            else:
                user = User()
                user.FullName = fullName
                user.BirthDate = birthDate
                user.MobileNumber = mobileNumber
                user.UserName = userName
                user.AccessCode = accessCode
                user.AccessLevel = accessLevel
                user.OrganizationId = selectedOrganization.OrganizationId
                
                session.add(user)
                session.commit()
                
                QMessageBox.information(self, 'Success', "User succussfully created.")
                self.windowEvent = 'START_LOGIN'
                self.close()

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