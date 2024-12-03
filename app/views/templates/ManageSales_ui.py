# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/templates/generated\ManageSales.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_FormManageSales(object):
    def setupUi(self, FormManageSales):
        FormManageSales.setObjectName("FormManageSales")
        FormManageSales.resize(973, 382)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(FormManageSales)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditFilter = QtWidgets.QLineEdit(FormManageSales)
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout.addWidget(self.lineEditFilter)
        self.pushButtonFilter = QtWidgets.QPushButton(FormManageSales)
        self.pushButtonFilter.setObjectName("pushButtonFilter")
        self.horizontalLayout.addWidget(self.pushButtonFilter)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditBarcode = QtWidgets.QLineEdit(FormManageSales)
        self.lineEditBarcode.setEnabled(False)
        self.lineEditBarcode.setObjectName("lineEditBarcode")
        self.horizontalLayout_4.addWidget(self.lineEditBarcode)
        self.comboBoxBarcodeFilter = QtWidgets.QComboBox(FormManageSales)
        self.comboBoxBarcodeFilter.setEnabled(False)
        self.comboBoxBarcodeFilter.setObjectName("comboBoxBarcodeFilter")
        self.comboBoxBarcodeFilter.addItem("")
        self.comboBoxBarcodeFilter.addItem("")
        self.comboBoxBarcodeFilter.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxBarcodeFilter)
        self.pushButtonAdd = QtWidgets.QPushButton(FormManageSales)
        self.pushButtonAdd.setEnabled(False)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout_4.addWidget(self.pushButtonAdd)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tableWidgetData = QtWidgets.QTableWidget(FormManageSales)
        self.tableWidgetData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetData.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setShowGrid(False)
        self.tableWidgetData.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetData.setWordWrap(False)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(7)
        self.tableWidgetData.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(6, item)
        self.tableWidgetData.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetData.horizontalHeader().setHighlightSections(False)
        self.tableWidgetData.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetData.verticalHeader().setVisible(False)
        self.tableWidgetData.verticalHeader().setDefaultSectionSize(50)
        self.tableWidgetData.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidgetData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonPrev = QtWidgets.QPushButton(FormManageSales)
        self.pushButtonPrev.setEnabled(False)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout_2.addWidget(self.pushButtonPrev)
        self.labelPageIndicator = QtWidgets.QLabel(FormManageSales)
        self.labelPageIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPageIndicator.setObjectName("labelPageIndicator")
        self.horizontalLayout_2.addWidget(self.labelPageIndicator)
        self.pushButtonNext = QtWidgets.QPushButton(FormManageSales)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.frameOrder = QtWidgets.QFrame(FormManageSales)
        self.frameOrder.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frameOrder.setObjectName("frameOrder")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameOrder)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.frameOrder)
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelOrderName = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelOrderName.setFont(font)
        self.labelOrderName.setObjectName("labelOrderName")
        self.horizontalLayout_7.addWidget(self.labelOrderName)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.comboBoxOrderType = QtWidgets.QComboBox(self.widget)
        self.comboBoxOrderType.setObjectName("comboBoxOrderType")
        self.comboBoxOrderType.addItem("")
        self.comboBoxOrderType.addItem("")
        self.comboBoxOrderType.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBoxOrderType)
        self.pushButtonNew = QtWidgets.QPushButton(self.widget)
        self.pushButtonNew.setObjectName("pushButtonNew")
        self.horizontalLayout_7.addWidget(self.pushButtonNew)
        self.verticalLayout_2.addWidget(self.widget)
        self.tabWidgetOrder = QtWidgets.QTabWidget(self.frameOrder)
        self.tabWidgetOrder.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidgetOrder.setDocumentMode(False)
        self.tabWidgetOrder.setTabsClosable(True)
        self.tabWidgetOrder.setObjectName("tabWidgetOrder")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidgetOrder.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidgetOrder.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidgetOrder)
        self.horizontalLayout_6.addWidget(self.frameOrder)

        self.retranslateUi(FormManageSales)
        self.tabWidgetOrder.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FormManageSales)

    def retranslateUi(self, FormManageSales):
        _translate = QtCore.QCoreApplication.translate
        FormManageSales.setWindowTitle(_translate("FormManageSales", "Manage sales"))
        self.pushButtonFilter.setText(_translate("FormManageSales", "Filter"))
        self.comboBoxBarcodeFilter.setItemText(0, _translate("FormManageSales", "Retail"))
        self.comboBoxBarcodeFilter.setItemText(1, _translate("FormManageSales", "Wholesale"))
        self.comboBoxBarcodeFilter.setItemText(2, _translate("FormManageSales", "Mixed"))
        self.pushButtonAdd.setText(_translate("FormManageSales", "Add"))
        self.tableWidgetData.setSortingEnabled(False)
        item = self.tableWidgetData.verticalHeaderItem(0)
        item.setText(_translate("FormManageSales", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(1)
        item.setText(_translate("FormManageSales", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(2)
        item.setText(_translate("FormManageSales", "New Row"))
        item = self.tableWidgetData.horizontalHeaderItem(0)
        item.setText(_translate("FormManageSales", "Action"))
        item = self.tableWidgetData.horizontalHeaderItem(1)
        item.setText(_translate("FormManageSales", "ItemName"))
        item = self.tableWidgetData.horizontalHeaderItem(2)
        item.setText(_translate("FormManageSales", "Barcode"))
        item = self.tableWidgetData.horizontalHeaderItem(3)
        item.setText(_translate("FormManageSales", "Brand"))
        item = self.tableWidgetData.horizontalHeaderItem(4)
        item.setText(_translate("FormManageSales", "Price"))
        item = self.tableWidgetData.horizontalHeaderItem(5)
        item.setText(_translate("FormManageSales", "Available"))
        item = self.tableWidgetData.horizontalHeaderItem(6)
        item.setText(_translate("FormManageSales", "PromoName"))
        self.pushButtonPrev.setText(_translate("FormManageSales", "Prev"))
        self.labelPageIndicator.setText(_translate("FormManageSales", "<CurrentPage>/<TotalPage>"))
        self.pushButtonNext.setText(_translate("FormManageSales", "Next"))
        self.labelOrderName.setText(_translate("FormManageSales", "<OrderName>"))
        self.comboBoxOrderType.setItemText(0, _translate("FormManageSales", "Retail"))
        self.comboBoxOrderType.setItemText(1, _translate("FormManageSales", "Wholesale"))
        self.comboBoxOrderType.setItemText(2, _translate("FormManageSales", "Mixed"))
        self.pushButtonNew.setText(_translate("FormManageSales", "New"))
        self.tabWidgetOrder.setTabText(self.tabWidgetOrder.indexOf(self.tab), _translate("FormManageSales", "Tab 1"))
        self.tabWidgetOrder.setTabText(self.tabWidgetOrder.indexOf(self.tab_2), _translate("FormManageSales", "Tab 2"))
