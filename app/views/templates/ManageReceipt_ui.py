# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/templates/generated\ManageReceipt.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_FormManageReceipt(object):
    def setupUi(self, FormManageReceipt):
        FormManageReceipt.setObjectName("FormManageReceipt")
        FormManageReceipt.resize(665, 629)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(FormManageReceipt)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditFilter = QtWidgets.QLineEdit(FormManageReceipt)
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout.addWidget(self.lineEditFilter)
        self.pushButtonFilter = QtWidgets.QPushButton(FormManageReceipt)
        self.pushButtonFilter.setObjectName("pushButtonFilter")
        self.horizontalLayout.addWidget(self.pushButtonFilter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgetData = QtWidgets.QTableWidget(FormManageReceipt)
        self.tableWidgetData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetData.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setShowGrid(False)
        self.tableWidgetData.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetData.setWordWrap(False)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(11)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(10, item)
        self.tableWidgetData.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetData.verticalHeader().setVisible(False)
        self.tableWidgetData.verticalHeader().setDefaultSectionSize(50)
        self.tableWidgetData.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidgetData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonPrev = QtWidgets.QPushButton(FormManageReceipt)
        self.pushButtonPrev.setEnabled(False)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout_2.addWidget(self.pushButtonPrev)
        self.labelPageIndicator = QtWidgets.QLabel(FormManageReceipt)
        self.labelPageIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPageIndicator.setObjectName("labelPageIndicator")
        self.horizontalLayout_2.addWidget(self.labelPageIndicator)
        self.pushButtonNext = QtWidgets.QPushButton(FormManageReceipt)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(FormManageReceipt)
        QtCore.QMetaObject.connectSlotsByName(FormManageReceipt)

    def retranslateUi(self, FormManageReceipt):
        _translate = QtCore.QCoreApplication.translate
        FormManageReceipt.setWindowTitle(_translate("FormManageReceipt", "Manage receipt"))
        self.pushButtonFilter.setText(_translate("FormManageReceipt", "Filter"))
        self.tableWidgetData.setSortingEnabled(False)
        item = self.tableWidgetData.verticalHeaderItem(0)
        item.setText(_translate("FormManageReceipt", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(1)
        item.setText(_translate("FormManageReceipt", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(2)
        item.setText(_translate("FormManageReceipt", "New Row"))
        item = self.tableWidgetData.horizontalHeaderItem(0)
        item.setText(_translate("FormManageReceipt", "Action"))
        item = self.tableWidgetData.horizontalHeaderItem(1)
        item.setText(_translate("FormManageReceipt", "OrderName"))
        item = self.tableWidgetData.horizontalHeaderItem(2)
        item.setText(_translate("FormManageReceipt", "OrderTypeName"))
        item = self.tableWidgetData.horizontalHeaderItem(3)
        item.setText(_translate("FormManageReceipt", "ReferenceId"))
        item = self.tableWidgetData.horizontalHeaderItem(4)
        item.setText(_translate("FormManageReceipt", "UserName"))
        item = self.tableWidgetData.horizontalHeaderItem(5)
        item.setText(_translate("FormManageReceipt", "MemberName"))
        item = self.tableWidgetData.horizontalHeaderItem(6)
        item.setText(_translate("FormManageReceipt", "PurchaseDate"))
        item = self.tableWidgetData.horizontalHeaderItem(7)
        item.setText(_translate("FormManageReceipt", "GrandTotal"))
        item = self.tableWidgetData.horizontalHeaderItem(8)
        item.setText(_translate("FormManageReceipt", "Payment"))
        item = self.tableWidgetData.horizontalHeaderItem(9)
        item.setText(_translate("FormManageReceipt", "Change"))
        item = self.tableWidgetData.horizontalHeaderItem(10)
        item.setText(_translate("FormManageReceipt", "UpdateTs"))
        self.pushButtonPrev.setText(_translate("FormManageReceipt", "Prev"))
        self.labelPageIndicator.setText(_translate("FormManageReceipt", "<CurrentPage>/<TotalPage>"))
        self.pushButtonNext.setText(_translate("FormManageReceipt", "Next"))
