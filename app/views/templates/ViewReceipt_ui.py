# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\ViewReceipt.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogViewReceipt(object):
    def setupUi(self, DialogViewReceipt):
        DialogViewReceipt.setObjectName("DialogViewReceipt")
        DialogViewReceipt.resize(699, 752)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogViewReceipt)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(DialogViewReceipt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtWidgets.QLabel(DialogViewReceipt)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.labelMemberName = QtWidgets.QLabel(DialogViewReceipt)
        self.labelMemberName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelMemberName.setObjectName("labelMemberName")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelMemberName)
        self.label_9 = QtWidgets.QLabel(DialogViewReceipt)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.labelMobileNumber = QtWidgets.QLabel(DialogViewReceipt)
        self.labelMobileNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelMobileNumber.setObjectName("labelMobileNumber")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelMobileNumber)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.tableWidgetData = QtWidgets.QTableWidget(DialogViewReceipt)
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
        self.tableWidgetData.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetData.horizontalHeader().setStretchLastSection(False)
        self.tableWidgetData.verticalHeader().setVisible(False)
        self.tableWidgetData.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetData.verticalHeader().setDefaultSectionSize(50)
        self.tableWidgetData.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidgetData)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(DialogViewReceipt)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.labelSubtotal = QtWidgets.QLabel(DialogViewReceipt)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelSubtotal.setFont(font)
        self.labelSubtotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSubtotal.setObjectName("labelSubtotal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelSubtotal)
        self.label_2 = QtWidgets.QLabel(DialogViewReceipt)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.labelDiscount = QtWidgets.QLabel(DialogViewReceipt)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelDiscount.setFont(font)
        self.labelDiscount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDiscount.setObjectName("labelDiscount")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelDiscount)
        self.label_3 = QtWidgets.QLabel(DialogViewReceipt)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.labelTax = QtWidgets.QLabel(DialogViewReceipt)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelTax.setFont(font)
        self.labelTax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTax.setObjectName("labelTax")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelTax)
        self.label_4 = QtWidgets.QLabel(DialogViewReceipt)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.labelGrandTotal = QtWidgets.QLabel(DialogViewReceipt)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelGrandTotal.setFont(font)
        self.labelGrandTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelGrandTotal.setObjectName("labelGrandTotal")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelGrandTotal)
        self.verticalLayout.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(DialogViewReceipt)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(DialogViewReceipt)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.labelAmount = QtWidgets.QLabel(DialogViewReceipt)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelAmount.setFont(font)
        self.labelAmount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelAmount.setObjectName("labelAmount")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelAmount)
        self.label_8 = QtWidgets.QLabel(DialogViewReceipt)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.labelChange = QtWidgets.QLabel(DialogViewReceipt)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelChange.setFont(font)
        self.labelChange.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelChange.setObjectName("labelChange")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelChange)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonClose = QtWidgets.QPushButton(DialogViewReceipt)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout.addWidget(self.pushButtonClose)
        self.pushButtonPrint = QtWidgets.QPushButton(DialogViewReceipt)
        self.pushButtonPrint.setObjectName("pushButtonPrint")
        self.horizontalLayout.addWidget(self.pushButtonPrint)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogViewReceipt)
        QtCore.QMetaObject.connectSlotsByName(DialogViewReceipt)

    def retranslateUi(self, DialogViewReceipt):
        _translate = QtCore.QCoreApplication.translate
        DialogViewReceipt.setWindowTitle(_translate("DialogViewReceipt", "view receipt"))
        self.label_6.setText(_translate("DialogViewReceipt", "MTS POS"))
        self.label_5.setText(_translate("DialogViewReceipt", "Member name"))
        self.labelMemberName.setText(_translate("DialogViewReceipt", "<MemberName>"))
        self.label_9.setText(_translate("DialogViewReceipt", "Mobile number"))
        self.labelMobileNumber.setText(_translate("DialogViewReceipt", "<MobileNumber>"))
        self.tableWidgetData.setSortingEnabled(False)
        item = self.tableWidgetData.verticalHeaderItem(0)
        item.setText(_translate("DialogViewReceipt", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(1)
        item.setText(_translate("DialogViewReceipt", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(2)
        item.setText(_translate("DialogViewReceipt", "New Row"))
        item = self.tableWidgetData.horizontalHeaderItem(0)
        item.setText(_translate("DialogViewReceipt", "Action"))
        item = self.tableWidgetData.horizontalHeaderItem(1)
        item.setText(_translate("DialogViewReceipt", "ItemName"))
        item = self.tableWidgetData.horizontalHeaderItem(2)
        item.setText(_translate("DialogViewReceipt", "Quantity"))
        item = self.tableWidgetData.horizontalHeaderItem(3)
        item.setText(_translate("DialogViewReceipt", "Total"))
        item = self.tableWidgetData.horizontalHeaderItem(4)
        item.setText(_translate("DialogViewReceipt", "VoidReason"))
        item = self.tableWidgetData.horizontalHeaderItem(5)
        item.setText(_translate("DialogViewReceipt", "VoidStatus"))
        item = self.tableWidgetData.horizontalHeaderItem(6)
        item.setText(_translate("DialogViewReceipt", "UpdateTs"))
        self.label.setText(_translate("DialogViewReceipt", "Subtotal"))
        self.labelSubtotal.setText(_translate("DialogViewReceipt", "<Subtotal>"))
        self.label_2.setText(_translate("DialogViewReceipt", "Discount"))
        self.labelDiscount.setText(_translate("DialogViewReceipt", "<Discount>"))
        self.label_3.setText(_translate("DialogViewReceipt", "VAT"))
        self.labelTax.setText(_translate("DialogViewReceipt", "<Tax>"))
        self.label_4.setText(_translate("DialogViewReceipt", "Grand total"))
        self.labelGrandTotal.setText(_translate("DialogViewReceipt", "<GrandTotal>"))
        self.label_7.setText(_translate("DialogViewReceipt", "Amount"))
        self.labelAmount.setText(_translate("DialogViewReceipt", "<Amount>"))
        self.label_8.setText(_translate("DialogViewReceipt", "Change"))
        self.labelChange.setText(_translate("DialogViewReceipt", "<Change>"))
        self.pushButtonClose.setText(_translate("DialogViewReceipt", "Close"))
        self.pushButtonPrint.setText(_translate("DialogViewReceipt", "Print"))
