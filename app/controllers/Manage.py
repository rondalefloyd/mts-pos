import os, sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QEvent

sys.path.append(os.path.abspath(''))
from app.ui.Manage_ui import Ui_MainWindowManage
from app.controllers.UserConfig import UserConfigController
from app.controllers.OrganizationConfig import OrganizationConfigController
from app.controllers.ManageUser import ManageUserController
from app.utils.crud import (
    _updateUserActiveStatus,
    _updateUserActiveStatus,
)
from app.utils.gui import getManageTypeByIndex
from app.utils.turso import status

class ManageController(Ui_MainWindowManage, QMainWindow):
    def __init__(self, currentUserData):
        super().__init__()
        self.setupUi(self)
        
        self.windowEvent = 'NO_EVENT'
        self.currentUserData = currentUserData

        result = _updateUserActiveStatus(self, {
            'userId': self.currentUserData['userId'],
            'activeStatus': 1,
        })
        
        self.actionOrganizationConfig.setText(f"{self.currentUserData['organizationName']}")
        self.actionUserConfig.setText(f"{self.currentUserData['userName']}")
        
        self.actionSales.setVisible(self.currentUserData['accessLevel'] >= 1)
        self.actionTransaction.setVisible(self.currentUserData['accessLevel'] >= 1)
        self.actionItem.setVisible(self.currentUserData['accessLevel'] >= 2)
        self.actionStock.setVisible(self.currentUserData['accessLevel'] >= 2)
        self.actionPromo.setVisible(self.currentUserData['accessLevel'] >= 2)
        self.actionReward.setVisible(self.currentUserData['accessLevel'] >= 3)
        self.actionMember.setVisible(self.currentUserData['accessLevel'] >= 3)
        self.actionUser.setVisible(self.currentUserData['accessLevel'] >= 3)
        
        self.stackedWidgetManage.insertWidget(7, ManageUserController(self.currentUserData))
        
        self.actionSales.triggered.connect(lambda: self._setStackedWidgetManageCurrentIndex(0))
        self.actionTransaction.triggered.connect(lambda: self._setStackedWidgetManageCurrentIndex(1))
        self.actionItem.triggered.connect(lambda: self._setStackedWidgetManageCurrentIndex(2))
        self.actionStock.triggered.connect(lambda: self._setStackedWidgetManageCurrentIndex(3))
        self.actionPromo.triggered.connect(lambda: self._setStackedWidgetManageCurrentIndex(4))
        self.actionReward.triggered.connect(lambda: self._setStackedWidgetManageCurrentIndex(5))
        self.actionMember.triggered.connect(lambda: self._setStackedWidgetManageCurrentIndex(6))
        self.actionUser.triggered.connect(lambda: self._setStackedWidgetManageCurrentIndex(7))
        
        self.actionOrganizationConfig.triggered.connect(self._onActionOrganizationConfigTriggered)
        self.actionUserConfig.triggered.connect(self._onActionUserConfigTriggered)
        self.actionLogout.triggered.connect(self._onActionLogoutTriggered)

        self._updateMenuBarInfo(0)
        self._updateStatusBarInfo()
    
    def _onActionOrganizationConfigTriggered(self):
        dialogOrganizationConfig = OrganizationConfigController(self.currentUserData['organizationId'])
        dialogOrganizationConfig.exec()
    
    def _onActionUserConfigTriggered(self):
        dialogUserConfig = UserConfigController(self.currentUserData)
        dialogUserConfig.exec()
        
    def _onActionLogoutTriggered(self):
        confirmation = QMessageBox.warning(self, 'Logout', "Are you sure you want to logout?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirmation == QMessageBox.StandardButton.Yes:
            result = _updateUserActiveStatus(self, {
                'userId': self.currentUserData['userId'],
                'activeStatus': 0,
            })
            self.close()
            self.windowEvent = 'START_LOGIN'
            self.currentUserData = None
    
    def _setStackedWidgetManageCurrentIndex(self, index):
        self.stackedWidgetManage.setCurrentIndex(index)
        self._updateMenuBarInfo(index)

    def _updateMenuBarInfo(self, index):
        self.menuManage.setTitle(getManageTypeByIndex(index))
        
        self.actionSales.setChecked(index == 0)
        self.actionTransaction.setChecked(index == 1)
        self.actionItem.setChecked(index == 2)
        self.actionStock.setChecked(index == 3)
        self.actionPromo.setChecked(index == 4)
        self.actionReward.setChecked(index == 5)
        self.actionMember.setChecked(index == 6)
        self.actionUser.setChecked(index == 7)
                
    def _updateStatusBarInfo(self):
        self.labelFullName.setText(f"{self.currentUserData['fullName']}")
        self.labelMobileNumber.setText(f"{self.currentUserData['mobileNumber']}")
        self.labelDatabaseSource.setText(f"{status}")
    
    def closeEvent(self, event:QEvent):
        event.accept()
        pass