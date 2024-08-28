import os
import sys
import logging
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManageReceipt_ui import Ui_FormManageReceipt
from app.views.components.Loading import Loading
from app.views.components.ManageActionButton import ManageActionButton
from app.views.components.ViewReceipt import ViewReceipt
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

class ManageReceipt(Ui_FormManageReceipt, QWidget):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        self.windowEvent = EVENT_NO_EVENT
        