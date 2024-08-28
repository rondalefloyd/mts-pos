import os
import sys
import logging
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManagePromo_ui import Ui_FormManagePromo
from app.views.components.Loading import Loading
from app.views.components.EditPromo import EditPromo
from app.views.components.ManageActionButton import ManageActionButton
from app.views.validator import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

class ManagePromo(Ui_FormManagePromo, QWidget):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        self.windowEvent = EVENT_NO_EVENT
        