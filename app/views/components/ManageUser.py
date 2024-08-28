# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.config import *
from app.views.templates.ManageUser_ui import Ui_FormManageUser
from app.views.components.Loading import Loading
from app.views.components.ManageActionButton import ManageActionButton
from app.views.validator import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

class ManageUser(Ui_FormManageUser, QWidget):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        self.windowEvent = EVENT_NO_EVENT