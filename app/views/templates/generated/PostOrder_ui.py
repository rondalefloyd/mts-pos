# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\generated\PostOrder.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_DialogPostOrder(object):
    def setupUi(self, DialogPostOrder):
        DialogPostOrder.setObjectName("DialogPostOrder")
        DialogPostOrder.resize(878, 413)
        DialogPostOrder.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DialogPostOrder)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(DialogPostOrder)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(DialogPostOrder)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(DialogPostOrder)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.labelGrandTotal = QtWidgets.QLabel(DialogPostOrder)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelGrandTotal.setFont(font)
        self.labelGrandTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelGrandTotal.setObjectName("labelGrandTotal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelGrandTotal)
        self.labelPayment = QtWidgets.QLabel(DialogPostOrder)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelPayment.setFont(font)
        self.labelPayment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPayment.setObjectName("labelPayment")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelPayment)
        self.labelChange = QtWidgets.QLabel(DialogPostOrder)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelChange.setFont(font)
        self.labelChange.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelChange.setObjectName("labelChange")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelChange)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonClose = QtWidgets.QPushButton(DialogPostOrder)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout.addWidget(self.pushButtonClose)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogPostOrder)
        QtCore.QMetaObject.connectSlotsByName(DialogPostOrder)

    def retranslateUi(self, DialogPostOrder):
        _translate = QtCore.QCoreApplication.translate
        DialogPostOrder.setWindowTitle(_translate("DialogPostOrder", "Sign up"))
        self.label.setText(_translate("DialogPostOrder", "Grand total"))
        self.label_2.setText(_translate("DialogPostOrder", "Payment"))
        self.label_3.setText(_translate("DialogPostOrder", "Change"))
        self.labelGrandTotal.setText(_translate("DialogPostOrder", "TextLabel"))
        self.labelPayment.setText(_translate("DialogPostOrder", "TextLabel"))
        self.labelChange.setText(_translate("DialogPostOrder", "TextLabel"))
        self.pushButtonClose.setText(_translate("DialogPostOrder", "Close"))
