# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\InOrder.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogInOrder(object):
    def setupUi(self, DialogInOrder):
        DialogInOrder.setObjectName("DialogInOrder")
        DialogInOrder.resize(922, 567)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(DialogInOrder)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidgetData = QtWidgets.QTableWidget(DialogInOrder)
        self.tableWidgetData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(4)
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
        self.tableWidgetData.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetData.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidgetData)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(DialogInOrder)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.labelSubtotal = QtWidgets.QLabel(DialogInOrder)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelSubtotal.setFont(font)
        self.labelSubtotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSubtotal.setObjectName("labelSubtotal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelSubtotal)
        self.label_2 = QtWidgets.QLabel(DialogInOrder)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.labelDiscount = QtWidgets.QLabel(DialogInOrder)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelDiscount.setFont(font)
        self.labelDiscount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDiscount.setObjectName("labelDiscount")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelDiscount)
        self.label_3 = QtWidgets.QLabel(DialogInOrder)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.labelTax = QtWidgets.QLabel(DialogInOrder)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelTax.setFont(font)
        self.labelTax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTax.setObjectName("labelTax")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelTax)
        self.label_5 = QtWidgets.QLabel(DialogInOrder)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.labelCustomDiscount = QtWidgets.QLabel(DialogInOrder)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelCustomDiscount.setFont(font)
        self.labelCustomDiscount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCustomDiscount.setObjectName("labelCustomDiscount")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelCustomDiscount)
        self.label_4 = QtWidgets.QLabel(DialogInOrder)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.labelGrandTotal = QtWidgets.QLabel(DialogInOrder)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelGrandTotal.setFont(font)
        self.labelGrandTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelGrandTotal.setObjectName("labelGrandTotal")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.labelGrandTotal)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(DialogInOrder)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(DialogInOrder)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEditMemberName = QtWidgets.QLineEdit(DialogInOrder)
        self.lineEditMemberName.setEnabled(False)
        self.lineEditMemberName.setObjectName("lineEditMemberName")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditMemberName)
        self.label_9 = QtWidgets.QLabel(DialogInOrder)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEditMobileNumber = QtWidgets.QLineEdit(DialogInOrder)
        self.lineEditMobileNumber.setEnabled(False)
        self.lineEditMobileNumber.setObjectName("lineEditMobileNumber")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditMobileNumber)
        self.label_11 = QtWidgets.QLabel(DialogInOrder)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEditPoints = QtWidgets.QLineEdit(DialogInOrder)
        self.lineEditPoints.setEnabled(False)
        self.lineEditPoints.setObjectName("lineEditPoints")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditPoints)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.line_3 = QtWidgets.QFrame(DialogInOrder)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(DialogInOrder)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEditCash = QtWidgets.QLineEdit(DialogInOrder)
        self.lineEditCash.setObjectName("lineEditCash")
        self.horizontalLayout_2.addWidget(self.lineEditCash)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonKeySix = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeySix.sizePolicy().hasHeightForWidth())
        self.pushButtonKeySix.setSizePolicy(sizePolicy)
        self.pushButtonKeySix.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeySix.setObjectName("pushButtonKeySix")
        self.gridLayout.addWidget(self.pushButtonKeySix, 1, 2, 1, 1)
        self.pushButtonKeyFive = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyFive.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyFive.setSizePolicy(sizePolicy)
        self.pushButtonKeyFive.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeyFive.setObjectName("pushButtonKeyFive")
        self.gridLayout.addWidget(self.pushButtonKeyFive, 1, 1, 1, 1)
        self.pushButtonKeyNine = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyNine.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyNine.setSizePolicy(sizePolicy)
        self.pushButtonKeyNine.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeyNine.setObjectName("pushButtonKeyNine")
        self.gridLayout.addWidget(self.pushButtonKeyNine, 2, 2, 1, 1)
        self.pushButtonKeySeven = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeySeven.sizePolicy().hasHeightForWidth())
        self.pushButtonKeySeven.setSizePolicy(sizePolicy)
        self.pushButtonKeySeven.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeySeven.setObjectName("pushButtonKeySeven")
        self.gridLayout.addWidget(self.pushButtonKeySeven, 2, 0, 1, 1)
        self.pushButtonKeyEight = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyEight.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyEight.setSizePolicy(sizePolicy)
        self.pushButtonKeyEight.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeyEight.setObjectName("pushButtonKeyEight")
        self.gridLayout.addWidget(self.pushButtonKeyEight, 2, 1, 1, 1)
        self.pushButtonKeyTwo = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyTwo.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyTwo.setSizePolicy(sizePolicy)
        self.pushButtonKeyTwo.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeyTwo.setObjectName("pushButtonKeyTwo")
        self.gridLayout.addWidget(self.pushButtonKeyTwo, 0, 1, 1, 1)
        self.pushButtonKeyThree = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyThree.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyThree.setSizePolicy(sizePolicy)
        self.pushButtonKeyThree.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeyThree.setObjectName("pushButtonKeyThree")
        self.gridLayout.addWidget(self.pushButtonKeyThree, 0, 2, 1, 1)
        self.pushButtonKeyFour = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyFour.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyFour.setSizePolicy(sizePolicy)
        self.pushButtonKeyFour.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeyFour.setObjectName("pushButtonKeyFour")
        self.gridLayout.addWidget(self.pushButtonKeyFour, 1, 0, 1, 1)
        self.pushButtonKeyOne = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyOne.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyOne.setSizePolicy(sizePolicy)
        self.pushButtonKeyOne.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeyOne.setObjectName("pushButtonKeyOne")
        self.gridLayout.addWidget(self.pushButtonKeyOne, 0, 0, 1, 1)
        self.pushButtonKeyDelete = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyDelete.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyDelete.setSizePolicy(sizePolicy)
        self.pushButtonKeyDelete.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeyDelete.setObjectName("pushButtonKeyDelete")
        self.gridLayout.addWidget(self.pushButtonKeyDelete, 3, 0, 1, 1)
        self.pushButtonKeyZero = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyZero.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyZero.setSizePolicy(sizePolicy)
        self.pushButtonKeyZero.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeyZero.setObjectName("pushButtonKeyZero")
        self.gridLayout.addWidget(self.pushButtonKeyZero, 3, 1, 1, 1)
        self.pushButtonKeyDecimal = QtWidgets.QPushButton(DialogInOrder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyDecimal.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyDecimal.setSizePolicy(sizePolicy)
        self.pushButtonKeyDecimal.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonKeyDecimal.setObjectName("pushButtonKeyDecimal")
        self.gridLayout.addWidget(self.pushButtonKeyDecimal, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(DialogInOrder)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_12 = QtWidgets.QLabel(DialogInOrder)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(DialogInOrder)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(DialogInOrder)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.labelCashShortage = QtWidgets.QLabel(DialogInOrder)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelCashShortage.setFont(font)
        self.labelCashShortage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCashShortage.setObjectName("labelCashShortage")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelCashShortage)
        self.label_6 = QtWidgets.QLabel(DialogInOrder)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_6)
        self.labelPointsShortage = QtWidgets.QLabel(DialogInOrder)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPointsShortage.setFont(font)
        self.labelPointsShortage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPointsShortage.setObjectName("labelPointsShortage")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelPointsShortage)
        self.labelHybridShortage = QtWidgets.QLabel(DialogInOrder)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelHybridShortage.setFont(font)
        self.labelHybridShortage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelHybridShortage.setObjectName("labelHybridShortage")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelHybridShortage)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogInOrder)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.line_4 = QtWidgets.QFrame(DialogInOrder)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.pushButtonPayHybrid = QtWidgets.QPushButton(DialogInOrder)
        self.pushButtonPayHybrid.setObjectName("pushButtonPayHybrid")
        self.horizontalLayout.addWidget(self.pushButtonPayHybrid)
        self.pushButtonPayPoints = QtWidgets.QPushButton(DialogInOrder)
        self.pushButtonPayPoints.setObjectName("pushButtonPayPoints")
        self.horizontalLayout.addWidget(self.pushButtonPayPoints)
        self.pushButtonPayCash = QtWidgets.QPushButton(DialogInOrder)
        self.pushButtonPayCash.setObjectName("pushButtonPayCash")
        self.horizontalLayout.addWidget(self.pushButtonPayCash)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogInOrder)
        QtCore.QMetaObject.connectSlotsByName(DialogInOrder)
        DialogInOrder.setTabOrder(self.pushButtonCancel, self.pushButtonPayCash)

    def retranslateUi(self, DialogInOrder):
        _translate = QtCore.QCoreApplication.translate
        DialogInOrder.setWindowTitle(_translate("DialogInOrder", "In-Order"))
        self.tableWidgetData.setSortingEnabled(False)
        item = self.tableWidgetData.verticalHeaderItem(0)
        item.setText(_translate("DialogInOrder", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(1)
        item.setText(_translate("DialogInOrder", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(2)
        item.setText(_translate("DialogInOrder", "New Row"))
        item = self.tableWidgetData.horizontalHeaderItem(0)
        item.setText(_translate("DialogInOrder", "Action"))
        item = self.tableWidgetData.horizontalHeaderItem(1)
        item.setText(_translate("DialogInOrder", "Qty."))
        item = self.tableWidgetData.horizontalHeaderItem(2)
        item.setText(_translate("DialogInOrder", "ItemName"))
        item = self.tableWidgetData.horizontalHeaderItem(3)
        item.setText(_translate("DialogInOrder", "Total"))
        self.label.setText(_translate("DialogInOrder", "Subtotal"))
        self.labelSubtotal.setText(_translate("DialogInOrder", "<Subtotal>"))
        self.label_2.setText(_translate("DialogInOrder", "Discount"))
        self.labelDiscount.setText(_translate("DialogInOrder", "<Discount>"))
        self.label_3.setText(_translate("DialogInOrder", "VAT"))
        self.labelTax.setText(_translate("DialogInOrder", "<Tax>"))
        self.label_5.setText(_translate("DialogInOrder", "Custom discount"))
        self.labelCustomDiscount.setText(_translate("DialogInOrder", "<CustomDiscount>"))
        self.label_4.setText(_translate("DialogInOrder", "Grand total"))
        self.labelGrandTotal.setText(_translate("DialogInOrder", "<GrandTotal>"))
        self.label_8.setText(_translate("DialogInOrder", "Member name"))
        self.label_9.setText(_translate("DialogInOrder", "Mobile number"))
        self.label_11.setText(_translate("DialogInOrder", "Points"))
        self.label_7.setText(_translate("DialogInOrder", "Cash"))
        self.pushButtonKeySix.setText(_translate("DialogInOrder", "6"))
        self.pushButtonKeyFive.setText(_translate("DialogInOrder", "5"))
        self.pushButtonKeyNine.setText(_translate("DialogInOrder", "9"))
        self.pushButtonKeySeven.setText(_translate("DialogInOrder", "7"))
        self.pushButtonKeyEight.setText(_translate("DialogInOrder", "8"))
        self.pushButtonKeyTwo.setText(_translate("DialogInOrder", "2"))
        self.pushButtonKeyThree.setText(_translate("DialogInOrder", "3"))
        self.pushButtonKeyFour.setText(_translate("DialogInOrder", "4"))
        self.pushButtonKeyOne.setText(_translate("DialogInOrder", "1"))
        self.pushButtonKeyDelete.setText(_translate("DialogInOrder", "Del"))
        self.pushButtonKeyZero.setText(_translate("DialogInOrder", "0"))
        self.pushButtonKeyDecimal.setText(_translate("DialogInOrder", "."))
        self.label_12.setText(_translate("DialogInOrder", "Cash"))
        self.label_13.setText(_translate("DialogInOrder", "Points"))
        self.label_14.setText(_translate("DialogInOrder", "Hybrid"))
        self.labelCashShortage.setText(_translate("DialogInOrder", "<CashShortage>"))
        self.label_6.setText(_translate("DialogInOrder", "Payment eligibility:"))
        self.labelPointsShortage.setText(_translate("DialogInOrder", "<PointsShortage>"))
        self.labelHybridShortage.setText(_translate("DialogInOrder", "<HybridShortage>"))
        self.pushButtonCancel.setText(_translate("DialogInOrder", "Cancel"))
        self.pushButtonPayHybrid.setText(_translate("DialogInOrder", "Hybrid"))
        self.pushButtonPayPoints.setText(_translate("DialogInOrder", "Points"))
        self.pushButtonPayCash.setText(_translate("DialogInOrder", "Cash"))
