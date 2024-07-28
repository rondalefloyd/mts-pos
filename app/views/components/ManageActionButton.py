
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.ManageActionButton_ui import Ui_FormManageActionButton

class ManageActionButton(Ui_FormManageActionButton, QWidget):
    def __init__(self, add=False, delete=False, discount=False, edit=False, view=False):
        super().__init__()
        self.setupUi(self)
        
        self.pushButtonAdd.setVisible(add)
        self.pushButtonDelete.setVisible(delete)
        self.pushButtonDiscount.setVisible(discount)
        self.pushButtonEdit.setVisible(edit)
        self.pushButtonView.setVisible(view)
        
        self.setWindowFlags(Qt.FramelessWindowHint)