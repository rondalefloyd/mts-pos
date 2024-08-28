# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.config import *
from app.views.templates.Login_ui import Ui_DialogLogin
from app.views.components.Loading import Loading
from app.views.validator import nonSpaceTextFormatValidator
from app.controllers.dedicated.authenticate import AuthenticateThread

class Login(Ui_DialogLogin, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.windowEvent = EVENT_NO_EVENT
        