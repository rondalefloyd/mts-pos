# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.config import *
from app.views.templates.SignUp_ui import Ui_DialogSignUp
from app.views.components.Loading import Loading
from app.views.validator import *
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.fetch import FetchThread

class SignUp(Ui_DialogSignUp, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.windowEvent = EVENT_NO_EVENT