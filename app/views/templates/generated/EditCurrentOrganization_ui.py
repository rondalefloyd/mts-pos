# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\raccoondale\Documents\Personal\Git\mts-pos\app\views\templates\generated\EditCurrentOrganization.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogEditCurrentOrganization(object):
    def setupUi(self, DialogEditCurrentOrganization):
        DialogEditCurrentOrganization.setObjectName("DialogEditCurrentOrganization")
        DialogEditCurrentOrganization.resize(440, 241)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogEditCurrentOrganization)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(DialogEditCurrentOrganization)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 440, 200))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditOrganizationName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditOrganizationName.setObjectName("lineEditOrganizationName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditOrganizationName)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditAddress = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditAddress)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditMobileNumber = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditMobileNumber.setObjectName("lineEditMobileNumber")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditMobileNumber)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditTaxId = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditTaxId.setObjectName("lineEditTaxId")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditTaxId)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEditPassword = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.widgetConfirmationButton = QtWidgets.QWidget(DialogEditCurrentOrganization)
        self.widgetConfirmationButton.setObjectName("widgetConfirmationButton")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetConfirmationButton)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(257, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.pushButtonSave = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_2.addWidget(self.pushButtonSave)
        self.verticalLayout.addWidget(self.widgetConfirmationButton)

        self.retranslateUi(DialogEditCurrentOrganization)
        QtCore.QMetaObject.connectSlotsByName(DialogEditCurrentOrganization)

    def retranslateUi(self, DialogEditCurrentOrganization):
        _translate = QtCore.QCoreApplication.translate
        DialogEditCurrentOrganization.setWindowTitle(_translate("DialogEditCurrentOrganization", "Edit Organization"))
        self.label.setText(_translate("DialogEditCurrentOrganization", "Organization Name"))
        self.label_2.setText(_translate("DialogEditCurrentOrganization", "Address"))
        self.label_3.setText(_translate("DialogEditCurrentOrganization", "Mobile number"))
        self.label_4.setText(_translate("DialogEditCurrentOrganization", "Tax ID"))
        self.label_5.setText(_translate("DialogEditCurrentOrganization", "Password"))
        self.pushButtonCancel.setText(_translate("DialogEditCurrentOrganization", "Cancel"))
        self.pushButtonSave.setText(_translate("DialogEditCurrentOrganization", "Save"))
