# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\VoidItemSold.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_DialogVoidItemSold(object):
    def setupUi(self, DialogVoidItemSold):
        DialogVoidItemSold.setObjectName("DialogVoidItemSold")
        DialogVoidItemSold.resize(699, 506)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogVoidItemSold)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(DialogVoidItemSold)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.scrollArea = QtWidgets.QScrollArea(DialogVoidItemSold)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 436))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBoxVoidReason = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxVoidReason.setEditable(True)
        self.comboBoxVoidReason.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxVoidReason.setObjectName("comboBoxVoidReason")
        self.comboBoxVoidReason.addItem("")
        self.comboBoxVoidReason.addItem("")
        self.comboBoxVoidReason.addItem("")
        self.comboBoxVoidReason.addItem("")
        self.comboBoxVoidReason.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxVoidReason)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogVoidItemSold)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.pushButtonVoid = QtWidgets.QPushButton(DialogVoidItemSold)
        self.pushButtonVoid.setObjectName("pushButtonVoid")
        self.horizontalLayout.addWidget(self.pushButtonVoid)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogVoidItemSold)
        QtCore.QMetaObject.connectSlotsByName(DialogVoidItemSold)
        DialogVoidItemSold.setTabOrder(self.scrollArea, self.pushButtonCancel)
        DialogVoidItemSold.setTabOrder(self.pushButtonCancel, self.pushButtonVoid)

    def retranslateUi(self, DialogVoidItemSold):
        _translate = QtCore.QCoreApplication.translate
        DialogVoidItemSold.setWindowTitle(_translate("DialogVoidItemSold", "Void item sold"))
        self.label_6.setText(_translate("DialogVoidItemSold", "MTS POS"))
        self.label_3.setText(_translate("DialogVoidItemSold", "Reason"))
        self.comboBoxVoidReason.setItemText(0, _translate("DialogVoidItemSold", "Customer Cancellation"))
        self.comboBoxVoidReason.setItemText(1, _translate("DialogVoidItemSold", "Incorrect Entry"))
        self.comboBoxVoidReason.setItemText(2, _translate("DialogVoidItemSold", "Price Discrepancy"))
        self.comboBoxVoidReason.setItemText(3, _translate("DialogVoidItemSold", "Item Not Available"))
        self.comboBoxVoidReason.setItemText(4, _translate("DialogVoidItemSold", "Payment Issue"))
        self.pushButtonCancel.setText(_translate("DialogVoidItemSold", "Cancel"))
        self.pushButtonVoid.setText(_translate("DialogVoidItemSold", "Void"))
