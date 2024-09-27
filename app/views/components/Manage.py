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
from app.views.components.EditCurrentUser import EditCurrentUser
from app.views.components.EditCurrentOrganization import EditCurrentOrganization
from app.views.components.ManageUser import ManageUser
from app.views.components.ManageMember import ManageMember
from app.views.components.ManagePromo import ManagePromo
from app.views.components.ManageReward import ManageReward
from app.views.components.ManageProduct import ManageProduct
from app.views.components.ManageItem import ManageItem
from app.views.components.ManageItemType import ManageItemType
from app.views.components.ManageBrand import ManageBrand
from app.views.components.ManageSupplier import ManageSupplier
from app.views.components.ManageStock import ManageStock
from app.views.components.ManageSales import ManageSales
from app.views.components.ManageReceipt import ManageReceipt
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
        self.manageReceipt = ManageReceipt(authData)
        self.manageStock = ManageStock(authData)
        self.manageProduct = ManageProduct(authData)
        self.manageItem = ManageItem(authData)
        self.manageItemType = ManageItemType(authData)
        self.manageBrand = ManageBrand(authData)
        self.manageSupplier = ManageSupplier(authData)
        self.managePromo = ManagePromo(authData)
        self.manageReward = ManageReward(authData)
        self.manageMember = ManageMember(authData)
        self.manageUser = ManageUser(authData)
        
        # Add widgets to the stacked widget
        self.stackedWidgetManage.insertWidget(0, self.manageSales)
        self.stackedWidgetManage.insertWidget(1, self.manageReceipt)
        self.stackedWidgetManage.insertWidget(2, self.manageProduct)
        self.stackedWidgetManage.insertWidget(3, self.manageStock)
        self.stackedWidgetManage.insertWidget(4, self.managePromo)
        self.stackedWidgetManage.insertWidget(5, self.manageReward)
        self.stackedWidgetManage.insertWidget(6, self.manageMember)
        self.stackedWidgetManage.insertWidget(7, self.manageUser)
        self.stackedWidgetManage.insertWidget(8, self.manageItem)
        self.stackedWidgetManage.insertWidget(9, self.manageItemType)
        self.stackedWidgetManage.insertWidget(10, self.manageBrand)
        self.stackedWidgetManage.insertWidget(11, self.manageSupplier)
        
        self.labelFullName.setText(f"{self.userData['fullName']}")
        self.labelMobileNumber.setText(f"{self.userData['mobileNumber']}")
        self.labelDatabaseSource.setText(f"test")
        self.actionCurrentOrganization.setText(f"{self.organizationData['organizationName']}")
        self.actionCurrentUser.setText(f"{self.userData['userName']}")
        
        self.actionSales.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(0))
        self.actionTransaction.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(1))
        self.actionAll.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(2))
        self.actionStock.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(3))
        self.actionPromo.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(4))
        self.actionReward.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(5))
        self.actionMember.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(6))
        self.actionUser.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(7))
        self.actionItem.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(8))
        self.actionItemType.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(9))
        self.actionBrand.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(10))
        self.actionSupplier.triggered.connect(lambda: self._onStackedWidgetManageSetCurrentIndex(11))
        
        self.actionLogout.triggered.connect(self._onActionLogoutTriggered)
        
        self.actionCurrentOrganization.triggered.connect(self._onActionCurrentOrganizationTriggered)
        self.actionCurrentUser.triggered.connect(self._onActionCurrentUserTriggered)

        self._onStackedWidgetManageSetCurrentIndex(0)

    # private methods
    def _onStackedWidgetManageSetCurrentIndex(self, index):
        self.stackedWidgetManage.setCurrentIndex(index)
        
        self.actionSales.setChecked(index == 0)
        self.actionTransaction.setChecked(index == 1)
        self.actionAll.setChecked(index == 2)
        self.actionStock.setChecked(index == 3)
        self.actionPromo.setChecked(index == 4)
        self.actionReward.setChecked(index == 5)
        self.actionMember.setChecked(index == 6)
        self.actionUser.setChecked(index == 7)
        self.actionItem.setChecked(index == 8)
        self.actionItemType.setChecked(index == 9)
        self.actionBrand.setChecked(index == 10)
        self.actionSupplier.setChecked(index == 11)

        menuManageTitle = 'Unavailable'
        
        match index:
            case 0:
                menuManageTitle = 'Sales'
                self.manageSales.refresh()
            case 1:
                menuManageTitle = 'Transaction'
                self.manageReceipt.refresh()
            case 2:
                menuManageTitle = 'All'
                self.manageProduct.refresh()
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
            case 8:
                menuManageTitle = 'Item'
                self.manageItem.refresh()
            case 9:
                menuManageTitle = 'ItemType'
                self.manageItemType.refresh()
            case 10:
                menuManageTitle = 'Brand'
                self.manageBrand.refresh()
            case 11:
                menuManageTitle = 'Supplier'
                self.manageSupplier.refresh()
                
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
            self.currentThread = AuthenticateThread('unauthenticate_user_by_id', {'id': self.userData['id']})
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
