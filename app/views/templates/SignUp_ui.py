# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\raccoondale\Documents\Personal\Git\mts-pos\app\views\templates\SignUp.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSignUp(object):
    def setupUi(self, DialogSignUp):
        DialogSignUp.setObjectName("DialogSignUp")
        DialogSignUp.resize(699, 558)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogSignUp)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(DialogSignUp)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 699, 517))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBoxOrganizationName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxOrganizationName.setEditable(True)
        self.comboBoxOrganizationName.setMaxVisibleItems(2147483647)
        self.comboBoxOrganizationName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxOrganizationName.setObjectName("comboBoxOrganizationName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxOrganizationName)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditUserName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditUserName)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditPassword = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditFullName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditFullName.setObjectName("lineEditFullName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditFullName)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dateEditBirthDate = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEditBirthDate.setCalendarPopup(True)
        self.dateEditBirthDate.setObjectName("dateEditBirthDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateEditBirthDate)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditMobileNumber = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditMobileNumber.setObjectName("lineEditMobileNumber")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditMobileNumber)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBoxAccessLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxAccessLevel.setObjectName("comboBoxAccessLevel")
        self.comboBoxAccessLevel.addItem("")
        self.comboBoxAccessLevel.addItem("")
        self.comboBoxAccessLevel.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBoxAccessLevel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.widgetConfirmationButton = QtWidgets.QWidget(DialogSignUp)
        self.widgetConfirmationButton.setObjectName("widgetConfirmationButton")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetConfirmationButton)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.pushButtonCreate = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.horizontalLayout_2.addWidget(self.pushButtonCreate)
        self.verticalLayout.addWidget(self.widgetConfirmationButton)

        self.retranslateUi(DialogSignUp)
        QtCore.QMetaObject.connectSlotsByName(DialogSignUp)
        DialogSignUp.setTabOrder(self.scrollArea, self.lineEditFullName)
        DialogSignUp.setTabOrder(self.lineEditFullName, self.dateEditBirthDate)
        DialogSignUp.setTabOrder(self.dateEditBirthDate, self.lineEditMobileNumber)
        DialogSignUp.setTabOrder(self.lineEditMobileNumber, self.lineEditUserName)
        DialogSignUp.setTabOrder(self.lineEditUserName, self.lineEditPassword)
        DialogSignUp.setTabOrder(self.lineEditPassword, self.comboBoxAccessLevel)
        DialogSignUp.setTabOrder(self.comboBoxAccessLevel, self.comboBoxOrganizationName)

    def retranslateUi(self, DialogSignUp):
        _translate = QtCore.QCoreApplication.translate
        DialogSignUp.setWindowTitle(_translate("DialogSignUp", "Sign up"))
        self.label_8.setText(_translate("DialogSignUp", "Organization"))
        self.label_3.setText(_translate("DialogSignUp", "Username"))
        self.label_4.setText(_translate("DialogSignUp", "Password"))
        self.label.setText(_translate("DialogSignUp", "Full name"))
        self.label_5.setText(_translate("DialogSignUp", "Birthdate"))
        self.dateEditBirthDate.setDisplayFormat(_translate("DialogSignUp", "yyyy-MM-dd"))
        self.label_2.setText(_translate("DialogSignUp", "Mobile number"))
        self.label_7.setText(_translate("DialogSignUp", "Level"))
        self.comboBoxAccessLevel.setItemText(0, _translate("DialogSignUp", "1"))
        self.comboBoxAccessLevel.setItemText(1, _translate("DialogSignUp", "2"))
        self.comboBoxAccessLevel.setItemText(2, _translate("DialogSignUp", "3"))
        self.pushButtonCancel.setText(_translate("DialogSignUp", "Cancel"))
        self.pushButtonCreate.setText(_translate("DialogSignUp", "Create"))
