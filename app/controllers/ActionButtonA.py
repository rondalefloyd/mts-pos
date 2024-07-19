import os, sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QLineEdit
from PyQt5.QtCore import Qt, QEvent
from machineid import id

sys.path.append(os.path.abspath(''))
from app.ui.ActionButtonA_ui import Ui_FormActionButtonA
from app.utils.dbops_helpers import GetDataThread

class ActionButtonAController(Ui_FormActionButtonA, QWidget):
    def __init__(self, allowAdd=False, allowDelete=False, allowDiscount=False, allowEdit=False, allowView=False):
        super().__init__()
        self.setupUi(self)
        self._setupInitialTask({
            'allowAdd': allowAdd,
            'allowDelete': allowDelete,
            'allowDiscount': allowDiscount,
            'allowEdit': allowEdit,
            'allowView': allowView,
        })
    
    def _setupInitialTask(self, option):
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.pushButtonAdd.setVisible(option['allowAdd'] is True)
        self.pushButtonDelete.setVisible(option['allowDelete'] is True)
        self.pushButtonDiscount.setVisible(option['allowDiscount'] is True)
        self.pushButtonEdit.setVisible(option['allowEdit'] is True)
        self.pushButtonView.setVisible(option['allowView'] is True)

    def closeEvent(self, event:QEvent):
        event.accept()
        pass