import os, sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QInputDialog, QLineEdit
from PyQt5.QtCore import QEvent

sys.path.append(os.path.abspath(''))
from app.ui.ManageUser_ui import Ui_FormMenuUser
from app.controllers.Loading import LoadingController
from app.utils.crud import CRUDThread

class ManageUserController(Ui_FormMenuUser, QWidget):
    def __init__(self, currentUserData):
        super().__init__()
        self.setupUi(self)
        
        self.windowEvent = 'NO_EVENT'
        self.currentUserData = currentUserData
        self.currentPage = 1
        self.totalPages = 1

    def closeEvent(self, event:QEvent):
        event.accept()
        pass