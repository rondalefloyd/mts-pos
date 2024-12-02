# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.global_variables import *
from app.views.templates.Manage_ui import Ui_MainWindowManage
from app.views.components.Loading import Loading
from app.views.validator import *
from app.views.components.EditCurrentUser import EditCurrentUser
from app.views.components.EditCurrentOrganization import EditCurrentOrganization
from app.views.components.ManageUser import ManageUsers
from app.views.components.ManageMember import ManageMembers
from app.views.components.ManagePromo import ManagePromos
from app.views.components.ManageReward import ManageRewards
from app.views.components.ManageProduct import ManageProducts
from app.views.components.ManageItem import ManageItems
from app.views.components.ManageItemType import ManageItemTypes
from app.views.components.ManageBrand import ManageBrands
from app.views.components.ManageSupplier import ManageSuppliers
from app.views.components.ManageStock import ManageStocks
from app.views.components.ManageSales import ManageSales
from app.views.components.ManageReceipt import ManageReceipts
from app.controllers.dedicated.authenticate import AuthenticateThread

# class definition
class Manage(Ui_MainWindowManage, QMainWindow):
    # initialization method (__init__)
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.userData = authData['user']
        self.organizationData = authData['organization']
        self.currentThread = None
        self.activeThreads = []
        
        # Initialize widgets only once
        self.manageSales = ManageSales(authData)
        self.manageReceipts = ManageReceipts(authData)
        self.manageStocks = ManageStocks(authData)
        self.manageProducts = ManageProducts(authData)
        self.manageItems = ManageItems(authData)
        self.manageItemTypes = ManageItemTypes(authData)
        self.manageBrands = ManageBrands(authData)
        self.manageSuppliers = ManageSuppliers(authData)
        self.managePromos = ManagePromos(authData)
        self.manageRewards = ManageRewards(authData)
        self.manageMembers = ManageMembers(authData)
        self.manageUsers = ManageUsers(authData)
        
        # Add widgets to the stacked widget
        self.stackedWidgetManage.insertWidget(0, self.manageSales)
        self.stackedWidgetManage.insertWidget(1, self.manageReceipts)
        self.stackedWidgetManage.insertWidget(2, self.manageProducts)
        self.stackedWidgetManage.insertWidget(3, self.manageStocks)
        self.stackedWidgetManage.insertWidget(4, self.managePromos)
        self.stackedWidgetManage.insertWidget(5, self.manageRewards)
        self.stackedWidgetManage.insertWidget(6, self.manageMembers)
        self.stackedWidgetManage.insertWidget(7, self.manageUsers)
        self.stackedWidgetManage.insertWidget(8, self.manageItems)
        self.stackedWidgetManage.insertWidget(9, self.manageItemTypes)
        self.stackedWidgetManage.insertWidget(10, self.manageBrands)
        self.stackedWidgetManage.insertWidget(11, self.manageSuppliers)
        
        self.labelFullName.setText(f"{self.userData['fullName']}")
        self.labelMobileNumber.setText(f"{self.userData['mobileNumber']}")
        self.actionCurrentOrganization.setText(f"{self.organizationData['organizationName']}")
        self.actionCurrentUser.setText(f"{self.userData['userName']}")
        
        self.actionSales.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(0))
        self.actionTransactions.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(1))
        self.actionAll.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(2))
        self.actionStocks.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(3))
        self.actionPromos.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(4))
        self.actionRewards.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(5))
        self.actionMembers.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(6))
        self.actionUsers.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(7))
        self.actionItems.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(8))
        self.actionItemTypes.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(9))
        self.actionBrands.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(10))
        self.actionSuppliers.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(11))
        
        self.actionLogout.triggered.connect(self._onActionLogoutTriggered)
        
        self.actionCurrentOrganization.triggered.connect(self._onActionCurrentOrganizationTriggered)
        self.actionCurrentUser.triggered.connect(self._onActionCurrentUserTriggered)

        self._onStackedWidgetManageSetCurrentIndex(0)

    # private methods
    def _onStackedWidgetManageSetCurrentIndex(self, index):
        self.stackedWidgetManage.setCurrentIndex(index)
        
        self.actionSales.setChecked(index == 0)
        self.actionTransactions.setChecked(index == 1)
        self.actionAll.setChecked(index == 2)
        self.actionStocks.setChecked(index == 3)
        self.actionPromos.setChecked(index == 4)
        self.actionRewards.setChecked(index == 5)
        self.actionMembers.setChecked(index == 6)
        self.actionUsers.setChecked(index == 7)
        self.actionItems.setChecked(index == 8)
        self.actionItemTypes.setChecked(index == 9)
        self.actionBrands.setChecked(index == 10)
        self.actionSuppliers.setChecked(index == 11)

        menuManageTitle = 'Unavailable'
        
        match index:
            case 0:
                menuManageTitle = 'Sales'
                self.manageSales.refresh()
            case 1:
                menuManageTitle = 'Transactions'
                self.manageReceipts.refresh()
            case 2:
                menuManageTitle = 'Product: All'
                self.manageProducts.refresh()
            case 3:
                menuManageTitle = 'Stocks'
                self.manageStocks.refresh()
            case 4:
                menuManageTitle = 'Promos'
                self.managePromos.refresh()
            case 5:
                menuManageTitle = 'Rewards'
                self.manageRewards.refresh()
            case 6:
                menuManageTitle = 'Members'
                self.manageMembers.refresh()
            case 7:
                menuManageTitle = 'Users'
                self.manageUsers.refresh()
            case 8:
                menuManageTitle = 'Product: Items'
                self.manageItems.refresh()
            case 9:
                menuManageTitle = 'Product: Types'
                self.manageItemTypes.refresh()
            case 10:
                menuManageTitle = 'Product: Brands'
                self.manageBrands.refresh()
            case 11:
                menuManageTitle = 'Product: Suppliers'
                self.manageSuppliers.refresh()
                
        self.menuManage.setTitle(menuManageTitle)

    def _onActionCurrentOrganizationTriggered(self):
        self.editCurrentOrganization = EditCurrentOrganization(self.authData)
        self.editCurrentOrganization.exec()
        self.windowEvent = self.editCurrentOrganization.windowEvent

        if self.windowEvent == EVENT_START_LOGIN:
            self.authData = None
            self.close()
            pass
    
    def _onActionCurrentUserTriggered(self):
        self.editCurrentUser = EditCurrentUser(self.authData)
        self.editCurrentUser.exec()
        self.windowEvent = self.editCurrentUser.windowEvent

        if self.windowEvent == EVENT_START_LOGIN:
            self.authData = None
            self.close()
            pass

    def _onActionLogoutTriggered(self):
        confirm = QMessageBox.warning(self, 'Confirm', f"Logout {self.userData['userName']}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.loading.show()
            self.currentThread = AuthenticateThread('unauthenticateUserById', {'id': self.userData['id']})
            self.currentThread.finished.connect(self._handleOnActionLogoutTriggeredFinished)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.finished.connect(self.loading.close)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)
        
    def _handleOnActionLogoutTriggeredFinished(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
        
        self.windowEvent = EVENT_START_LOGIN
        self.authData = None
        self.close()

    def _cleanupThread(self):
        sender = self.sender()
        if sender in self.activeThreads:
            self.activeThreads.remove(sender)
        self.currentThread = None
        print('active threads:', self.activeThreads)

    # overridden methods
    def closeEvent(self, event):
        self.authData = None
        
        for thread in self.activeThreads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        
        self.activeThreads.clear()
        
        # Set the window event state to EVENT_START_LOGIN
        self.windowEvent = EVENT_START_LOGIN
        
        event.accept() # for closing the window
        
        print('closed...')
