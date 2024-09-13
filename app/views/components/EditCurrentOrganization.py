import os, sys, logging
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.global_variables import *
from app.views.templates.EditCurrentOrganization_ui import Ui_DialogEditCurrentOrganization
from app.views.components.Loading import Loading
from app.views.validator import *
from app.controllers.dedicated.edit import EditThread

class EditCurrentOrganization(Ui_DialogEditCurrentOrganization, QDialog):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.organizationData = authData['organization']
        self.currentThread = None
        self.activeThreads = []
        
        self.lineEditOrganizationName.setValidator(withSpaceTextDigitFormatValidator())
        self.lineEditAddress.setValidator(addressFormatValidator())
        self.lineEditMobileNumber.setValidator(mobileNumberValidator())

        self.lineEditTaxId.setText(f"{self.organizationData['taxId']}")
        self.lineEditOrganizationName.setText(f"{self.organizationData['organizationName']}")
        self.lineEditAddress.setText(f"{self.organizationData['address']}")
        self.lineEditMobileNumber.setText(f"{self.organizationData['mobileNumber']}")
        self.lineEditAccessCode.setText(f"{self.organizationData['accessCode']}")

        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonSave.clicked.connect(self._onPushButtonSaveClicked)

    def _onPushButtonCancelClicked(self):
        self.close()
        
    def _onPushButtonSaveClicked(self):
        self.loading.show()
        self.currentThread = EditThread('editOrganizationDataById', {
            'id': self.organizationData['id'],
            'taxId': self.lineEditTaxId.text(),
            'organizationName': self.lineEditOrganizationName.text(),
            'address': self.lineEditAddress.text().upper(),
            'mobileNumber': self.lineEditMobileNumber.text(),
            'accessCode': self.lineEditAccessCode.text(),
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
