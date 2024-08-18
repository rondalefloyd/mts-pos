# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\PreOrder.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormPreOrder(object):
    def setupUi(self, FormPreOrder):
        FormPreOrder.setObjectName("FormPreOrder")
        FormPreOrder.resize(658, 650)
        self.verticalLayout = QtWidgets.QVBoxLayout(FormPreOrder)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelOrderType = QtWidgets.QLabel(FormPreOrder)
        self.labelOrderType.setObjectName("labelOrderType")
        self.horizontalLayout_2.addWidget(self.labelOrderType)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonClear = QtWidgets.QPushButton(FormPreOrder)
        self.pushButtonClear.setEnabled(False)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_2.addWidget(self.pushButtonClear)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidgetData = QtWidgets.QTableWidget(FormPreOrder)
        self.tableWidgetData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(4)
        self.tableWidgetData.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(3, item)
        self.tableWidgetData.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetData.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidgetData)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(FormPreOrder)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.labelSubtotal = QtWidgets.QLabel(FormPreOrder)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelSubtotal.setFont(font)
        self.labelSubtotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSubtotal.setObjectName("labelSubtotal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelSubtotal)
        self.label_2 = QtWidgets.QLabel(FormPreOrder)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.labelDiscount = QtWidgets.QLabel(FormPreOrder)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelDiscount.setFont(font)
        self.labelDiscount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDiscount.setObjectName("labelDiscount")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelDiscount)
        self.label_3 = QtWidgets.QLabel(FormPreOrder)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.labelTax = QtWidgets.QLabel(FormPreOrder)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelTax.setFont(font)
        self.labelTax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTax.setObjectName("labelTax")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelTax)
        self.label_4 = QtWidgets.QLabel(FormPreOrder)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.labelGrandTotal = QtWidgets.QLabel(FormPreOrder)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelGrandTotal.setFont(font)
        self.labelGrandTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelGrandTotal.setObjectName("labelGrandTotal")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelGrandTotal)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonDiscard = QtWidgets.QPushButton(FormPreOrder)
        self.pushButtonDiscard.setObjectName("pushButtonDiscard")
        self.horizontalLayout.addWidget(self.pushButtonDiscard)
        self.pushButtonPark = QtWidgets.QPushButton(FormPreOrder)
        self.pushButtonPark.setObjectName("pushButtonPark")
        self.horizontalLayout.addWidget(self.pushButtonPark)
        self.pushButtonPay = QtWidgets.QPushButton(FormPreOrder)
        self.pushButtonPay.setEnabled(False)
        self.pushButtonPay.setObjectName("pushButtonPay")
        self.horizontalLayout.addWidget(self.pushButtonPay)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(FormPreOrder)
        QtCore.QMetaObject.connectSlotsByName(FormPreOrder)

    def retranslateUi(self, FormPreOrder):
        _translate = QtCore.QCoreApplication.translate
        FormPreOrder.setWindowTitle(_translate("FormPreOrder", "Form"))
        self.labelOrderType.setText(_translate("FormPreOrder", "<OrderType>"))
        self.pushButtonClear.setText(_translate("FormPreOrder", "Clear"))
        self.tableWidgetData.setSortingEnabled(False)
        item = self.tableWidgetData.horizontalHeaderItem(0)
        item.setText(_translate("FormPreOrder", "Action"))
        item = self.tableWidgetData.horizontalHeaderItem(1)
        item.setText(_translate("FormPreOrder", "Qty."))
        item = self.tableWidgetData.horizontalHeaderItem(2)
        item.setText(_translate("FormPreOrder", "ItemName"))
        item = self.tableWidgetData.horizontalHeaderItem(3)
        item.setText(_translate("FormPreOrder", "Total"))
        self.label.setText(_translate("FormPreOrder", "Subtotal"))
        self.labelSubtotal.setText(_translate("FormPreOrder", "<Subtotal>"))
        self.label_2.setText(_translate("FormPreOrder", "Discount"))
        self.labelDiscount.setText(_translate("FormPreOrder", "<Discount>"))
        self.label_3.setText(_translate("FormPreOrder", "VAT"))
        self.labelTax.setText(_translate("FormPreOrder", "<Tax>"))
        self.label_4.setText(_translate("FormPreOrder", "Grand total"))
        self.labelGrandTotal.setText(_translate("FormPreOrder", "<GrandTotal>"))
        self.pushButtonDiscard.setText(_translate("FormPreOrder", "Discard"))
        self.pushButtonPark.setText(_translate("FormPreOrder", "Park"))
        self.pushButtonPay.setText(_translate("FormPreOrder", "Pay"))
