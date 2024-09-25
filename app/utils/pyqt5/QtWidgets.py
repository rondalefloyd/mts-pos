from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        QTimer.singleShot(0, self._executeTask)

    def _executeTask(self):
        objectName = self.objectName()
        print('--objectName:', objectName)
        
        if objectName == 'tableWidgetData':
            self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        elif objectName == 'tableWidgetOrderItem':
            self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
            self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            pass