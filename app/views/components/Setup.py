
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

        self.pushButtonCancel.clicked.connect(self.onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self.onPushButtonCreateClicked)
        
    def onPushButtonCancelClicked(self):
        self.close()
        pass

    def onPushButtonCreateClicked(self):
        self.loading.show()
        self.registerThread = RegisterThread('pos/register/organization', {
            'taxId': f"{self.lineEditTaxId.text()}".upper(),
            'organizationName': f"{self.lineEditOrganizationName.text()}".upper(),
            'address': f"{self.lineEditAddress.text()}".upper(),
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
        })
        self.registerThread.finished.connect(self.handleOnPushButtonCreateClickedResult)
        self.registerThread.start()
        
    def handleOnPushButtonCreateClickedResult(self, result):
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