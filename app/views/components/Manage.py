# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.Manage_ui import Ui_MainWindowManage
from app.views.components.Loading import Loading
from app.views.components.ManageUser import ManageUser
from app.views.components.ManageMember import ManageMember
from app.views.components.ManagePromo import ManagePromo
from app.views.components.ManageReward import ManageReward
from app.views.components.ManageItem import ManageItem
from app.views.components.ManageStock import ManageStock
from app.views.components.ManageSales import ManageSales
from app.views.components.ManageReceipt import ManageReceipt
from app.controllers.dedicated.authenticate import *

class Manage(Ui_MainWindowManage, QMainWindow):
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        self.window_event = EVENT_NO_EVENT
        