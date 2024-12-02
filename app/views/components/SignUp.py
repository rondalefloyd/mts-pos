# import
import os, sys

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.SignUp_ui import Ui_DialogSignUp
from app.views.components.Loading import Loading
from app.utils.helpers.formatter import *
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.fetch import FetchThread

# class definition
class SignUp(Ui_DialogSignUp, QDialog):
    # initialization method (__init__)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = None
        self.currentThread = None
        self.activeThreads = []
        
        self._populateComboBoxOrganizationName()
        
        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self._onPushButtonCreateClicked)
    
    # private methods
    def _populateComboBoxOrganizationName(self):
        self.fetchThread = FetchThread('fetchAllOrganizationData')
        self.fetchThread.finished.connect(self._handlePopulateComboBoxOrganizationNameFinished)
        self.fetchThread.start()
        
    def _handlePopulateComboBoxOrganizationNameFinished(self, result):
        self.comboBoxOrganizationName.clear()
        for data in result['listData']:
            self.comboBoxOrganizationName.addItem(f"{data['organizationName']}")
            
    def _onPushButtonCancelClicked(self):
        self.windowEvent = EVENT_START_LOGIN
        self.close()
    
    
    def _onPushButtonCreateClicked(self):
        self.loading.show()
        self.currentThread = RegisterThread('registerUser', {
            'organizationName': self.comboBoxOrganizationName.currentText(),
            'userName': self.lineEditUserName.text(),
            'password': self.lineEditPassword.text(),
            'fullName': self.lineEditFullName.text().upper(),
            'birthDate': self.dateEditBirthDate.text(),
            'mobileNumber': self.lineEditMobileNumber.text(),
            'accessLevel': self.comboBoxAccessLevel.currentText(),
        })
        self.currentThread.finished.connect(self._handleOnPushButtonCreateClickedFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handleOnPushButtonCreateClickedFinished(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Information', f"{result['message']}")
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
        
        # Set the window event state to EVENT_START_LOGIN
        self.windowEvent = EVENT_START_LOGIN
        
        event.accept() # for closing the window
        
        print('closed...')