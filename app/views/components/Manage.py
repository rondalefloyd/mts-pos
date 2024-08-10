# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.Manage_ui import Ui_MainWindowManage
from app.views.components.Loading import Loading
from app.views.components.ManageUser import ManageUser
from app.views.components.ManageMember import ManageMember
from app.views.components.ManagePromo import ManagePromo
from app.views.components.ManageReward import ManageReward
from app.views.components.ManageItem import ManageItem
from app.views.components.ManageStock import ManageStock
from app.controllers.dedicated.authenticate import AuthenticateThread

# class definition
class Manage(Ui_MainWindowManage, QMainWindow):
    # initialization method (__init__)
    def __init__(self, userData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.userData = userData
        self.currentThread = None
        self.activeThreads = []
        
        # Initialize widgets only once
        self.manageStock = ManageStock(self.userData)
        self.manageItem = ManageItem(self.userData)
        self.managePromo = ManagePromo(self.userData)
        self.manageReward = ManageReward(self.userData)
        self.manageMember = ManageMember(self.userData)
        self.manageUser = ManageUser(self.userData)
        
        # Add widgets to the stacked widget
        self.stackedWidgetManage.insertWidget(2, self.manageItem)
        self.stackedWidgetManage.insertWidget(3, self.manageStock)
        self.stackedWidgetManage.insertWidget(4, self.managePromo)
        self.stackedWidgetManage.insertWidget(5, self.manageReward)
        self.stackedWidgetManage.insertWidget(6, self.manageMember)
        self.stackedWidgetManage.insertWidget(7, self.manageUser)
        
        self.labelFullName.setText(f"{self.userData['fullName']}")
        self.labelMobileNumber.setText(f"{self.userData['mobileNumber']}")
        self.labelDatabaseSource.setText(f"test")
        
        self.actionSales.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(0))
        self.actionTransaction.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(1))
        self.actionItem.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(2))
        self.actionStock.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(3))
        self.actionPromo.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(4))
        self.actionReward.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(5))
        self.actionMember.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(6))
        self.actionUser.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(7))
        
        self.actionLogout.triggered.connect(self._onActionLogoutTriggered)

        self._onStackedWidgetManageSetCurrentIndex(0)

    # private methods
    def _onStackedWidgetManageSetCurrentIndex(self, index):
        self.stackedWidgetManage.setCurrentIndex(index)
        
        self.actionSales.setChecked(self.stackedWidgetManage.currentIndex() == 0)
        self.actionTransaction.setChecked(self.stackedWidgetManage.currentIndex() == 1)
        self.actionItem.setChecked(self.stackedWidgetManage.currentIndex() == 2)
        self.actionStock.setChecked(self.stackedWidgetManage.currentIndex() == 3)
        self.actionPromo.setChecked(self.stackedWidgetManage.currentIndex() == 4)
        self.actionReward.setChecked(self.stackedWidgetManage.currentIndex() == 5)
        self.actionMember.setChecked(self.stackedWidgetManage.currentIndex() == 6)
        self.actionUser.setChecked(self.stackedWidgetManage.currentIndex() == 7)

        menuManageTitle = 'Unavailable'
        
        match index:
            case 0:
                menuManageTitle = 'Sale'
            case 1:
                menuManageTitle = 'Transaction'
            case 2:
                menuManageTitle = 'Item'
                self.manageItem.refresh()
            case 3:
                menuManageTitle = 'Stock'
                self.manageStock.refresh()
            case 4:
                menuManageTitle = 'Promo'
                self.managePromo.refresh()
            case 5:
                menuManageTitle = 'Reward'
                self.manageReward.refresh()
            case 6:
                menuManageTitle = 'Member'
                self.manageMember.refresh()
            case 7:
                menuManageTitle = 'User'
                self.manageUser.refresh()
                
        self.menuManage.setTitle(menuManageTitle)

    def _onActionLogoutTriggered(self):
        confirm = QMessageBox.warning(self, 'Confirm', f"Logout {self.userData['userName']}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.currentThread = AuthenticateThread('unauthenticate_user_by_id', {'id': self.userData['id']})
            self.currentThread.finished.connect(self._handleOnActionLogoutTriggeredResult)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnActionLogoutTriggeredResult(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
        
        self.windowEvent = EVENT_START_LOGIN
        self.userData = None
        self.close()

    def _cleanupThread(self):
        sender = self.sender()
        if sender in self.activeThreads:
            self.activeThreads.remove(sender)
        self.currentThread = None
        print('active threads:', self.activeThreads)

    # overridden methods
    def closeEvent(self, event):
        for thread in self.activeThreads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        
        self.activeThreads.clear()
        
        # Set the window event state to EVENT_START_LOGIN
        self.windowEvent = EVENT_START_LOGIN
        
        event.accept()
        
        print('closed...')
