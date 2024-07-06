import os, sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QEvent

sys.path.append(os.path.abspath(''))
from app.ui.forms.Manage_ui import Ui_MainWindowManage
from app.utils.helpers import getManageTypeByIndex

class ManageController(Ui_MainWindowManage, QMainWindow):
    def __init__(self, userId):
        super().__init__()
        self.windowEvent = 'NO_EVENT'
        self.setupUi(self)
        
        self.userId = userId
        # --
        self.actionSales.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(0))
        self.actionTransaction.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(1))
        self.actionItem.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(2))
        self.actionStock.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(3))
        self.actionPromo.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(4))
        self.actionReward.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(5))
        self.actionMember.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(6))
        self.actionUser.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(7))
        
        self.actionLogout.triggered.connect(self.onActionLogoutTriggered)
           
        self.updateMenuBarInfo(0)
        self.updateStatusBarInfo()
        
    def onActionLogoutTriggered(self):
        confirmation = QMessageBox.warning(self, 'Logout', "Are you sure you want to logout?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirmation == QMessageBox.StandardButton.Yes:
            self.close()
            self.windowEvent = 'START_LOGIN'
            self.userId = None
    
    def setStackedWidgetManageCurrentIndex(self, index):
        self.stackedWidgetManage.setCurrentIndex(index)
        self.updateMenuBarInfo(index)

    def updateMenuBarInfo(self, index):
        self.menuManage.setTitle(getManageTypeByIndex(index))
                        
        self.actionSales.setChecked(index == 0)
        self.actionTransaction.setChecked(index == 1)
        self.actionItem.setChecked(index == 2)
        self.actionStock.setChecked(index == 3)
        self.actionPromo.setChecked(index == 4)
        self.actionReward.setChecked(index == 5)
        self.actionMember.setChecked(index == 6)
        self.actionUser.setChecked(index == 7)
        
    def updateStatusBarInfo(self):
        self.labelDatabaseSource.setText(f"")
    
    def closeEvent(self, event:QEvent):
        event.accept()
        pass