# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.config import *
from app.views.templates.ManageMember_ui import Ui_FormManageMember
from app.views.components.Loading import Loading
from app.views.components.EditMember import EditMember
from app.views.components.ManageActionButton import ManageActionButton
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread
from app.controllers.common.validator import (
    mobileNumberValidator,
    addressFormatValidator,
    customNameValidator,
)

# class definition
class ManageMember(Ui_FormManageMember, QWidget):
    # initialization method (__init__)
    def __init__(self, userData):
        super().__init__()
        self.setupUi(self)
        
        self.mobileNumberValidator = QRegExpValidator(QRegExp(r'^\d{11}$'))
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.userData = userData
        self.currentThread = None
        self.activeThreads = []
        
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
        
        self.comboBoxOrganizationName.setCurrentText(f"{self.userData['organizationName']}")
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
        self.currentThread = RegisterThread('register_member', {
            'organizationName': self.comboBoxOrganizationName.currentText().upper(),
            'memberName': self.lineEditMemberName.text().upper(),
            'birthDate': self.dateEditBirthDate.text(),
            'address': self.lineEditAddress.text().upper(),
            'mobileNumber': self.lineEditMobileNumber.text(),
            'points': 0,  # Assuming new members start with 0 points
        })
        self.currentThread.finished.connect(self._handleOnPushButtonAddClickedResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonAddClickedResult(self, result):
        if result['success'] is False:
            QMessageBox.critical(self, 'Error', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Success', f"{result['message']}")
        self._populateTableWidgetData()
        return
        
        
    def _populateTableWidgetData(self):
        self.currentThread = FetchThread('fetch_all_member_data_by_keyword_in_pagination', {
            'organizationName': self.userData['organizationName'],
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text()}",
        })
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePopulateTableWidgetDataResult(self, result):
        oneData = result['dictData']
        manyData = result['listData']
        
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(manyData))
        
        self.totalPages = oneData['totalPages'] if 'totalPages' in oneData else 1
        
        for i, data in enumerate(manyData):
            manageActionButton = ManageActionButton(edit=True, delete=True)
            tableItems = [
                QTableWidgetItem(f"{data['memberName']}"),
                QTableWidgetItem(f"{data['birthDate']}"),
                QTableWidgetItem(f"{data['address']}"),
                QTableWidgetItem(f"{data['mobileNumber']}"),
                QTableWidgetItem(f"{data['points']}"),
                QTableWidgetItem(f"{data['updateTs']}"),
            ]
            
            self.tableWidgetData.setCellWidget(i, 0, manageActionButton)
            self.tableWidgetData.setItem(i, 1, tableItems[0])
            self.tableWidgetData.setItem(i, 2, tableItems[1])
            self.tableWidgetData.setItem(i, 3, tableItems[2])
            self.tableWidgetData.setItem(i, 4, tableItems[3])
            self.tableWidgetData.setItem(i, 5, tableItems[4])
            self.tableWidgetData.setItem(i, 6, tableItems[5])
        
            manageActionButton.pushButtonEdit.clicked.connect(lambda _=i, data=data: self._onPushButtonEditClicked(data))
            manageActionButton.pushButtonDelete.clicked.connect(lambda _, data=data: self._onPushButtonDeleteClicked(data))
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)

    def _onPushButtonEditClicked(self, data):
        self.editMember = EditMember(self.userData, data)
        self.editMember.exec()
        self._populateTableWidgetData()

    def _onPushButtonDeleteClicked(self, data):
        confirm = QMessageBox.warning(self, 'Confirm', f"Delete {data['memberName']}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.currentThread = RemoveThread('remove_member_by_id', {'id': data['id']})
            self.currentThread.finished.connect(self._handleOnPushButtonDeleteClickedResult)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)

    def _handleOnPushButtonDeleteClickedResult(self, result):
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