# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\UserConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_DialogUserConfig(object):
    def setupUi(self, DialogUserConfig):
        DialogUserConfig.setObjectName("DialogUserConfig")
        DialogUserConfig.resize(486, 550)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogUserConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(DialogUserConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.scrollArea = QtWidgets.QScrollArea(DialogUserConfig)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 466, 480))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBoxOrganizationName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxOrganizationName.setEnabled(False)
        self.comboBoxOrganizationName.setEditable(True)
        self.comboBoxOrganizationName.setMaxVisibleItems(2147483647)
        self.comboBoxOrganizationName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxOrganizationName.setObjectName("comboBoxOrganizationName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxOrganizationName)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditUserName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditUserName)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditAccessCode = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditAccessCode.setObjectName("lineEditAccessCode")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditAccessCode)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditFullName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditFullName.setObjectName("lineEditFullName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditFullName)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditMobileNumber = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditMobileNumber.setObjectName("lineEditMobileNumber")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditMobileNumber)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBoxAccessLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxAccessLevel.setEnabled(False)
        self.comboBoxAccessLevel.setObjectName("comboBoxAccessLevel")
        self.comboBoxAccessLevel.addItem("")
        self.comboBoxAccessLevel.addItem("")
        self.comboBoxAccessLevel.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBoxAccessLevel)
        self.dateEditBirthDate = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEditBirthDate.setCalendarPopup(True)
        self.dateEditBirthDate.setObjectName("dateEditBirthDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateEditBirthDate)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogUserConfig)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.pushButtonCreate = QtWidgets.QPushButton(DialogUserConfig)
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.horizontalLayout.addWidget(self.pushButtonCreate)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogUserConfig)
        QtCore.QMetaObject.connectSlotsByName(DialogUserConfig)

    def retranslateUi(self, DialogUserConfig):
        _translate = QtCore.QCoreApplication.translate
        DialogUserConfig.setWindowTitle(_translate("DialogUserConfig", "Edit User Config"))
        self.label_6.setText(_translate("DialogUserConfig", "MTS POS"))
        self.label_8.setText(_translate("DialogUserConfig", "Organization"))
        self.label.setText(_translate("DialogUserConfig", "Username"))
        self.label_2.setText(_translate("DialogUserConfig", "Password"))
        self.label_4.setText(_translate("DialogUserConfig", "Full name"))
        self.label_5.setText(_translate("DialogUserConfig", "Birthdate"))
        self.label_3.setText(_translate("DialogUserConfig", "Mobile number"))
        self.label_7.setText(_translate("DialogUserConfig", "Level"))
        self.comboBoxAccessLevel.setItemText(0, _translate("DialogUserConfig", "1"))
        self.comboBoxAccessLevel.setItemText(1, _translate("DialogUserConfig", "2"))
        self.comboBoxAccessLevel.setItemText(2, _translate("DialogUserConfig", "3"))
        self.dateEditBirthDate.setDisplayFormat(_translate("DialogUserConfig", "yyyy-MM-dd"))
        self.pushButtonCancel.setText(_translate("DialogUserConfig", "Cancel"))
        self.pushButtonCreate.setText(_translate("DialogUserConfig", "Save"))
