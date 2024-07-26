
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.Manage_ui import Ui_MainWindowManage
from app.views.components.Loading import Loading
from app.controllers.register import RegisterThread

class Manage(Ui_MainWindowManage, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = None
        
    def closeEvent(self, event):
        event.accept()
        self.windowEvent = 'start/login'
        print('closed...')