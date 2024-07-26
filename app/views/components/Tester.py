
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.Tester_ui import Ui_Dialog
from app.controllers.Authenticate import Authenticate

class Tester(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButtonTest.clicked.connect(self.onPushButtonTestClicked)
        
    def onPushButtonTestClicked(self):
        self.authenticate = Authenticate('pos/authenticate/user/password')
        self.authenticate.finished.connect(self.handleOnPushButtonTestClickedResult)
        self.authenticate.start()
        pass
    
    def handleOnPushButtonTestClickedResult(self, result):
        print('--result:', result)
    
    def closeEvent(self):
        print('closed...')
        pass