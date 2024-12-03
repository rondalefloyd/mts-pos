# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/templates/generated\PostOrder.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_DialogPostOrder(object):
    def setupUi(self, DialogPostOrder):
        DialogPostOrder.setObjectName("DialogPostOrder")
        DialogPostOrder.resize(815, 661)
        DialogPostOrder.setModal(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(DialogPostOrder)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(DialogPostOrder)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.labelGrandTotal = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelGrandTotal.setFont(font)
        self.labelGrandTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelGrandTotal.setObjectName("labelGrandTotal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelGrandTotal)
        self.labelPayment = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelPayment.setFont(font)
        self.labelPayment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPayment.setObjectName("labelPayment")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelPayment)
        self.labelChange = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.labelChange.setFont(font)
        self.labelChange.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelChange.setObjectName("labelChange")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelChange)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 290, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame)
        self.widgetConfirmationButton = QtWidgets.QWidget(self.frame_2)
        self.widgetConfirmationButton.setObjectName("widgetConfirmationButton")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetConfirmationButton)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonClose = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout_2.addWidget(self.pushButtonClose)
        self.verticalLayout_2.addWidget(self.widgetConfirmationButton)
        self.verticalLayout_3.addWidget(self.frame_2)

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
