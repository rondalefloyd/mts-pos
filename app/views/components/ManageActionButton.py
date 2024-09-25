
import os, sys

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.views.templates.ManageActionButton_ui import Ui_FormManageActionButton

class ManageActionButton(Ui_FormManageActionButton, QWidget):
    def __init__(self, add=False, delete=False, discount=False, edit=False, view=False, void=False):
        super().__init__()
        self.setupUi(self)
        
        # self.pushButtonAdd.setText("")
        # self.pushButtonDelete.setText("")
        # self.pushButtonDiscount.setText("")
        # self.pushButtonEdit.setText("")
        # self.pushButtonView.setText("")
        # self.pushButtonVoid.setText("")
        
        self.pushButtonAdd.setVisible(add)
        self.pushButtonDelete.setVisible(delete)
        self.pushButtonDiscount.setVisible(discount)
        self.pushButtonEdit.setVisible(edit)
        self.pushButtonView.setVisible(view)
        self.pushButtonVoid.setVisible(void)
        
        self.setWindowFlags(Qt.FramelessWindowHint)