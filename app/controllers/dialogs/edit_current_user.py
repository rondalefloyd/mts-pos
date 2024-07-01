import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QDateEdit
from PyQt5.QtCore import QEventLoop, QDate
from sqlalchemy.sql import exists

sys.path.append(os.path.abspath(''))
from app.ui.dialogs.edit_current_user_ui import Ui_DialogEditCurrentUser
from app.models.system import session
from app.models.association import User, Organization, Configuration

class EditCurrentUser(Ui_DialogEditCurrentUser, QDialog):
    def __init__(self, userId):
        super().__init__()
        self.windowEvent = 'NO_EVENT'
        self.setupUi(self)

        self.userId = userId

        self.pushButtonCancel.clicked.connect(self.onPushButtonCancelClicked)
        self.pushButtonSave.clicked.connect(self.onPushButtonSaveClicked)
        pass

        self.populateEditField()

    def populateEditField(self):
        try:           
            currentUser = session.query(User)
            currentUser = currentUser.filter(User.UserId == self.userId).first()
                        
            self.lineEditFullName.setText(f"{currentUser.FullName}")
            self.dateEditBirthDate.setDate(QDate.fromString(currentUser.BirthDate, 'yyyy-MM-dd'))
            self.lineEditUserName.setText(f"{currentUser.UserName}")
            self.lineEditAccessCode.setText(f"{currentUser.AccessCode}")
            self.lineEditMobileNumber.setText(f"{currentUser.MobileNumber}")
            
        except Exception as error:
            session.rollback()
            print('error at setStatusBar:', error)

        finally:
            session.close()
            print('session closed')
        pass
    
    def onPushButtonCancelClicked(self):
        self.close()

    def onPushButtonSaveClicked(self):
        try:
            fullName = f"{self.lineEditFullName.text()}".upper()
            birthDate = f"{self.dateEditBirthDate.text()}"
            mobileNumber = f"{self.lineEditMobileNumber.text()}"
            userName = f"{self.lineEditUserName.text()}"
            accessCode = f"{self.lineEditAccessCode.text()}"
            
            if any(entry == "" for entry in (fullName, birthDate, mobileNumber, userName, accessCode)):
                QMessageBox.critical(self, 'Invalid', f"Please fill the field with missing entry.")
                return
            
            # TODO: fix checker where it should not be able to update the data if it's already existing
            existingUser = session.query(User)
            existingUser = existingUser.filter(
                (User.UserName == userName) &
                (User.FullName == fullName) &
                (User.MobileNumber == mobileNumber) &
                (User.UserName == userName) &
                (User.AccessCode == accessCode)
            ).first()
            
            if existingUser:
                QMessageBox.critical(self, 'Invalid', "Cannot use the same information.")
                session.rollback()
                return
        
            currentUser = session.query(User)
            currentUser = currentUser.filter(User.UserId == self.userId).first()    

            if existingUser and not currentUser:
                pass
        
            
            if currentUser:
                currentUser.FullName = fullName
                currentUser.BirthDate = birthDate
                currentUser.MobileNumber = mobileNumber
                currentUser.UserName = userName
                currentUser.AccessCode = accessCode

                session.commit()
                
                QMessageBox.information(self, 'Success', "User succussfully edited.")
                self.close()

        except Exception as error:
            session.rollback()
            QMessageBox.critical(self, 'Error', f"Error: {error}")
            print('error at onPushButtonSaveClicked:', error)

        finally:
            session.close()
            print('session closed')
        pass

    def closeEvent(self, event):
        event.accept()
        pass