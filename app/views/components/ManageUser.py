# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.templates.ManageUser_ui import Ui_FormManageUser
from app.views.components.Loading import Loading
from app.views.components.ManageActionButton import ManageActionButton
from app.controllers.dedicated.fetch import FetchThread
from app.controllers.dedicated.register import RegisterThread
from app.controllers.dedicated.remove import RemoveThread

# class definition
class ManageUser(Ui_FormManageUser, QWidget):
    # initialization method (__init__)
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
            manageActionButton = ManageActionButton(delete=True)
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
        
            manageActionButton.pushButtonDelete.clicked.connect(lambda _=i, data=data: self._onPushButtonDeleteClicked(data))
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)
        pass

    def _onPushButtonDeleteClicked(self, data):
        confirm = QMessageBox.warning(self, 'Confirm', f"Delete {data['userName']}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.loading.show()
            self.currentThread = RemoveThread('pos/remove/user/id', {'id': f"{data['id']}"})
            self.currentThread.finished.connect(self._handleOnPushButtonDeleteClickedResult)
            self.currentThread.finished.connect(self._cleanupThread)
            self.currentThread.start()
            self.activeThreads.append(self.currentThread)

    def _handleOnPushButtonDeleteClickedResult(self, result):
        self.loading.close()
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
        
        event.accept()
        
        print('closed...')