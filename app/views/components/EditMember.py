# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.config import *
from app.views.templates.EditMember_ui import Ui_DialogEditMember
from app.views.components.Loading import Loading
from app.views.components.ManageActionButton import ManageActionButton
from app.views.validator import *
from app.controllers.dedicated.edit import EditThread

class EditMember(Ui_DialogEditMember, QDialog):
    def __init__(self, authData, selectedData):
        super().__init__()
        self.setupUi(self)
        self.windowEvent = EVENT_NO_EVENT
        