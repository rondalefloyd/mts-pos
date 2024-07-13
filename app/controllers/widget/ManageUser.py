import os, sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QInputDialog, QLineEdit
from PyQt5.QtCore import QEvent

sys.path.append(os.path.abspath(''))
from app.ui.widget.ManageUser_ui import Ui_FormMenuUser
from app.controllers.widget.ManageActionButton import ManageActionButtonController
from app.utils.function_helpers import (
    getOneOrganizationByOrganizationId,
    getOneUserByUserId,
    getAllUserWithPaginationByKeyword,
    deleteUser,
    addNewUser,
    updatePaginationInfo,
)
from app.models.model_association import status

class ManageUserController(Ui_FormMenuUser, QWidget):
    def __init__(self, userId):
        super().__init__()
        self.setupUi(self)
        
        self.windowEvent = 'NO_EVENT'
        self.userId = userId
        self.currentPage = 1
        self.totalPages = 1

        self.pushButtonAdd.clicked.connect(self.onPushButtonAddClicked)
        self.pushButtonFilter.clicked.connect(self.onPushButtonFilterClicked)
        self.pushButtonNext.clicked.connect(self.onPushButtonNextClicked)
        self.pushButtonPrev.clicked.connect(self.onPushButtonPrevClicked)
        
        self.populateTableWidgetData()
        self.populateComboBoxOrganizationName()
    
    def onPushButtonFilterClicked(self):
        self.populateTableWidgetData()

    def onPushButtonDeleteClicked(self, data):
        confirmA = QMessageBox.warning(self, 'Confirm', f"Are you sure you want to delete {data['userName']}", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirmA != QMessageBox.StandardButton.Yes:
            return
            
        while True:
            accessCodeEntry, confirmB = QInputDialog.getText(self, 'Verify', "Please enter your password", QLineEdit.Password)
            
            if not confirmB:
                return
            
            result = getOneUserByUserId(self, {'userId': self.userId})
            if accessCodeEntry != result['accessCode']:
                QMessageBox.critical(self, 'Error', "Incorrect password. Please try again.")
                
            isSuccess = deleteUser(self, data)
            if isSuccess is False:
                QMessageBox.information(self, 'Error', "Failed to delete user.")
                
            QMessageBox.information(self, 'Success', f"{data['userName']} deleted.")
            self.populateTableWidgetData()
            return

    def onPushButtonNextClicked(self):
        if self.currentPage <= self.totalPages:
            self.currentPage += 1
            self.populateTableWidgetData()

    def onPushButtonPrevClicked(self):
        if self.totalPages > 1:
            self.currentPage -= 1
            self.populateTableWidgetData()
    
    def onPushButtonAddClicked(self):
        isSuccess = addNewUser(self, {
            'organizationName': f"{self.comboBoxOrganizationName.currentText()}".upper(),
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
            'fullName': f"{self.lineEditFullName.text()}".upper(),
            'birthDate': f"{self.dateEditBirthDate.text()}",
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessLevel': f"{self.comboBoxAccessLevel.currentText()}",
        })
        
        if isSuccess is False:
            QMessageBox.information(self, 'Error', "Failed to add user.")
            
        QMessageBox.information(self, 'Success', "New user added.")
        self.populateTableWidgetData()

    def populateComboBoxOrganizationName(self):
        resultA = getOneUserByUserId(self, {'userId': self.userId})
        resultB = getOneOrganizationByOrganizationId(self, {'organizationId': resultA['organizationId']})
        
        self.comboBoxOrganizationName.setCurrentText(f"{resultB['organizationName']}")
    
    def populateTableWidgetData(self):
        # TODO: add threading 
        result = getAllUserWithPaginationByKeyword(self, {
            'keyword': f"{self.lineEditFilter.text()}",
            'currentPage': self.currentPage
        })
        self.totalPages = result['totalPages']
        
        updatePaginationInfo(self)
        
        self.tableWidgetData.clearContents()
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
    
            acitonButtonACellWidget.pushButtonDelete.clicked.connect(lambda _=i, data=data: self.onPushButtonDeleteClicked(data))

    def closeEvent(self, event:QEvent):
        event.accept()
        pass