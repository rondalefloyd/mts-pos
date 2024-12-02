import os, sys, logging

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.VoidItemSold_ui import Ui_DialogVoidItemSold
from app.views.components.Loading import Loading
from app.utils.helpers.validator import *
from app.utils.helpers.formatter import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.void import VoidThread

class VoidItemSold(Ui_DialogVoidItemSold, QDialog):
    def __init__(self, authData, selectedData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.selectedData = selectedData
        self.currentThread = None
        self.activeThreads = []
        
        self.pushButtonCancel.clicked.connect(self._onPushButtonCancelClicked)
        self.pushButtonVoid.clicked.connect(self._onPushButtonVoidClicked) 

    def _onPushButtonCancelClicked(self):
        self.close()
        
    def _onPushButtonVoidClicked(self):
        confirm = QMessageBox.warning(self, 'Confirm', f"Void {self.selectedData['itemName']} in this order?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.loading.show()
            self.currentThread = VoidThread('voidItemSoldDataById', {
                'id': self.selectedData['id'],
                'itemId': self.selectedData['itemId'],
                'stockBypass': self.selectedData['stockBypass'],
                'quantity': self.selectedData['quantity'],
                'reasonName': f"{self.comboBoxVoidReason.currentText()}",
            })
            self.currentThread.finished.connect(self._handleOnPushButtonVoidClickedFinished)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.finished.connect(self.loading.close)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonVoidClickedFinished(self, result):
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

    def closeEvent(self, event):
        for thread in self.activeThreads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        
        self.activeThreads.clear()
        
        event.accept() # for closing the window
        
        print('closed...')
