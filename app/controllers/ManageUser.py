import os, sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QInputDialog, QLineEdit
from PyQt5.QtCore import QEvent

sys.path.append(os.path.abspath(''))
from app.ui.ManageUser_ui import Ui_FormMenuUser
from app.controllers.ManageActionButton import ManageActionButtonController
from app.controllers.Loading import LoadingController
from app.utils.crud import (
    getOneOrganizationByOrganizationId,
    getOneUserByUserId,
    getAllUserWithPaginationByKeyword,
    deleteUser,
    addNewUser,
)

class ManageUserController(Ui_FormMenuUser, QWidget):
    def __init__(self, currentUserData):
        super().__init__()
        self.setupUi(self)
        
        self.loadingWindow = LoadingController(self)
        self.windowEvent = 'NO_EVENT'
        self.currentUserData = currentUserData
        self.currentPage = 1
        self.totalPages = 1

        self.pushButtonAdd.clicked.connect(self._onPushButtonAddClicked)
        self.pushButtonFilter.clicked.connect(self._onPushButtonFilterClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        
        self._populateTableWidgetData()
        self._populateComboBoxOrganizationName()
    
    def _onPushButtonFilterClicked(self):
        self._populateTableWidgetData()

    def _onPushButtonDeleteClicked(self, data):
        confirmA = QMessageBox.warning(self, 'Confirm', f"Are you sure you want to delete {data['userName']}", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirmA != QMessageBox.StandardButton.Yes:
            return
            
        while True:
            accessCodeEntry, confirmB = QInputDialog.getText(self, 'Verify', "Please enter your password", QLineEdit.Password)
            
            if not confirmB:
                return
            
            result = getOneUserByUserId(self, {'userId': self.currentUserData['userId']})
            if accessCodeEntry != result['accessCode']:
                QMessageBox.critical(self, 'Error', "Incorrect password. Please try again.")
                
            result = deleteUser(self, data)
            if result is False:
                QMessageBox.critical(self, 'Error', "Failed to delete user.")
                
            QMessageBox.information(self, 'Success', f"{data['userName']} deleted.")
            self._populateTableWidgetData()
            return

    def _onPushButtonNextClicked(self):
        if self.currentPage <= self.totalPages:
            self.currentPage += 1
            self._populateTableWidgetData()

    def _onPushButtonPrevClicked(self):
        if self.totalPages > 1:
            self.currentPage -= 1
            self._populateTableWidgetData()
    
    def _onPushButtonAddClicked(self):
        result = addNewUser(self, {
            'organizationName': f"{self.comboBoxOrganizationName.currentText()}".upper(),
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
            'fullName': f"{self.lineEditFullName.text()}".upper(),
            'birthDate': f"{self.dateEditBirthDate.text()}",
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessLevel': f"{self.comboBoxAccessLevel.currentText()}",
        })
        
        if result is False:
            QMessageBox.critical(self, 'Error', "Failed to add user.")
            return
            
        QMessageBox.information(self, 'Success', "New user added.")
        self._populateTableWidgetData()

    def _populateComboBoxOrganizationName(self):
        resultA = getOneUserByUserId(self, {'userId': self.currentUserData['userId']})
        resultB = getOneOrganizationByOrganizationId(self, {'organizationId': resultA['organizationId']})
        
        self.comboBoxOrganizationName.setCurrentText(f"{resultB['organizationName']}")
    
    def _populateTableWidgetData(self):
        self.tableWidgetData.clearContents()
        
        result = getAllUserWithPaginationByKeyword(self, {
            'keyword': f"{self.lineEditFilter.text()}",
            'currentPage': self.currentPage
        })
        
        self.totalPages = result['totalPages']
        
        self.tableWidgetData.setRowCount(len(result['data']))
        
        for i, data in enumerate(result['data']):
            acitonButtonACellWidget = ManageActionButtonController(delete=True)
            organizationNameItem = QTableWidgetItem(f"{data['organizationName']}")
            userNameItem = QTableWidgetItem(f"{data['userName']}")
            accessCodeItem = QTableWidgetItem(f"{data['accessCode']}")
            fullNameItem = QTableWidgetItem(f"{data['fullName']}")
            birthDateItem = QTableWidgetItem(f"{data['birthDate']}")
            mobileNumberItem = QTableWidgetItem(f"{data['mobileNumber']}")
            accessLevelItem = QTableWidgetItem(f"{data['accessLevel']}")
            activeStatusItem = QTableWidgetItem(f"{data['activeStatus']}")
            lastLoginTsItem = QTableWidgetItem(f"{data['lastLoginTs']}")
            lastLogoutTsItem = QTableWidgetItem(f"{data['lastLogoutTs']}")
            updateTsItem = QTableWidgetItem(f"{data['updateTs']}")

            self.tableWidgetData.setCellWidget(i, 0, acitonButtonACellWidget)
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
    
            acitonButtonACellWidget.pushButtonDelete.clicked.connect(lambda _=i, data=data: self._onPushButtonDeleteClicked(data))

        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        
        self.loadingWindow.close()

    def closeEvent(self, event:QEvent):
        event.accept()
        pass