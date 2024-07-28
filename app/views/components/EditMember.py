# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.EditMember_ui import Ui_DialogEditMember
from app.views.components.Loading import Loading
from app.views.components.ManageActionButton import ManageActionButton
from app.controllers.dedicated.edit import EditThread

# class definition
class EditMember(Ui_DialogEditMember, QDialog):
    # initialization method (__init__)
    def __init__(self, userData, selectedData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = userData
        self.selectedData = selectedData
        self.currentThread = None
        self.activeThreads = []
        
        self.comboBoxOrganizationName.setCurrentText(f"{self.userData['organizationName']}")

        self.lineEditMemberName.setText(f"{self.selectedData['memberName']}")
        self.dateEditBirthDate.setDate(QDate.fromString(f"{self.selectedData['birthDate']}", 'yyyy-MM-dd'))
        self.lineEditAddress.setText(f"{self.selectedData['address']}")
        self.lineEditMobileNumber.setText(f"{self.selectedData['mobileNumber']}")
        self.lineEditPoints.setText(f"{self.selectedData['points']}")

        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonSave.clicked.connect(self._onPushButtonSaveClicked)

    # private methods
    def _onPushButtonCancelClicked(self):
        self.close()
        
    def _onPushButtonSaveClicked(self):
        self.currentThread = EditThread('pos/edit/member', {
            'id': f"{self.selectedData['id']}",
            'memberName': f"{self.lineEditMemberName.text()}".upper(),
            'birthDate': f"{self.dateEditBirthDate.text()}",
            'address': f"{self.lineEditAddress.text()}".upper(),
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'points': f"{self.lineEditPoints.text()}",  # Assuming new members start with 0 points
        })
        self.currentThread.finished.connect(self._handleOnPushButtonAddClickedResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonAddClickedResult(self, result):
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
        
        event.accept()
        
        print('closed...')