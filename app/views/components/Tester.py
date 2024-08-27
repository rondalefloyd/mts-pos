
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.config import *
from app.views.templates.Tester_ui import Ui_Dialog
from app.controllers.dedicated.authenticate import AuthenticateThread

class Tester(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButtonTest.clicked.connect(self._onPushButtonTestClicked)
        
    def _onPushButtonTestClicked(self):
        self.authenticate = AuthenticateThread('authenticate_user_by_user_name_access_code')
        self.authenticate.finished.connect(self._handleOnPushButtonTestClickedFinished)
        self.authenticate.start()
        pass
    
    def _handleOnPushButtonTestClickedFinished(self, result):
        print('--result:', result)
    
    def closeEvent(self):
        print('closed...')
        pass