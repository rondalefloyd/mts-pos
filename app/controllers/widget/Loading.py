import os, sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QEvent, Qt

sys.path.append(os.path.abspath(''))
from app.ui.widget.Loading_ui import Ui_DialogLoading

class LoadingController(Ui_DialogLoading, QDialog):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)

    def closeEvent(self, event:QEvent):
        event.accept()
        pass