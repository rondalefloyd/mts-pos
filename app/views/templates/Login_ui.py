# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\raccoondale\Documents\Personal\Git\mts-pos\app\views\templates\Login.ui'
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
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(DialogLogin)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 206))
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
        self.lineEditPassword = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.horizontalLayout.addWidget(self.lineEditPassword)
        self.pushButtonPasswordVisibility = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPasswordVisibility.sizePolicy().hasHeightForWidth())
        self.pushButtonPasswordVisibility.setSizePolicy(sizePolicy)
        self.pushButtonPasswordVisibility.setCheckable(True)
        self.pushButtonPasswordVisibility.setObjectName("pushButtonPasswordVisibility")
        self.horizontalLayout.addWidget(self.pushButtonPasswordVisibility)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.widgetConfirmationButton = QtWidgets.QWidget(DialogLogin)
        self.widgetConfirmationButton.setObjectName("widgetConfirmationButton")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetConfirmationButton)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(136, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButtonSetup = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonSetup.setObjectName("pushButtonSetup")
        self.horizontalLayout_3.addWidget(self.pushButtonSetup)
        self.pushButtonSignUp = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonSignUp.setObjectName("pushButtonSignUp")
        self.horizontalLayout_3.addWidget(self.pushButtonSignUp)
        self.pushButtonLogin = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.horizontalLayout_3.addWidget(self.pushButtonLogin)
        self.verticalLayout.addWidget(self.widgetConfirmationButton)

        self.retranslateUi(DialogLogin)
        QtCore.QMetaObject.connectSlotsByName(DialogLogin)
        DialogLogin.setTabOrder(self.scrollArea, self.lineEditUserName)
        DialogLogin.setTabOrder(self.lineEditUserName, self.lineEditPassword)
        DialogLogin.setTabOrder(self.lineEditPassword, self.pushButtonPasswordVisibility)

    def retranslateUi(self, DialogLogin):
        _translate = QtCore.QCoreApplication.translate
        DialogLogin.setWindowTitle(_translate("DialogLogin", "Login"))
        self.label.setText(_translate("DialogLogin", "Username"))
        self.label_2.setText(_translate("DialogLogin", "Password"))
        self.pushButtonPasswordVisibility.setText(_translate("DialogLogin", "<VisibilityIndicator>"))
        self.pushButtonSetup.setText(_translate("DialogLogin", "Setup"))
        self.pushButtonSignUp.setText(_translate("DialogLogin", "Sign up"))
        self.pushButtonLogin.setText(_translate("DialogLogin", "Login"))
