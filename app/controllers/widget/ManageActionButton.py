import os, sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QEvent

sys.path.append(os.path.abspath(''))
from app.ui.widget.ManageActionButton_ui import Ui_FormManageActionButton

class ManageActionButtonController(Ui_FormManageActionButton, QWidget):
    def __init__(self, add=False, delete=False, discount=False, edit=False, view=False):
        super().__init__()
        self.windowEvent = 'NO_EVENT'
        self.setupUi(self)
        # --
        self.pushButtonAdd.setVisible(add is True)
        self.pushButtonDelete.setVisible(delete is True)
        self.pushButtonDiscount.setVisible(discount is True)
        self.pushButtonEdit.setVisible(edit is True)
        self.pushButtonView.setVisible(view is True)
        

    def closeEvent(self, event:QEvent):
        event.accept()
        pass