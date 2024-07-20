import os, sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QEvent
from machineid import id
import threading

sys.path.append(os.path.abspath(''))
from app.ui.ManageUser_ui import Ui_FormManageUser
from app.controllers.Loader import LoaderController
from app.controllers.ActionButtonA import ActionButtonAController
from app.utils.dbops_helpers import status, GetDataThread

class ManageUserController(Ui_FormManageUser, QWidget):
    def __init__(self, currentUserData):
        super().__init__()
        self.setupUi(self)
        self._setupInitialTask(currentUserData)
    
    def _setupInitialTask(self, currentUserData):
        self.windowEvent = 'NO_EVENT'
        self.currentUserData = currentUserData
        
        self.currentPage = 1
        self.totalPages = 1
        
        self.comboBoxOrganizationName.setCurrentText(f"{self.currentUserData['organizationName']}")
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        
        self.lineEditFilter.textChanged.connect(self._onLineEditFilterTextChanged)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)

        self._populateTableWidgetData()
    
    def _onLineEditFilterTextChanged(self):
        self._populateTableWidgetData()
    
    def _onPushButtonPrevClicked(self):
        if self.currentPage > 1:
            self.currentPage -= 1
            self._populateTableWidgetData()

    def _onPushButtonNextClicked(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
            self._populateTableWidgetData()
        
    def _populateTableWidgetData(self):
        self.loaderController = LoaderController()
        self.loaderController.show()
        
        self.getDataThread = GetDataThread()
        self.getDataThread.finished.connect(self._handlePopulateTableWidgetDataResult)
        self.getDataThread.setRequirements(self, '_getAllUserWithPaginationByKeyword', {
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text()}",
        })
        self.getDataThread.start()
        self._printActiveThreads()
        
    def _handlePopulateTableWidgetDataResult(self, result):
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(result['data']))
        
        self.totalPages = result['totalPages']
        
        for i, data in enumerate(result['data']):
            actionButtonAController = ActionButtonAController(allowDelete=True)
            organizationNameItem = QTableWidgetItem(data['organizationName'])
            userNameItem = QTableWidgetItem(data['userName'])
            accessCodeItem = QTableWidgetItem(data['accessCode'])
            fullNameItem = QTableWidgetItem(data['fullName'])
            birthDateItem = QTableWidgetItem(data['birthDate'])
            mobileNumberItem = QTableWidgetItem(data['mobileNumber'])
            accessLevelItem = QTableWidgetItem(data['accessLevel'])
            activeStatusItem = QTableWidgetItem(data['activeStatus'])
            lastLoginTsItem = QTableWidgetItem(data['lastLoginTs'])
            lastLogoutTsItem = QTableWidgetItem(data['lastLogoutTs'])
            updateTsItem = QTableWidgetItem(data['updateTs'])

            self.tableWidgetData.setCellWidget(i, 0, actionButtonAController)
            self.tableWidgetData.setItem(i, 1, organizationNameItem)
            self.tableWidgetData.setItem(i, 2, userNameItem)
            self.tableWidgetData.setItem(i, 3, accessCodeItem)
            self.tableWidgetData.setItem(i, 4, fullNameItem)
            self.tableWidgetData.setItem(i, 5, birthDateItem)
            self.tableWidgetData.setItem(i, 6, mobileNumberItem)
            self.tableWidgetData.setItem(i, 7, accessLevelItem)
            self.tableWidgetData.setItem(i, 8, activeStatusItem)
            self.tableWidgetData.setItem(i, 9, lastLoginTsItem)
            self.tableWidgetData.setItem(i, 10, lastLogoutTsItem)
            self.tableWidgetData.setItem(i, 11, updateTsItem)
    
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)
        self.loaderController.close()

    def _printActiveThreads(self):
        active_threads = threading.enumerate()
        print("Current running threads:")
        for thread in active_threads:
            print(thread.name)
            
    def closeEvent(self, event:QEvent):
        self.currentUserData = None
        event.accept()
        pass