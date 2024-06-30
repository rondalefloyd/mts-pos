import os, sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit
from PyQt5.QtCore import QEvent
from sqlalchemy.sql import func
from machineid import id

sys.path.append(os.path.abspath(''))
from app.ui.dialogs.login_ui import Ui_DialogLogin
from app.models.system import session
from app.models.association import User, Organization, Configuration

class Login(Ui_DialogLogin, QDialog):
    def __init__(self):
        super().__init__()
        self.windowEvent = 'NO_EVENT'
        self.setupUi(self)

        self.userId = None

        self.pushButtonAccessCodeVisibility.setText('Show')

        self.pushButtonAccessCodeVisibility.clicked.connect(self.onPushButtonVisibilityIndicator)
        self.pushButtonSignUp.clicked.connect(self.onPushButtonSignUpClicked)
        self.pushButtonLogin.clicked.connect(self.onPushButtonLoginClicked)
        
        self.populateLoginField()
        pass
        
    def populateLoginField(self):
        try:
            existingConfiguration = session.query(Configuration)
            existingConfiguration = existingConfiguration.filter(
                (Configuration.MachineId == f"{id()}") &
                (Configuration.IsRememberUser == "True")
            )
            existingConfiguration = existingConfiguration.order_by(Configuration.UpdateTs.desc()).first()
            
            if existingConfiguration:
                if existingConfiguration.IsRememberUser == "True":
                    self.lineEditUserName.setText(f"{existingConfiguration.LastLoginUserName}")
                    self.lineEditAccessCode.setText(f"{existingConfiguration.LastLoginAccessCode}")
                    self.checkBoxRememberMe.setChecked(True)
                else:
                    self.checkBoxRememberMe.setChecked(False)

        except Exception as error:
            session.rollback()
            QMessageBox.critical(self, 'Error', f"Error: {error}")
            print('error at populateLineEditUserNamLineEditAccessCode:', error)

        finally:
            session.close()
            print('session closed')

    def onPushButtonVisibilityIndicator(self):
        accessCodeVisibility = self.pushButtonAccessCodeVisibility.isChecked()
        
        self.lineEditAccessCode.setEchoMode(QLineEdit.Normal if accessCodeVisibility else QLineEdit.Password)
        self.pushButtonAccessCodeVisibility.setText('Hide' if accessCodeVisibility else 'Show')

    def onPushButtonSignUpClicked(self):
        self.windowEvent = 'START_SIGNUP'
        self.close()

    def onPushButtonLoginClicked(self):
        try:
            userName = f"{self.lineEditUserName.text()}"
            accessCode = f"{self.lineEditAccessCode.text()}"
            machineId = f"{id()}"
            isRememberMe = f"{self.checkBoxRememberMe.isChecked()}"
            
            exstingUser = session.query(User).filter(
                (User.UserName == userName) & 
                (User.AccessCode == accessCode)
            ).first()
            
            if exstingUser:                    
                self.close()
                self.windowEvent = 'START_MANAGE'
                self.userId = exstingUser.UserId

            else:
                QMessageBox.critical(self, 'Invalid', "User not found")
                return
                
                
            # TODO: fix by addimg function for lneeditusername and accesscode to check the remember me when it matches the credentials in the database
            existingConfiguration = session.query(Configuration)
            existingConfiguration = existingConfiguration.filter(
                (Configuration.MachineId == machineId) &
                (Configuration.LastLoginUserName == userName)
            ).first()

            if existingConfiguration:
                existingConfiguration.IsRememberUser = isRememberMe
                existingConfiguration.UpdateTs = func.now()
                session.commit()
                        
            if not existingConfiguration and isRememberMe == "True":
                configuration = Configuration()
                
                configuration.MachineId = machineId
                configuration.LastLoginUserName = userName
                configuration.LastLoginAccessCode = accessCode
                configuration.IsRememberUser = isRememberMe

                session.add(configuration)
                session.commit()
                
        except Exception as error:
            session.rollback()
            QMessageBox.critical(self, 'Error', f"Error: {error}")
            print('error at onPushButtonLoginClicked:', error)

        finally:
            session.close()
            print('session closed')
            

    def closeEvent(self, event:QEvent):
        event.accept()
        pass