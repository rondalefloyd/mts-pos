# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.global_variables import *
from app.views.templates.ManageUser_ui import Ui_FormManageUser
from app.views.components.Loading import Loading
from app.views.components.EditUser import EditUser
from app.views.components.ManageActionButton import ManageActionButton
from app.views.validator import *
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

# class definition
class ManageUser(Ui_FormManageUser, QWidget):
    # initialization method (__init__)
    def __init__(self, authData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.authData = authData
        self.organizationData = authData['organization']
        self.currentThread = None
        self.activeThreads = []
        
        self.lineEditUserName.setValidator(nonSpaceTextFormatValidator())
        self.lineEditFullName.setValidator(fullNameValidator())
        self.lineEditMobileNumber.setValidator(mobileNumberValidator())
        
        self.refresh()
        
        self.pushButtonFilter.clicked.connect(self._onPushButtonFilterClicked)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)
        self.pushButtonClear.clicked.connect(self._onPushButtonClearClicked)
        self.pushButtonAdd.clicked.connect(self._onPushButtonAddClicked)

    # public methods
    def refresh(self):
        self.currentPage = 1
        self.totalPages = 1
        
        self.comboBoxOrganizationName.setCurrentText(f"{self.organizationData['organizationName']}")
        self._populateTableWidgetData()

    # private methods
    def _onPushButtonFilterClicked(self):
        self.currentPage = 1
        self._populateTableWidgetData()

    def _onPushButtonPrevClicked(self):
        if self.currentPage > 1:
            self.currentPage -= 1
            self._populateTableWidgetData()
            
    def _onPushButtonNextClicked(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
            self._populateTableWidgetData()
        
    def _onPushButtonClearClicked(self):
        self.lineEditUserName.setText("")
        self.lineEditAccessCode.setText("")
        self.lineEditFullName.setText("")
        self.lineEditMobileNumber.setText("")
        pass
        
        
    def _onPushButtonAddClicked(self):
        self.loading.show()
        self.currentThread = RegisterThread('registerUser', {
            'organizationName': self.comboBoxOrganizationName.currentText(),
            'userName': self.lineEditUserName.text(),
            'accessCode': self.lineEditAccessCode.text(),
            'fullName': self.lineEditFullName.text().upper(),
            'birthDate': self.dateEditBirthDate.text(),
            'mobileNumber': self.lineEditMobileNumber.text(),
            'accessLevel': self.comboBoxAccessLevel.currentText(),
        })
        self.currentThread.finished.connect(self._handleOnPushButtonAddClickedFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonAddClickedFinished(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Success', f"{result['message']}")
        self._populateTableWidgetData()
        return
        
        
    def _populateTableWidgetData(self):
        self.loading.show()
        self.currentThread = FetchThread('fetchAllUserDataByKeywordInPagination', {
            'organizationName': self.organizationData['organizationName'],
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text().upper()}",
        })
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataFinished)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.finished.connect(self.loading.close)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePopulateTableWidgetDataFinished(self, result):
        dictData = result['dictData']
        listData = result['listData']
        
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(listData))
        
        self.totalPages = dictData['totalPages'] if 'totalPages' in dictData else 1
        
        for i, data in enumerate(listData):
            manageActionButton = ManageActionButton(edit=True, delete=True)
            tableItems = [
                QTableWidgetItem(f"{data['userName']}"),
                QTableWidgetItem(f"{data['accessCode']}"),
                QTableWidgetItem(f"{data['fullName']}"),
                QTableWidgetItem(f"{data['birthDate']}"),
                QTableWidgetItem(f"{data['mobileNumber']}"),
                QTableWidgetItem(f"{data['accessLevel']}"),
                QTableWidgetItem(f"{data['updateTs']}"),
            ]
            
            self.tableWidgetData.setCellWidget(i, 0, manageActionButton)
            self.tableWidgetData.setItem(i, 1, tableItems[0])
            self.tableWidgetData.setItem(i, 2, tableItems[1])
            self.tableWidgetData.setItem(i, 3, tableItems[2])
            self.tableWidgetData.setItem(i, 4, tableItems[3])
            self.tableWidgetData.setItem(i, 5, tableItems[4])
            self.tableWidgetData.setItem(i, 6, tableItems[5])
            self.tableWidgetData.setItem(i, 7, tableItems[6])
        
            manageActionButton.pushButtonEdit.clicked.connect(lambda _, data=data: self._onPushButtonEditClicked(data))
            manageActionButton.pushButtonDelete.clicked.connect(lambda _, data=data: self._onPushButtonDeleteClicked(data))
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)
        pass
    def _onPushButtonEditClicked(self, data):
        self.editUser = EditUser(self.authData, data)
        self.editUser.exec()
        self._populateTableWidgetData()
        print('--data:', data)
        pass

    def _onPushButtonDeleteClicked(self, data):
        confirm = QMessageBox.warning(self, 'Confirm', f"Delete {data['userName']}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.loading.show()
            self.currentThread = RemoveThread('removeUserById', {'id': data['id']})
            self.currentThread.finished.connect(self._handleOnPushButtonDeleteClickedFinished)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.finished.connect(self.loading.close)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)

    def _handleOnPushButtonDeleteClickedFinished(self, result):
        QMessageBox.information(self, 'Success', f"{result['message']}")
        self.currentPage = 1
        self._populateTableWidgetData()

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
        
        event.accept() # for closing the window
        
        print('closed...')