# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.global_variables import *
from app.views.templates.EditUser_ui import Ui_DialogEditUser
from app.views.components.Loading import Loading
from app.views.components.ManageActionButton import ManageActionButton
from app.views.validator import *
from app.controllers.dedicated.edit import EditThread

# class definition
class EditUser(Ui_DialogEditUser, QDialog):
    # initialization method (__init__)
    def __init__(self, authData, selectedData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.organizationData = authData['organization']
        self.selectedData = selectedData
        self.currentThread = None
        self.activeThreads = []
        
        self.comboBoxOrganizationName.setCurrentText(f"{self.organizationData['organizationName']}")
        self.lineEditUserName.setText(f"{self.selectedData['userName']}")
        self.lineEditAccessCode.setText(f"{self.selectedData['accessCode']}")
        self.lineEditFullName.setText(f"{self.selectedData['fullName']}")
        self.dateEditBirthDate.setDate(QDate.fromString(f"{self.selectedData['birthDate']}", 'yyyy-MM-dd'))
        self.lineEditMobileNumber.setText(f"{self.selectedData['mobileNumber']}")
        self.comboBoxAccessLevel.setCurrentText(f"{self.selectedData['accessLevel']}")

        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonSave.clicked.connect(self._onPushButtonSaveClicked)

    # private methods
    def _onPushButtonCancelClicked(self):
        self.close()
        
    def _onPushButtonSaveClicked(self):
        self.loading.show()
        self.currentThread = EditThread('editUserDataById', {
            'id': self.selectedData['id'],
            'userName': self.lineEditUserName.text(),
            'accessCode': self.lineEditAccessCode.text(),
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

    # overridden methods
    def closeEvent(self, event):
        for thread in self.activeThreads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        
        self.activeThreads.clear()
        
        event.accept() # for closing the window
        
        print('closed...')