# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/templates/generated\InOrder.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_DialogInOrder(object):
    def setupUi(self, DialogInOrder):
        DialogInOrder.setObjectName("DialogInOrder")
        DialogInOrder.resize(756, 819)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(DialogInOrder)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(DialogInOrder)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidgetOrderItem = QtWidgets.QTableWidget(self.frame)
        self.tableWidgetOrderItem.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetOrderItem.setAlternatingRowColors(True)
        self.tableWidgetOrderItem.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetOrderItem.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidgetOrderItem.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetOrderItem.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetOrderItem.setShowGrid(False)
        self.tableWidgetOrderItem.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetOrderItem.setWordWrap(False)
        self.tableWidgetOrderItem.setObjectName("tableWidgetOrderItem")
        self.tableWidgetOrderItem.setColumnCount(5)
        self.tableWidgetOrderItem.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderItem.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderItem.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderItem.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderItem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderItem.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderItem.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderItem.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderItem.setHorizontalHeaderItem(4, item)
        self.tableWidgetOrderItem.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetOrderItem.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetOrderItem.verticalHeader().setVisible(False)
        self.tableWidgetOrderItem.verticalHeader().setDefaultSectionSize(50)
        self.tableWidgetOrderItem.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidgetOrderItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.labelSubtotal = QtWidgets.QLabel(self.frame)
        self.labelSubtotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSubtotal.setObjectName("labelSubtotal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelSubtotal)
        self.labelDiscount = QtWidgets.QLabel(self.frame)
        self.labelDiscount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDiscount.setObjectName("labelDiscount")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelDiscount)
        self.labelTax = QtWidgets.QLabel(self.frame)
        self.labelTax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTax.setObjectName("labelTax")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelTax)
        self.labelGrandTotal = QtWidgets.QLabel(self.frame)
        self.labelGrandTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelGrandTotal.setObjectName("labelGrandTotal")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.labelGrandTotal)
        self.labelCustomDiscount = QtWidgets.QLabel(self.frame)
        self.labelCustomDiscount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCustomDiscount.setObjectName("labelCustomDiscount")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelCustomDiscount)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.frameRegister = QtWidgets.QFrame(self.frame)
        self.frameRegister.setObjectName("frameRegister")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameRegister)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.frameRegister)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEditMemberName = QtWidgets.QLineEdit(self.frameRegister)
        self.lineEditMemberName.setEnabled(False)
        self.lineEditMemberName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditMemberName.setObjectName("lineEditMemberName")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditMemberName)
        self.label_9 = QtWidgets.QLabel(self.frameRegister)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEditMobileNumber = QtWidgets.QLineEdit(self.frameRegister)
        self.lineEditMobileNumber.setEnabled(False)
        self.lineEditMobileNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditMobileNumber.setObjectName("lineEditMobileNumber")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditMobileNumber)
        self.label_11 = QtWidgets.QLabel(self.frameRegister)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEditPoints = QtWidgets.QLineEdit(self.frameRegister)
        self.lineEditPoints.setEnabled(False)
        self.lineEditPoints.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditPoints.setObjectName("lineEditPoints")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditPoints)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.line_3 = QtWidgets.QFrame(self.frameRegister)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frameRegister)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEditCash = QtWidgets.QLineEdit(self.frameRegister)
        self.lineEditCash.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditCash.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditCash.setObjectName("lineEditCash")
        self.horizontalLayout_2.addWidget(self.lineEditCash)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonKeySix = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeySix.sizePolicy().hasHeightForWidth())
        self.pushButtonKeySix.setSizePolicy(sizePolicy)
        self.pushButtonKeySix.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeySix.setFont(font)
        self.pushButtonKeySix.setObjectName("pushButtonKeySix")
        self.gridLayout.addWidget(self.pushButtonKeySix, 1, 2, 1, 1)
        self.pushButtonKeyFive = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyFive.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyFive.setSizePolicy(sizePolicy)
        self.pushButtonKeyFive.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeyFive.setFont(font)
        self.pushButtonKeyFive.setObjectName("pushButtonKeyFive")
        self.gridLayout.addWidget(self.pushButtonKeyFive, 1, 1, 1, 1)
        self.pushButtonKeyNine = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyNine.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyNine.setSizePolicy(sizePolicy)
        self.pushButtonKeyNine.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeyNine.setFont(font)
        self.pushButtonKeyNine.setObjectName("pushButtonKeyNine")
        self.gridLayout.addWidget(self.pushButtonKeyNine, 2, 2, 1, 1)
        self.pushButtonKeySeven = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeySeven.sizePolicy().hasHeightForWidth())
        self.pushButtonKeySeven.setSizePolicy(sizePolicy)
        self.pushButtonKeySeven.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeySeven.setFont(font)
        self.pushButtonKeySeven.setObjectName("pushButtonKeySeven")
        self.gridLayout.addWidget(self.pushButtonKeySeven, 2, 0, 1, 1)
        self.pushButtonKeyEight = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyEight.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyEight.setSizePolicy(sizePolicy)
        self.pushButtonKeyEight.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeyEight.setFont(font)
        self.pushButtonKeyEight.setObjectName("pushButtonKeyEight")
        self.gridLayout.addWidget(self.pushButtonKeyEight, 2, 1, 1, 1)
        self.pushButtonKeyTwo = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyTwo.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyTwo.setSizePolicy(sizePolicy)
        self.pushButtonKeyTwo.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeyTwo.setFont(font)
        self.pushButtonKeyTwo.setObjectName("pushButtonKeyTwo")
        self.gridLayout.addWidget(self.pushButtonKeyTwo, 0, 1, 1, 1)
        self.pushButtonKeyThree = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyThree.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyThree.setSizePolicy(sizePolicy)
        self.pushButtonKeyThree.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeyThree.setFont(font)
        self.pushButtonKeyThree.setObjectName("pushButtonKeyThree")
        self.gridLayout.addWidget(self.pushButtonKeyThree, 0, 2, 1, 1)
        self.pushButtonKeyFour = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyFour.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyFour.setSizePolicy(sizePolicy)
        self.pushButtonKeyFour.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeyFour.setFont(font)
        self.pushButtonKeyFour.setObjectName("pushButtonKeyFour")
        self.gridLayout.addWidget(self.pushButtonKeyFour, 1, 0, 1, 1)
        self.pushButtonKeyOne = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyOne.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyOne.setSizePolicy(sizePolicy)
        self.pushButtonKeyOne.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeyOne.setFont(font)
        self.pushButtonKeyOne.setObjectName("pushButtonKeyOne")
        self.gridLayout.addWidget(self.pushButtonKeyOne, 0, 0, 1, 1)
        self.pushButtonKeyDelete = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyDelete.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyDelete.setSizePolicy(sizePolicy)
        self.pushButtonKeyDelete.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeyDelete.setFont(font)
        self.pushButtonKeyDelete.setObjectName("pushButtonKeyDelete")
        self.gridLayout.addWidget(self.pushButtonKeyDelete, 3, 0, 1, 1)
        self.pushButtonKeyZero = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyZero.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyZero.setSizePolicy(sizePolicy)
        self.pushButtonKeyZero.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeyZero.setFont(font)
        self.pushButtonKeyZero.setObjectName("pushButtonKeyZero")
        self.gridLayout.addWidget(self.pushButtonKeyZero, 3, 1, 1, 1)
        self.pushButtonKeyDecimal = QtWidgets.QPushButton(self.frameRegister)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKeyDecimal.sizePolicy().hasHeightForWidth())
        self.pushButtonKeyDecimal.setSizePolicy(sizePolicy)
        self.pushButtonKeyDecimal.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKeyDecimal.setFont(font)
        self.pushButtonKeyDecimal.setObjectName("pushButtonKeyDecimal")
        self.gridLayout.addWidget(self.pushButtonKeyDecimal, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.frameRegister)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelCombo = QtWidgets.QLabel(self.frameRegister)
        self.labelCombo.setObjectName("labelCombo")
        self.gridLayout_2.addWidget(self.labelCombo, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frameRegister)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frameRegister)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frameRegister)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frameRegister)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.labelPoints = QtWidgets.QLabel(self.frameRegister)
        self.labelPoints.setObjectName("labelPoints")
        self.gridLayout_2.addWidget(self.labelPoints, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelComboCashPayment = QtWidgets.QLabel(self.frameRegister)
        self.labelComboCashPayment.setObjectName("labelComboCashPayment")
        self.horizontalLayout.addWidget(self.labelComboCashPayment)
        self.labelPlusSymbol = QtWidgets.QLabel(self.frameRegister)
        self.labelPlusSymbol.setObjectName("labelPlusSymbol")
        self.horizontalLayout.addWidget(self.labelPlusSymbol)
        self.labelComboPointsPayment = QtWidgets.QLabel(self.frameRegister)
        self.labelComboPointsPayment.setObjectName("labelComboPointsPayment")
        self.horizontalLayout.addWidget(self.labelComboPointsPayment)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.labelPointsPayment = QtWidgets.QLabel(self.frameRegister)
        self.labelPointsPayment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPointsPayment.setObjectName("labelPointsPayment")
        self.gridLayout_2.addWidget(self.labelPointsPayment, 2, 1, 1, 1)
        self.labelCashPayment = QtWidgets.QLabel(self.frameRegister)
        self.labelCashPayment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCashPayment.setObjectName("labelCashPayment")
        self.gridLayout_2.addWidget(self.labelCashPayment, 1, 1, 1, 1)
        self.labelCashShortageExcess = QtWidgets.QLabel(self.frameRegister)
        self.labelCashShortageExcess.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCashShortageExcess.setObjectName("labelCashShortageExcess")
        self.gridLayout_2.addWidget(self.labelCashShortageExcess, 1, 2, 1, 1)
        self.labelPointsShortageExcess = QtWidgets.QLabel(self.frameRegister)
        self.labelPointsShortageExcess.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPointsShortageExcess.setObjectName("labelPointsShortageExcess")
        self.gridLayout_2.addWidget(self.labelPointsShortageExcess, 2, 2, 1, 1)
        self.labelComboShortageExcess = QtWidgets.QLabel(self.frameRegister)
        self.labelComboShortageExcess.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelComboShortageExcess.setObjectName("labelComboShortageExcess")
        self.gridLayout_2.addWidget(self.labelComboShortageExcess, 3, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout_3.addWidget(self.frameRegister, 0, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.frame)
        self.widgetConfirmationButton = QtWidgets.QWidget(DialogInOrder)
        self.widgetConfirmationButton.setObjectName("widgetConfirmationButton")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widgetConfirmationButton)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButtonCancel = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_4.addWidget(self.pushButtonCancel)
        self.line_4 = QtWidgets.QFrame(self.widgetConfirmationButton)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_4.addWidget(self.line_4)
        self.pushButtonPayCombo = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonPayCombo.setObjectName("pushButtonPayCombo")
        self.horizontalLayout_4.addWidget(self.pushButtonPayCombo)
        self.pushButtonPayPoints = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonPayPoints.setObjectName("pushButtonPayPoints")
        self.horizontalLayout_4.addWidget(self.pushButtonPayPoints)
        self.pushButtonPayCash = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonPayCash.setObjectName("pushButtonPayCash")
        self.horizontalLayout_4.addWidget(self.pushButtonPayCash)
        self.verticalLayout_5.addWidget(self.widgetConfirmationButton)

        self.retranslateUi(DialogInOrder)
        QtCore.QMetaObject.connectSlotsByName(DialogInOrder)

    def retranslateUi(self, DialogInOrder):
        _translate = QtCore.QCoreApplication.translate
        DialogInOrder.setWindowTitle(_translate("DialogInOrder", "In-Order"))
        self.tableWidgetOrderItem.setSortingEnabled(False)
        item = self.tableWidgetOrderItem.verticalHeaderItem(0)
        item.setText(_translate("DialogInOrder", "New Row"))
        item = self.tableWidgetOrderItem.verticalHeaderItem(1)
        item.setText(_translate("DialogInOrder", "New Row"))
        item = self.tableWidgetOrderItem.verticalHeaderItem(2)
        item.setText(_translate("DialogInOrder", "New Row"))
        item = self.tableWidgetOrderItem.horizontalHeaderItem(0)
        item.setText(_translate("DialogInOrder", "Action"))
        item = self.tableWidgetOrderItem.horizontalHeaderItem(1)
        item.setText(_translate("DialogInOrder", "Qty."))
        item = self.tableWidgetOrderItem.horizontalHeaderItem(2)
        item.setText(_translate("DialogInOrder", "ItemName"))
        item = self.tableWidgetOrderItem.horizontalHeaderItem(3)
        item.setText(_translate("DialogInOrder", "Total"))
        item = self.tableWidgetOrderItem.horizontalHeaderItem(4)
        item.setText(_translate("DialogInOrder", "CustomDiscount"))
        self.label.setText(_translate("DialogInOrder", "Subtotal"))
        self.label_2.setText(_translate("DialogInOrder", "Discount"))
        self.label_3.setText(_translate("DialogInOrder", "VAT"))
        self.label_5.setText(_translate("DialogInOrder", "Custom discount"))
        self.label_4.setText(_translate("DialogInOrder", "Grandtotal"))
        self.labelSubtotal.setText(_translate("DialogInOrder", "0.00"))
        self.labelDiscount.setText(_translate("DialogInOrder", "0.00"))
        self.labelTax.setText(_translate("DialogInOrder", "0.00"))
        self.labelGrandTotal.setText(_translate("DialogInOrder", "0.00"))
        self.labelCustomDiscount.setText(_translate("DialogInOrder", "0.00"))
        self.label_8.setText(_translate("DialogInOrder", "Member name"))
        self.label_9.setText(_translate("DialogInOrder", "Mobile number"))
        self.label_11.setText(_translate("DialogInOrder", "Point/s"))
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
        self.labelCombo.setText(_translate("DialogInOrder", "Combo"))
        self.label_12.setText(_translate("DialogInOrder", "Cash"))
        self.label_17.setText(_translate("DialogInOrder", "Shortage/Excess"))
        self.label_15.setText(_translate("DialogInOrder", "Payment"))
        self.label_10.setText(_translate("DialogInOrder", "Type"))
        self.labelPoints.setText(_translate("DialogInOrder", "Points"))
        self.labelComboCashPayment.setText(_translate("DialogInOrder", "0.00"))
        self.labelPlusSymbol.setText(_translate("DialogInOrder", "+"))
        self.labelComboPointsPayment.setText(_translate("DialogInOrder", "0.00"))
        self.labelPointsPayment.setText(_translate("DialogInOrder", "0.00"))
        self.labelCashPayment.setText(_translate("DialogInOrder", "0.00"))
        self.labelCashShortageExcess.setText(_translate("DialogInOrder", "0.00"))
        self.labelPointsShortageExcess.setText(_translate("DialogInOrder", "0.00"))
        self.labelComboShortageExcess.setText(_translate("DialogInOrder", "0.00"))
        self.pushButtonCancel.setText(_translate("DialogInOrder", "Cancel"))
        self.pushButtonPayCombo.setText(_translate("DialogInOrder", "Combo"))
        self.pushButtonPayPoints.setText(_translate("DialogInOrder", "Points"))
        self.pushButtonPayCash.setText(_translate("DialogInOrder", "Cash"))
