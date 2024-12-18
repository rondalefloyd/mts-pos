# import
import os, sys

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.Setup_ui import Ui_DialogSetup
from app.views.components.Loading import Loading
from app.utils.helpers.formatter import *
from app.controllers.dedicated.register import RegisterThread

# class definition
class Setup(Ui_DialogSetup, QDialog):
    # initialization method (__init__)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = None
        self.currentThread = None
        self.activeThreads = []

        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonCreate.clicked.connect(self._onPushButtonCreateClicked)
        
    # private methods
    def _onPushButtonCancelClicked(self):
        self.windowEvent = EVENT_START_LOGIN
        self.close()


    def _onPushButtonCreateClicked(self):
        self.loading.show()
        self.currentThread = RegisterThread('registerOrganization', {
            'taxId': self.lineEditTaxId.text().upper(),
            'organizationName': self.lineEditOrganizationName.text(),
            'address': self.lineEditAddress.text().upper(),
            'mobileNumber': self.lineEditMobileNumber.text(),
            'password': self.lineEditPassword.text(),
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