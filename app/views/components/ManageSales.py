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
        
        self.orderIndex = 0
        self.orderNumber = 0
        self.orderName = "N/A"
        self.activeOrder = []
        self.parkedOrder = []
        
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

    def _onTabWidgetOrderTabCloseRequested(self, index): # TODO: do this
        self.tabWidgetOrder.removeTab(index)
        self.activeOrder.pop(index)
        print('self.activeOrder:', json.dumps(self.activeOrder, indent=4, default=str))

    def _onTabWidgetOrderCurrentChanged(self): # TODO: do this
        self.orderIndex = self.tabWidgetOrder.currentIndex()
        pass

    def _onPushButtonNewClicked(self): # TODO: do this
        self.orderNumber += 1
        self.orderName = f"Order {self.orderNumber}"
        
        self.activeOrder.append({
            'orderName': f"{self.orderName}", 
            'orderType': f"{self.comboBoxOrderType.currentText()}",
            'orderItem': [], 
            'orderWidget': PreOrder(self),
        })
        
        self.orderIndex = len(self.activeOrder) - 1
        
        self.tabWidgetOrder.addTab(
            self.activeOrder[self.orderIndex]['orderWidget'], 
            self.activeOrder[self.orderIndex]['orderName'],
        )
        
        self.tabWidgetOrder.setCurrentIndex(self.orderIndex)
        
        print('self.activeOrder:', json.dumps(self.activeOrder, indent=4, default=str))
    
    def _onOrderWidgetPushButtonDiscardClicked(self):
        self._onTabWidgetOrderTabCloseRequested(self.orderIndex)
        
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
        # TODO: fix this FetchThread where it should filter depending on the order type (retail/wholesale/mixed)
        self.currentThread = FetchThread('fetch_all_item_price_related_data_by_keyword_order_type_in_pagination', {
            'currentPage': self.currentPage,
            'keyword': f"{self.lineEditFilter.text()}",
            # 'orderType': f"{self.orderType}",
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
                QTableWidgetItem(f"{data['available']}"),
                QTableWidgetItem(f"{data['promoName']}"),
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

    def _onPushButtonAddClicked(self, data): # TODO: do this
        print('you are here data:', data)
        itemId = data['itemId']
        itemName = data['itemName']
        promoName = data['promoName']
        price = data['price']
        discount = data['discount']
        available = data['available']
        stockBypass = False
        
        orderItem = self.activeOrder[self.orderIndex]['orderItem']
        orderWidget: PreOrder = self.activeOrder[self.orderIndex]['orderWidget']
        isItemExist = False
        
        # TODO: make a clean method of this instead of too much nested if else
        for item in orderItem:
            if item['itemId'] == itemId:
                if item['stockBypass'] is False and available is not None:
                    if item['quantity'] >= available:
                        confirm = QMessageBox.warning(self, 'Error', "Item out of stock. Bypass stock?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                        
                        if confirm == QMessageBox.StandardButton.Yes:
                            item['stockBypass'] = True
                        if confirm == QMessageBox.StandardButton.No:
                            return
                
                item['quantity'] += 1
                item['total'] += price
                isItemExist = True
                break
        
        if not isItemExist:
            orderItem.append({
                'itemId': itemId,
                'price': price,
                'discount': discount,
                'available': available,
                'stockBypass': stockBypass,
                
                'quantity': 1,
                'itemName': itemName,
                'promoName': promoName,
                'total': price,
            })
        
        orderWidget.populateTableWidgetData(orderItem)
        
        print('orderItem:', json.dumps(orderItem, indent=4, default=str))

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
