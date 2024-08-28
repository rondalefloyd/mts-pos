
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.config import *
from app.views.templates.LoadData_ui import Ui_DialogLoadData
from app.views.components.Loading import Loading

class LoadData(Ui_DialogLoadData, QDialog):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.window_event = EVENT_NO_EVENT
        self.authData = authData
        self.currentThread = None
        self.activeThreads = []

