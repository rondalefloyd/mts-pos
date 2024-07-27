
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.ManageUser_ui import Ui_FormManageUser
from app.views.components.Loading import Loading
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread

class ManageUser(Ui_FormManageUser, QWidget):
    def __init__(self, userData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = 'no-event'
        self.userData = userData
        self.currentThread = None
        self.activeThreads = []
        
        self.currentPage = 1
        self.totalPages = 1
        
        self.pushButtonFilter.clicked.connect(self._onPushButtonFilterClicked)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)
        self.pushButtonClear.clicked.connect(self._onPushButtonClearClicked)
        self.pushButtonAdd.clicked.connect(self._onPushButtonAddClicked)
        
        self._populateTableWidgetData()
        self._populateComboBoxOrganizationName()

    def _onPushButtonFilterClicked(self):
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
        self.currentThread = RegisterThread('pos/register/user', {
            'organizationName': f"{self.comboBoxOrganizationName.currentText()}".upper(),
            'userName': f"{self.lineEditUserName.text()}",
            'accessCode': f"{self.lineEditAccessCode.text()}",
            'fullName': f"{self.lineEditFullName.text()}".upper(),
            'birthDate': f"{self.dateEditBirthDate.text()}",
            'mobileNumber': f"{self.lineEditMobileNumber.text()}",
            'accessLevel': f"{self.comboBoxAccessLevel.currentText()}",
        })
        self.currentThread.finished.connect(self._handleOnPushButtonAddClickedResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)
        
    def _handleOnPushButtonAddClickedResult(self, result):
        self.loading.close()
        
        if result['success'] is False:
            QMessageBox.critical(self, 'Invalid', f"{result['message']}")
            return
            
        QMessageBox.information(self, 'Success', f"{result['message']}")
        self._populateTableWidgetData()
        return
        
    def _populateComboBoxOrganizationName(self):
        self.loading.show()
        self.currentThread = FetchThread('pos/fetch/organization/all')
        self.currentThread.finished.connect(self._handlePopulateComboBoxOrganizationNameResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePopulateComboBoxOrganizationNameResult(self, result):
        self.loading.close()
        
        for data in result['data']:
            self.comboBoxOrganizationName.addItem(f"{data['organizationName']}")
        
    def _populateTableWidgetData(self):
        self.loading.show()
        self.currentThread = FetchThread('pos/fetch/user/all/keyword/paginated', {
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text()}",
        })
        self.currentThread.finished.connect(self._handlePopulateTableWidgetDataResult)
        self.currentThread.finished.connect(self._cleanupThread)
        self.currentThread.start()
        self.activeThreads.append(self.currentThread)

    def _handlePopulateTableWidgetDataResult(self, result):
        self.loading.close()
        self.tableWidgetData.clearContents()
        self.tableWidgetData.setRowCount(len(result['data']))
        
        self.totalPages = result['totalPages']
        
        for i, data in enumerate(result['data']):
            self.tableWidgetData.setItem(i, 1, QTableWidgetItem(f"{data['userName']}"))
            self.tableWidgetData.setItem(i, 2, QTableWidgetItem(f"{data['accessCode']}"))
            self.tableWidgetData.setItem(i, 3, QTableWidgetItem(f"{data['fullName']}"))
            self.tableWidgetData.setItem(i, 4, QTableWidgetItem(f"{data['birthDate']}"))
            self.tableWidgetData.setItem(i, 5, QTableWidgetItem(f"{data['mobileNumber']}"))
            self.tableWidgetData.setItem(i, 6, QTableWidgetItem(f"{data['accessLevel']}"))
            self.tableWidgetData.setItem(i, 7, QTableWidgetItem(f"{data['updateTs']}"))
        
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)
        pass

    def _cleanupThread(self):
        sender = self.sender()
        if sender in self.activeThreads:
            self.activeThreads.remove(sender)
        self.currentThread = None
        print('active threads:', self.activeThreads)

    def closeEvent(self, event):
        for thread in self.activeThreads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        
        self.activeThreads.clear()
        
        event.accept()
        
        print('closed...')