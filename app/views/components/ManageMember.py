# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.config import *
from app.views.templates.ManageMember_ui import Ui_FormManageMember
from app.views.components.Loading import Loading
from app.views.components.EditMember import EditMember
from app.views.components.ManageActionButton import ManageActionButton
from app.views.validator import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

# class definition
class ManageMember(Ui_FormManageMember, QWidget):
    # initialization method (__init__)
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        self.windowEvent = EVENT_NO_EVENT
        