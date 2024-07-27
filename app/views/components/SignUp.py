
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.SignUp_ui import Ui_DialogSignUp
from app.views.components.Loading import Loading
from app.controllers.register import RegisterThread
from app.controllers.fetch import FetchThread

class SignUp(Ui_DialogSignUp, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = None
        
        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self._onPushButtonCreateClicked)
        self._populateComboBoxOrganizationName()
    
    def _populateComboBoxOrganizationName(self):
        self.loading.show()
        self.fetchThread = FetchThread('pos/fetch/organization/all')
        self.fetchThread.finished.connect(self._handlePopulateComboBoxOrganizationNameResult)
        self.fetchThread.start()
        
    def _handlePopulateComboBoxOrganizationNameResult(self, result):
        self.loading.close()
        
        for data in result['data']:
            self.comboBoxOrganizationName.addItem(f"{data['organizationName']}")
            
    def _onPushButtonCancelClicked(self):
        self.windowEvent = 'start/login'
        self.close()
    
    def _onPushButtonCreateClicked(self):
        self.loading.show()
        self.registerThread = RegisterThread('pos/register/user', {
            'organizationName': f"{self.comboBoxOrganizationName.currentText()}".upper(),
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
            'fullName': f"{self.lineEditFullName.text()}".upper(),
            'birthDate': f"{self.dateEditBirthDate.text()}",
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessLevel': f"{self.comboBoxAccessLevel.currentText()}",
        })
        self.registerThread.finished.connect(self._handleOnPushButtonCreateClickedResult)
        self.registerThread.start()
        
    def _handleOnPushButtonCreateClickedResult(self, result):
        self.loading.close()
        
        if result['success'] is False:
            QMessageBox.critical(self, 'Invalid', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Success', f"{result['message']}")
        self.close()
        return
        
    def closeEvent(self, event):
        event.accept()
        self.windowEvent = 'start/login'
        print('closed...')