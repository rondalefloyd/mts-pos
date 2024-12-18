# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/templates/generated\Setup.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_DialogSetup(object):
    def setupUi(self, DialogSetup):
        DialogSetup.setObjectName("DialogSetup")
        DialogSetup.resize(440, 432)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogSetup)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(DialogSetup)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 440, 391))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditOrganizationName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditOrganizationName.setObjectName("lineEditOrganizationName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditOrganizationName)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditAddress = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditAddress)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditMobileNumber = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditMobileNumber.setObjectName("lineEditMobileNumber")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditMobileNumber)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEditPassword = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditTaxId = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditTaxId.setObjectName("lineEditTaxId")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditTaxId)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.widget = QtWidgets.QWidget(DialogSetup)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(self.widget)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.pushButtonCreate = QtWidgets.QPushButton(self.widget)
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.horizontalLayout_2.addWidget(self.pushButtonCreate)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(DialogSetup)
        QtCore.QMetaObject.connectSlotsByName(DialogSetup)

    def retranslateUi(self, DialogSetup):
        _translate = QtCore.QCoreApplication.translate
        DialogSetup.setWindowTitle(_translate("DialogSetup", "Setup"))
        self.label.setText(_translate("DialogSetup", "Organization Name"))
        self.label_2.setText(_translate("DialogSetup", "Address"))
        self.label_3.setText(_translate("DialogSetup", "Mobile number"))
        self.label_5.setText(_translate("DialogSetup", "Password"))
        self.label_4.setText(_translate("DialogSetup", "Tax ID"))
        self.pushButtonCancel.setText(_translate("DialogSetup", "Cancel"))
        self.pushButtonCreate.setText(_translate("DialogSetup", "Create"))
