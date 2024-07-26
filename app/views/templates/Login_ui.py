# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogLogin(object):
    def setupUi(self, DialogLogin):
        DialogLogin.setObjectName("DialogLogin")
        DialogLogin.resize(400, 247)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogLogin)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(DialogLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.scrollArea = QtWidgets.QScrollArea(DialogLogin)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 177))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditUserName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditUserName)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditAccessCode = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditAccessCode.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditAccessCode.setObjectName("lineEditAccessCode")
        self.horizontalLayout.addWidget(self.lineEditAccessCode)
        self.pushButtonAccessCodeVisibility = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAccessCodeVisibility.sizePolicy().hasHeightForWidth())
        self.pushButtonAccessCodeVisibility.setSizePolicy(sizePolicy)
        self.pushButtonAccessCodeVisibility.setCheckable(True)
        self.pushButtonAccessCodeVisibility.setObjectName("pushButtonAccessCodeVisibility")
        self.horizontalLayout.addWidget(self.pushButtonAccessCodeVisibility)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.checkBoxRememberMe = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBoxRememberMe.setObjectName("checkBoxRememberMe")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.checkBoxRememberMe)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonSetup = QtWidgets.QPushButton(DialogLogin)
        self.pushButtonSetup.setObjectName("pushButtonSetup")
        self.horizontalLayout_2.addWidget(self.pushButtonSetup)
        self.pushButtonSignUp = QtWidgets.QPushButton(DialogLogin)
        self.pushButtonSignUp.setObjectName("pushButtonSignUp")
        self.horizontalLayout_2.addWidget(self.pushButtonSignUp)
        self.pushButtonLogin = QtWidgets.QPushButton(DialogLogin)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.horizontalLayout_2.addWidget(self.pushButtonLogin)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DialogLogin)
        QtCore.QMetaObject.connectSlotsByName(DialogLogin)

    def retranslateUi(self, DialogLogin):
        _translate = QtCore.QCoreApplication.translate
        DialogLogin.setWindowTitle(_translate("DialogLogin", "Login"))
        self.label_3.setText(_translate("DialogLogin", "MTS POS"))
        self.label.setText(_translate("DialogLogin", "Username"))
        self.label_2.setText(_translate("DialogLogin", "Password"))
        self.pushButtonAccessCodeVisibility.setText(_translate("DialogLogin", "<VisibilityIndicator>"))
        self.checkBoxRememberMe.setToolTip(_translate("DialogLogin", "<html><head/><body><p>When checked, the login field will automatically populate with the credentials of the last user who chose to be remembered upon their next login.</p></body></html>"))
        self.checkBoxRememberMe.setText(_translate("DialogLogin", "Remember me"))
        self.pushButtonSetup.setText(_translate("DialogLogin", "Setup"))
        self.pushButtonSignUp.setText(_translate("DialogLogin", "Sign up"))
        self.pushButtonLogin.setText(_translate("DialogLogin", "Login"))
