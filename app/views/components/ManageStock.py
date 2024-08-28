import os
import sys
import logging
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManageStock_ui import Ui_FormManageStock
from app.views.components.Loading import Loading
from app.views.components.EditStock import EditStock
from app.views.components.ManageActionButton import ManageActionButton
from app.controllers.dedicated.fetch import *
from app.controllers.dedicated.register import *
from app.controllers.dedicated.remove import *

class ManageStock(Ui_FormManageStock, QWidget):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        self.window_event = EVENT_NO_EVENT