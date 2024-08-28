# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.config import *
from app.views.templates.Setup_ui import Ui_DialogSetup
from app.views.components.Loading import Loading
from app.views.validator import *
from app.controllers.dedicated.register import RegisterThread

class Setup(Ui_DialogSetup, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.windowEvent = EVENT_NO_EVENT