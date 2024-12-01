import os, sys, logging

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.EditCurrentUser_ui import Ui_DialogEditCurrentUser
from app.views.components.Loading import Loading
from app.controllers.dedicated.edit import EditThread

class EditCurrentUser(Ui_DialogEditCurrentUser, QDialog):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.userData = authData['user']
        self.organizationData = authData['organization']
        self.currentThread = None
        self.activeThreads = []
        
        self.comboBoxOrganizationName.setCurrentText(f"{self.organizationData['organizationName']}")
        self.lineEditUserName.setText(f"{self.userData['userName']}")
        self.lineEditPassword.setText(f"{self.userData['password']}")
        self.lineEditFullName.setText(f"{self.userData['fullName']}")
        self.dateEditBirthDate.setDate(QDate.fromString(f"{self.userData['birthDate']}", 'yyyy-MM-dd'))
        self.lineEditMobileNumber.setText(f"{self.userData['mobileNumber']}")
        self.comboBoxAccessLevel.setCurrentText(f"{self.userData['accessLevel']}")

        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonSave.clicked.connect(self._onPushButtonSaveClicked)

    def _onPushButtonCancelClicked(self):
        self.close()
        
    def _onPushButtonSaveClicked(self):
        self.loading.show()
        self.currentThread = EditThread('editUserDataById', {
            'id': self.userData['id'],
            'userName': self.lineEditUserName.text(),
            'password': self.lineEditPassword.text(),
            'fullName': self.lineEditFullName.text().upper(),
            'birthDate': self.dateEditBirthDate.text(),
            'mobileNumber': self.lineEditMobileNumber.text(),
            'accessLevel': self.comboBoxAccessLevel.currentText(),
        })
        
        self.currentThread.finished.connect(self._handleOnPushButtonSaveClickedFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonSaveClickedFinished(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Success', f"{result['message']}")
        self.windowEvent = EVENT_START_LOGIN
        self.close()
        return
        
    def _cleanupThread(self):
        sender = self.sender()
        if sender in self.activeThreads:
            self.activeThreads.remove(sender)
        self.currentThread = None
        print('active threads:', self.activeThreads)

    def closeEvent(self, event):
        for thread in self.activeThreads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        
        self.activeThreads.clear()
        
        event.accept() # for closing the window
        
        print('closed...')
