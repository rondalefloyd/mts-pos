import os, sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from PyQt5.QtCore import QEvent
from machineid import id

sys.path.append(os.path.abspath(''))
from app.ui.Manage_ui import Ui_MainWindowManage
from app.controllers.ManageUser import ManageUserController
from app.utils.dbops_helpers import status, GetDataThread
from app.utils.ui_helpers import getManageTypeByIndex

class ManageController(Ui_MainWindowManage, QMainWindow):
    def __init__(self, currentUserData):
        super().__init__()
        self.setupUi(self)
        self._setupInitialTask(currentUserData)
    
    def _setupInitialTask(self, currentUserData):
        self.windowEvent = 'NO_EVENT'
        self.currentUserData = currentUserData
        
        # change the accessibility base on access level
        self.actionSales.setVisible(int(currentUserData['accessLevel']) >= 1)
        self.actionTransaction.setVisible(int(currentUserData['accessLevel']) >= 1)
        self.actionItem.setVisible(int(currentUserData['accessLevel']) >= 2)
        self.actionStock.setVisible(int(currentUserData['accessLevel']) >= 2)
        self.actionPromo.setVisible(int(currentUserData['accessLevel']) >= 2)
        self.actionReward.setVisible(int(currentUserData['accessLevel']) >= 3)
        self.actionMember.setVisible(int(currentUserData['accessLevel']) >= 3)
        self.actionUser.setVisible(int(currentUserData['accessLevel']) >= 3)
        
        # change the texts base on the current user
        self.labelFullName.setText(f"{self.currentUserData['fullName']}")
        self.labelMobileNumber.setText(f"{self.currentUserData['mobileNumber']}")
        self.labelDatabaseSource.setText(f"{status}")
        self.actionOrganizationConfig.setText(f"{self.currentUserData['organizationName']}")
        self.actionUserConfig.setText(f"{self.currentUserData['userName']}")

        self.stackedWidgetManage.insertWidget(7, ManageUserController(self.currentUserData))

        # setup connection for the action button in menu bar
        self.actionSales.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(0))
        self.actionTransaction.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(1))
        self.actionItem.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(2))
        self.actionStock.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(3))
        self.actionPromo.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(4))
        self.actionReward.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(5))
        self.actionMember.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(6))
        self.actionUser.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(7))
        self.actionOrganizationConfig.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(8))
        self.actionUserConfig.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(9))
        self.actionLogout.triggered.connect(self._onActionLogoutTriggered)
        
        self._onStackedWidgetManageSetCurrentIndex(7)

    def _onStackedWidgetManageSetCurrentIndex(self, index):
        self.stackedWidgetManage.setCurrentIndex(index)
        
        self.actionSales.setChecked(index == 0)
        self.actionTransaction.setChecked(index == 1)
        self.actionItem.setChecked(index == 2)
        self.actionStock.setChecked(index == 3)
        self.actionPromo.setChecked(index == 4)
        self.actionReward.setChecked(index == 5)
        self.actionMember.setChecked(index == 6)
        self.actionUser.setChecked(index == 7)
        self.actionOrganizationConfig.setChecked(index == 8)
        self.actionUserConfig.setChecked(index == 9)
        
        self.menuManage.setTitle(getManageTypeByIndex(index))
                    
    def _onActionLogoutTriggered(self):
        confirm = QMessageBox.warning(self, 'Confirm', "Logout user?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.currentUserData = None
            self.windowEvent = 'START_LOGIN'
            self.close()
            return
        
        return

    def closeEvent(self, event:QEvent):
        self.currentUserData = None
        event.accept()
        pass