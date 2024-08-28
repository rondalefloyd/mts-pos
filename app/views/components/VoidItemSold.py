import os, sys, logging
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.VoidItemSold_ui import Ui_DialogVoidItemSold
from app.views.components.Loading import Loading
from app.views.validator import *
from app.controllers.dedicated.fetch import *
from app.controllers.dedicated.void import *

class VoidItemSold(Ui_DialogVoidItemSold, QDialog):
    def __init__(self, authData, selectedData):
        super().__init__()
        self.setupUi(self)
        self.window_event = EVENT_NO_EVENT

