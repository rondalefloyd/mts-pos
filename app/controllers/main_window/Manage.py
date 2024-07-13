import os, sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QEvent

sys.path.append(os.path.abspath(''))
from app.ui.main_window.Manage_ui import Ui_MainWindowManage
from app.controllers.dialogs.UserConfig import UserConfigController
from app.controllers.dialogs.OrganizationConfig import OrganizationConfigController
from app.controllers.widget.ManageUser import ManageUserController
from app.utils.helpers import (
    updateUserActiveStatus,
    getManageTypeByIndex, 
    getOneUserByUserId,
    getOneOrganizationByOrganizationId,
    updateUserActiveStatus,
)
from app.models.model_association import status

class ManageController(Ui_MainWindowManage, QMainWindow):
    def __init__(self, userId):
        super().__init__()
        self.windowEvent = 'NO_EVENT'
        self.setupUi(self)
        
        self.userId = userId
        # --
        entry = {
            'userId': self.userId,
            'activeStatus': 1,
        }
        isSuccess = updateUserActiveStatus(self, entry)
        
        self.actionSales.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(0))
        self.actionTransaction.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(1))
        self.actionItem.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(2))
        self.actionStock.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(3))
        self.actionPromo.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(4))
        self.actionReward.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(5))
        self.actionMember.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(6))
        self.actionUser.triggered.connect(lambda: self.setStackedWidgetManageCurrentIndex(7))
        
        self.actionOrganizationConfig.triggered.connect(self.onActionOrganizationConfigTriggered)
        self.actionUserConfig.triggered.connect(self.onActionUserConfigTriggered)
        
        self.actionLogout.triggered.connect(self.onActionLogoutTriggered)

        self.updateMenuBarInfo(0)
        self.updateStatusBarInfo()
    
    def onActionOrganizationConfigTriggered(self):
        result = getOneUserByUserId(self, {'userId': self.userId})
        dialogOrganizationConfig = OrganizationConfigController(result['organizationId'])
        dialogOrganizationConfig.exec()
    
    def onActionUserConfigTriggered(self):
        dialogUserConfig = UserConfigController(self.userId)
        dialogUserConfig.exec()
        
    def onActionLogoutTriggered(self):
        confirmation = QMessageBox.warning(self, 'Logout', "Are you sure you want to logout?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirmation == QMessageBox.StandardButton.Yes:
            entry = {
                'userId': self.userId,
                'activeStatus': 0,
            }
            isSuccess = updateUserActiveStatus(self, entry)
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
        
        resultA = getOneUserByUserId(self, {'userId': self.userId})
        resultB = getOneOrganizationByOrganizationId(self, {'organizationId': resultA['organizationId']})
        
        self.actionOrganizationConfig.setText(f"{resultB['organizationName']}")
        self.actionUserConfig.setText(f"{resultA['userName']}")
        
        # TODO: fix accessibility base on accessLevel
        self.actionSales.setVisible(resultA['accessLevel'] >= 1)
        self.actionTransaction.setVisible(resultA['accessLevel'] >= 1)
        self.actionItem.setVisible(resultA['accessLevel'] >= 2)
        self.actionStock.setVisible(resultA['accessLevel'] >= 2)
        self.actionPromo.setVisible(resultA['accessLevel'] >= 2)
        self.actionReward.setVisible(resultA['accessLevel'] >= 3)
        self.actionMember.setVisible(resultA['accessLevel'] >= 3)
        self.actionUser.setVisible(resultA['accessLevel'] >= 3)
                
        self.stackedWidgetManage.insertWidget(7, ManageUserController(self.userId))
        
    def updateStatusBarInfo(self):
        result = getOneUserByUserId(self, {'userId': self.userId})
        
        self.labelFullName.setText(f"{result['fullName']}")
        self.labelMobileNumber.setText(f"{result['mobileNumber']}")
        self.labelDatabaseSource.setText(f"{status}")
    
    def closeEvent(self, event:QEvent):
        event.accept()
        pass