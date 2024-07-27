
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.Setup_ui import Ui_DialogSetup
from app.views.components.Loading import Loading
from app.controllers.register import RegisterThread

class Setup(Ui_DialogSetup, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = None

        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self._onPushButtonCreateClicked)
        
    def _onPushButtonCancelClicked(self):
        self.windowEvent = 'start/login'
        self.close()
        pass

    def _onPushButtonCreateClicked(self):
        self.loading.show()
        self.registerThread = RegisterThread('pos/register/organization', {
            'taxId': f"{self.lineEditTaxId.text()}".upper(),
            'organizationName': f"{self.lineEditOrganizationName.text()}".upper(),
            'address': f"{self.lineEditAddress.text()}".upper(),
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
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