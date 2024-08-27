
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.LoadData_ui import Ui_DialogLoadData

class LoadData(Ui_DialogLoadData, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        