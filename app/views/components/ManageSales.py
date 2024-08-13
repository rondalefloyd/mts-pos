import os, sys, logging, json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.config import *
from app.views.templates.ManageSales_ui import Ui_FormManageSales
from app.views.components.ManageActionButton import ManageActionButton
from app.views.components.PreOrder import PreOrder
from app.views.components.PreOrderActionButton import PreOrderActionButton
from app.views.components.Loading import Loading
from app.controllers.dedicated.fetch import FetchThread

class ManageSales(Ui_FormManageSales, QWidget):
    def __init__(self, userData):
        super().__init__()
        self.setupUi(self)
        
        self.loading = Loading()
        self.windowEvent = EVENT_NO_EVENT
        self.userData = userData
        self.currentThread = None
        self.activeThreads = []
        
        self.orderNumber = 0
        self.orderIndex = 0
        self.orderName = 'N/A'
        self.orderType = 'N/A'
        self.orderData = {
            'ongoing': [],
            'cancelled': [],
            'saved': [],
            'finished': [],
        }
        
        self.refresh()
        
        self.tabWidgetOrder.clear()
        
        self.tabWidgetOrder.tabCloseRequested.connect(self._onTabWidgetOrderTabCloseRequested)
        self.tabWidgetOrder.currentChanged.connect(self._onTabWidgetOrderCurrentChanged)
        self.pushButtonFilter.clicked.connect(self._onPushButtonFilterClicked)
        self.pushButtonPrev.clicked.connect(self._onPushButtonPrevClicked)
        self.pushButtonNext.clicked.connect(self._onPushButtonNextClicked)
        self.pushButtonNew.clicked.connect(self._onPushButtonNewClicked)

    def refresh(self):
        self.currentPage = 1
        self.totalPages = 1
        
        self._populateTableWidgetData()

    def _onTabWidgetOrderTabCloseRequested(self, index):
        orderOngoing = self.orderData['ongoing']
        self.orderData['cancelled'].append({
            'orderName': orderOngoing[index]['orderName'],
            'orderWidget': orderOngoing[index]['orderWidget'],
        })
        self.tabWidgetOrder.removeTab(index)
        orderOngoing.pop(index)
        
        print('self.orderData:', json.dumps(self.orderData, indent=4, default=str))

    def _onTabWidgetOrderCurrentChanged(self):
        self.orderIndex = self.tabWidgetOrder.currentIndex()
        self.labelOrderNumber.setText(self.orderData['ongoing'][self.orderIndex]['orderName'])
        pass
        # CONTINUE THIS

    def _onPushButtonNewClicked(self):
        self.preOrder = PreOrder(self)
        
        self.orderNumber += 1
        self.orderName = f"Order {self.orderNumber}"
        orderOngoing = self.orderData['ongoing']
        orderOngoing.append({
            'orderName': self.orderName,
            'orderWidget': self.preOrder,
        })
        
        self.orderIndex = len(orderOngoing) - 1
        
        orderWidget: PreOrder = self.orderData['ongoing'][self.orderIndex]['orderWidget']
        orderWidget.tableWidgetData.clearContents()
        self.tabWidgetOrder.addTab(orderWidget, self.orderName)
        self.tabWidgetOrder.setCurrentIndex(self.orderIndex)
        
        print('self.orderData:', json.dumps(self.orderData, indent=4, default=str))
        # CONTINUE THIS
    
    def _onOrderWidgetPushButtonDiscardClicked(self):
        self.orderIndex = self.tabWidgetOrder.currentIndex()
        self.tabWidgetOrder.removeTab(self.orderIndex)
        self.orderData['ongoing'].pop(self.orderIndex)
        
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
        
    def _populateTableWidgetData(self):
        # TODO: add fetcher for item displays
        self.currentThread = FetchThread('fetch_all_item_price_related_data_by_keyword_order_type_in_pagination', {
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text()}",
            'orderType': f"{self.orderType}",
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
            manageActionButton = ManageActionButton(add=True)
            tableItems = [
                QTableWidgetItem(f"{data['itemName']}"),
                QTableWidgetItem(f"{data['brandName']}"),
                QTableWidgetItem(f"{data['price']}"),
                QTableWidgetItem(f"{data['promoName']}"),
                QTableWidgetItem(f"{data['available']}"),
            ]
            
            self.tableWidgetData.setCellWidget(i, 0, manageActionButton)
            for j, tableitem in enumerate(tableItems):
                self.tableWidgetData.setItem(i, (j + 1), tableItems[j])
                
                if data['promoName'] is not None:
                    manageActionButton.pushButtonEdit.setVisible(False)
                    tableitem.setForeground(QColor(255, 0, 0))
        
            # TODO: add function
            manageActionButton.pushButtonAdd.clicked.connect(lambda _=i, data=data: self._onPushButtonAddClicked(data))
            
        self.labelPageIndicator.setText(f"{self.currentPage}/{self.totalPages}")
        self.pushButtonPrev.setEnabled(self.currentPage > 1)
        self.pushButtonNext.setEnabled(self.currentPage < self.totalPages)

    def _onPushButtonAddClicked(self, data):
        # TODO: create new method using array for getting the items added to cart
        
        self.orderIndex = self.tabWidgetOrder.currentIndex()
        orderWidget: PreOrder = self.orderData['ongoing'][self.orderIndex]['orderWidget']

        # TODO: fix indexing for rows
        rowCount = orderWidget.tableWidgetData.rowCount()
        orderWidget.tableWidgetData.insertRow(rowCount)
        orderWidget.tableWidgetData.setCellWidget(rowCount, 0, PreOrderActionButton())
        orderWidget.tableWidgetData.setItem(rowCount, 1, QTableWidgetItem(f"{data['itemName']}")) # the qty should be incremented
        orderWidget.tableWidgetData.setItem(rowCount, 2, QTableWidgetItem(f"{data['itemName']}"))
        orderWidget.tableWidgetData.setItem(rowCount, 3, QTableWidgetItem(f"{data['price']}")) # the price should be incremented
        
        print("orderWidget.tableWidgetData.rowCount():", orderWidget.tableWidgetData.rowCount())

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
