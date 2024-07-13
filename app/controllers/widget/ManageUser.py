import os, sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QInputDialog, QLineEdit
from PyQt5.QtCore import QEvent

sys.path.append(os.path.abspath(''))
from app.ui.widget.ManageUser_ui import Ui_FormMenuUser
from app.controllers.widget.ManageActionButton import ManageActionButtonController
from app.utils.helpers import (
    getOneOrganizationByOrganizationId,
    getOneUserByUserId,
    getAllUserWithPaginationByKeyword,
    deleteUser,
    addNewUser,
)
from app.models.model_association import status

class ManageUserController(Ui_FormMenuUser, QWidget):
    def __init__(self, userId):
        super().__init__()
        self.windowEvent = 'NO_EVENT'
        self.setupUi(self)
        
        self.userId = userId
        self.currentPage = 1
        self.totalPages = 1
        # --
        self.pushButtonAdd.clicked.connect(self.onPushButtonAddClicked)
        self.pushButtonFilter.clicked.connect(self.onPushButtonFilterClicked)
        self.pushButtonNext.clicked.connect(self.onPushButtonNextClicked)
        self.pushButtonPrev.clicked.connect(self.onPushButtonPrevClicked)
        
        self.populateTableWidgetData()
        self.populateComboBoxOrganizationName()
        
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
    
    def onPushButtonNextClicked(self):
        if self.currentPage <= self.totalPages:
            self.currentPage += 1
            self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)
            self.pushButtonPrev.setEnabled(self.currentPage > 1)
            self.populateTableWidgetData()

    def onPushButtonPrevClicked(self):
        if self.totalPages > 1:
            self.currentPage -= 1
            self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)
            self.pushButtonPrev.setEnabled(self.currentPage > 1)
            self.populateTableWidgetData()

    
    def populateComboBoxOrganizationName(self):
        resultA = getOneUserByUserId(self, {'userId': self.userId})
        resultB = getOneOrganizationByOrganizationId(self, {'organizationId': resultA['organizationId']})
        
        self.comboBoxOrganizationName.setCurrentText(f"{resultB['organizationName']}")
    
    def populateTableWidgetData(self):
        # TODO: add threading
        entry = {
            'keyword': f"{self.lineEditFilter.text()}",
            'currentPage': self.currentPage
        }
        
        result = getAllUserWithPaginationByKeyword(self, entry)
        
        self.totalPages = result['totalPages']
        
        self.setLabelPageIndicatorText()
        
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
    
            acitonButtonACellWidget.pushButtonView.clicked.connect(lambda _=i, data=data: self.onPushButtonViewClicked(data))
            acitonButtonACellWidget.pushButtonDelete.clicked.connect(lambda _=i, data=data: self.onPushButtonDeleteClicked(data))

    def onPushButtonDeleteClicked(self, data):
        confirmA = QMessageBox.warning(self, 'Confirm', f"Are you sure you want to delete {data['userName']}", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirmA == QMessageBox.StandardButton.Yes:
            while True:
                accessCodeEntry, confirmB = QInputDialog.getText(self, 'Verify', "Please enter your password", QLineEdit.Password)
                
                if confirmB:
                    result = getOneUserByUserId(self, {'userId': self.userId})
                    
                    if accessCodeEntry == result['accessCode']:
                        result = deleteUser(self, data)
                        QMessageBox.information(self, 'Success', f"{data['userName']} deleted.")
                        self.populateTableWidgetData()
                        break
                    else:
                        QMessageBox.critical(self, 'Error', "Incorrect password. Please try again.")

    
    def setLabelPageIndicatorText(self):
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
    
    def onPushButtonFilterClicked(self):
        self.populateTableWidgetData()
    
    def onPushButtonAddClicked(self):
        entry = {
            'organizationName': f"{self.comboBoxOrganizationName.currentText()}".upper(),
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
            'fullName': f"{self.lineEditFullName.text()}".upper(),
            'birthDate': f"{self.dateEditBirthDate.text()}",
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessLevel': f"{self.comboBoxAccessLevel.currentText()}",
        }
        
        isSuccess = addNewUser(self, entry)
        
        if isSuccess is True:
            QMessageBox.information(self, 'Success', "New user added.")
            self.populateTableWidgetData()
    
    def closeEvent(self, event:QEvent):
        event.accept()
        pass