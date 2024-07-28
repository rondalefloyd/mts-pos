# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.SignUp_ui import Ui_DialogSignUp
from app.views.components.Loading import Loading
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.fetch import FetchThread

# class definition
class SignUp(Ui_DialogSignUp, QDialog):
    # initialization method (__init__)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = None
        self.currentThread = None
        self.activeThreads = []
        
        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self._onPushButtonCreateClicked)
        self._populateComboBoxOrganizationName()
    
    # private methods
    def _populateComboBoxOrganizationName(self):
        self.fetchThread = FetchThread('pos/fetch/organization/all')
        self.fetchThread.finished.connect(self._handlePopulateComboBoxOrganizationNameResult)
        self.fetchThread.start()
        
    def _handlePopulateComboBoxOrganizationNameResult(self, result):
        for data in result['data']:
            self.comboBoxOrganizationName.addItem(f"{data['organizationName']}")
            
            
    def _onPushButtonCancelClicked(self):
        self.windowEvent = 'start/login'
        self.close()
    
    
    def _onPushButtonCreateClicked(self):
        self.currentThread = RegisterThread('pos/register/user', {
            'organizationName': f"{self.comboBoxOrganizationName.currentText()}".upper(),
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
            'fullName': f"{self.lineEditFullName.text()}".upper(),
            'birthDate': f"{self.dateEditBirthDate.text()}",
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessLevel': f"{self.comboBoxAccessLevel.currentText()}",
        })
        self.currentThread.finished.connect(self._handleOnPushButtonCreateClickedResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handleOnPushButtonCreateClickedResult(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Success', f"{result['message']}")
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
        
        # Set the window event state to 'start/login'
        self.windowEvent = 'start/login'
        
        event.accept()
        
        print('closed...')