import os, sys, logging, csv
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManageItem_ui import Ui_FormManageItem
from app.views.components.Loading import Loading
from app.views.components.LoadData import LoadData
from app.views.components.EditItem import EditItem
from app.views.components.ManageActionButton import ManageActionButton
from app.views.validator import *
from app.controllers.dedicated.fetch import *
from app.controllers.dedicated.register import *
from app.controllers.dedicated.load import *
from app.controllers.dedicated.remove import *

class ManageItem(Ui_FormManageItem, QWidget):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        self.window_event = EVENT_NO_EVENT
        