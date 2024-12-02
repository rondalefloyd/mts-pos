import os, sys

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.EditMember_ui import Ui_DialogEditMember
from app.views.components.Loading import Loading
from app.utils.helpers.validator import *
from app.utils.helpers.formatter import *
from app.views.components.ManageActionButton import ManageActionButton
from app.controllers.dedicated.edit import EditThread

# class definition
class EditMember(Ui_DialogEditMember, QDialog):
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

        self.lineEditMemberName.setText(f"{self.selectedData['memberName']}")
        self.dateEditBirthDate.setDate(QDate.fromString(f"{self.selectedData['birthDate']}", 'yyyy-MM-dd'))
        self.lineEditAddress.setText(f"{self.selectedData['address']}")
        self.lineEditMobileNumber.setText(f"{self.selectedData['mobileNumber']}")
        self.lineEditPoints.setText(f"{self.selectedData['points']}")

        self.lineEditPoints.setValidator(floatFormatValidator())
        self.lineEditMobileNumber.setValidator(mobileNumberValidator())

        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonSave.clicked.connect(self._onPushButtonSaveClicked)

    # private methods
    def _onPushButtonCancelClicked(self):
        self.close()
        
    def _onPushButtonSaveClicked(self):
        self.loading.show()
        self.currentThread = EditThread('editMemberDataById', {
            'id': self.selectedData['id'],
            'memberName': self.lineEditMemberName.text().upper(),
            'birthDate': self.dateEditBirthDate.text(),
            'address': self.lineEditAddress.text().upper(),
            'mobileNumber': self.lineEditMobileNumber.text(),
            'points': self.lineEditPoints.text(),
        })
        self.currentThread.finished.connect(self._handleOnPushButtonAddClickedFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonAddClickedFinished(self, result):
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
        
        event.accept() # for closing the window
        
        print('closed...')