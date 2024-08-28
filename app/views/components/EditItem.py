import os, sys, logging
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.EditItem_ui import Ui_DialogEditItem
from app.views.components.Loading import Loading
from app.views.validator import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.remove import RemoveThread
from app.controllers.dedicated.edit import EditThread

class EditItem(Ui_DialogEditItem, QDialog):
    def __init__(self, authData, selectedData):
        super().__init__()
        self.setupUi(self)
        self.windowEvent = EVENT_NO_EVENT
        
