import os, sys, logging
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.EditPromo_ui import Ui_DialogEditPromo
from app.views.components.Loading import Loading
from app.views.validator import *
from app.controllers.dedicated.edit import EditThread

class EditPromo(Ui_DialogEditPromo, QDialog):
    def __init__(self, authData, selectedData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.selectedData = selectedData
        self.currentThread = None
        self.activeThreads = []
        
        self.lineEditPromoName.setValidator(withSpaceTextDigitFormatValidator())
        self.lineEditDiscountRate.setValidator(billFormatValidator())
        
        self.lineEditPromoName.setText(f"{self.selectedData['promoName']}")
        self.lineEditDiscountRate.setText(f"{self.selectedData['discountRate']}")
        self.lineEditDescription.setText(f"{self.selectedData['description']}")

        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonSave.clicked.connect(self._onPushButtonSaveClicked)

    def _onPushButtonCancelClicked(self):
        self.close()
        
    def _onPushButtonSaveClicked(self):
        self.currentThread = EditThread('edit_promo_data_by_id', {
            'id': self.selectedData['id'],
            'promoName': self.lineEditPromoName.text().upper(),
            'discountRate': self.lineEditDiscountRate.text(),
            'description': self.lineEditDescription.text().upper(),
        })
        self.currentThread.finished.connect(self._handleOnPushButtonSaveClickedResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonSaveClickedResult(self, result):
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

    def closeEvent(self, event):
        for thread in self.activeThreads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        
        self.activeThreads.clear()
        
        event.accept() # for closing the window
        
        print('closed...')
