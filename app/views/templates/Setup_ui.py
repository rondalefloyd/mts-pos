# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\Setup.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSetup(object):
    def setupUi(self, DialogSetup):
        DialogSetup.setObjectName("DialogSetup")
        DialogSetup.resize(440, 432)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogSetup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(DialogSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.scrollArea = QtWidgets.QScrollArea(DialogSetup)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 420, 362))
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
        self.lineEditAccessCode = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditAccessCode.setObjectName("lineEditAccessCode")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditAccessCode)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditTaxId = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditTaxId.setObjectName("lineEditTaxId")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditTaxId)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogSetup)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.pushButtonCreate = QtWidgets.QPushButton(DialogSetup)
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.horizontalLayout.addWidget(self.pushButtonCreate)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogSetup)
        QtCore.QMetaObject.connectSlotsByName(DialogSetup)

    def retranslateUi(self, DialogSetup):
        _translate = QtCore.QCoreApplication.translate
        DialogSetup.setWindowTitle(_translate("DialogSetup", "Setup"))
        self.label_6.setText(_translate("DialogSetup", "MTS POS"))
        self.label.setText(_translate("DialogSetup", "Organization Name"))
        self.label_2.setText(_translate("DialogSetup", "Address"))
        self.label_3.setText(_translate("DialogSetup", "Mobile number"))
        self.label_5.setText(_translate("DialogSetup", "Password"))
        self.label_4.setText(_translate("DialogSetup", "Tax ID"))
        self.pushButtonCancel.setText(_translate("DialogSetup", "Cancel"))
        self.pushButtonCreate.setText(_translate("DialogSetup", "Create"))
