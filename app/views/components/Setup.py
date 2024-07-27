# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.Setup_ui import Ui_DialogSetup
from app.views.components.Loading import Loading
from app.controllers.dedicated.register import RegisterThread

# class definition
class Setup(Ui_DialogSetup, QDialog):
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
        
    # private methods
    def _onPushButtonCancelClicked(self):
        self.windowEvent = 'start/login'
        self.close()


    def _onPushButtonCreateClicked(self):
        self.loading.show()
        self.currentThread = RegisterThread('pos/register/organization', {
            'taxId': f"{self.lineEditTaxId.text()}".upper(),
            'organizationName': f"{self.lineEditOrganizationName.text()}".upper(),
            'address': f"{self.lineEditAddress.text()}".upper(),
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
        })
        self.currentThread.finished.connect(self._handleOnPushButtonCreateClickedResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonCreateClickedResult(self, result):
        self.loading.close()
        
        if result['success'] is False:
            QMessageBox.critical(self, 'Invalid', f"{result['message']}")
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