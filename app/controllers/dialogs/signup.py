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
        self.pushButtonCreate.clicked.connect(self.onPushButtonCreate)
        pass

        self.populateComboBoxOrganizationName()

    def populateComboBoxOrganizationName(self):
        self.comboBoxOrganizationName.addItems([organizationName[0] for organizationName in session.query(Organization.OrganizationName).all()])

    def onPushButtonCancelClicked(self):
        self.windowEvent = 'START_LOGIN'
        self.close()

    def onPushButtonCreate(self):
        try:
            fullName = f"{self.lineEditFullName.text()}".upper()
            birthDate = f"{self.dateEditBirthDate.text()}"
            mobileNumber = f"{self.lineEditMobileNumber.text()}"
            userName = f"{self.lineEditUserName.text()}"
            accessCode = f"{self.lineEditAccessCode.text()}"
            accessLevel = f"{self.comboBoxAccessLevel.currentText()}"
            organizationName = f"{self.comboBoxOrganizationName.currentText()}"
            organizationId = session.query(Organization.OrganizationId).filter(Organization.OrganizationName == organizationName).first()

            if any(entry == "" for entry in (fullName, birthDate, mobileNumber, userName, accessCode, accessLevel, organizationName)):
                QMessageBox.critical(self, 'Invalid', f"Please fill the field with missing entry.")
                return

            if organizationId == None:
                QMessageBox.critical(self, 'Invalid', f"{organizationName} not found")
                return
                
            existingData = session.query(User)
            existingData = existingData.filter(
                (User.FullName == fullName) | 
                (User.MobileNumber == mobileNumber) |
                (User.UserName == userName)
            ).first()

            if existingData:
                if existingData.FullName == fullName:
                    QMessageBox.critical(self, 'Invalid', "Full name already exists")
                    session.rollback()
                    
                if existingData.MobileNumber == mobileNumber:
                    QMessageBox.critical(self, 'Invalid', "Mobile number already exists")
                    session.rollback()
                    
                if existingData.UserName == userName:
                    QMessageBox.critical(self, 'Invalid', "Username already exists")
                    session.rollback()
                    
            else:
                user = User()
                user.FullName = fullName
                user.BirthDate = birthDate
                user.MobileNumber = mobileNumber
                user.UserName = userName
                user.AccessCode = accessCode
                user.AccessLevel = accessLevel
                user.OrganizationId = organizationId
                
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