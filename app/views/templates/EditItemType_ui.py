# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/mimoy/Documents/GitHub/mts-pos/app/views/templates/generated\EditItemType.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_DialogEditItemType(object):
    def setupUi(self, DialogEditItemType):
        DialogEditItemType.setObjectName("DialogEditItemType")
        DialogEditItemType.resize(699, 506)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogEditItemType)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(DialogEditItemType)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.scrollArea = QtWidgets.QScrollArea(DialogEditItemType)
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
        self.lineEditItemTypeName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditItemTypeName.setObjectName("lineEditItemTypeName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditItemTypeName)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogEditItemType)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.pushButtonSave = QtWidgets.QPushButton(DialogEditItemType)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogEditItemType)
        QtCore.QMetaObject.connectSlotsByName(DialogEditItemType)
        DialogEditItemType.setTabOrder(self.scrollArea, self.pushButtonCancel)
        DialogEditItemType.setTabOrder(self.pushButtonCancel, self.pushButtonSave)

    def retranslateUi(self, DialogEditItemType):
        _translate = QtCore.QCoreApplication.translate
        DialogEditItemType.setWindowTitle(_translate("DialogEditItemType", "Edit item type"))
        self.label_6.setText(_translate("DialogEditItemType", "MTS POS"))
        self.label_3.setText(_translate("DialogEditItemType", "Item type name"))
        self.pushButtonCancel.setText(_translate("DialogEditItemType", "Cancel"))
        self.pushButtonSave.setText(_translate("DialogEditItemType", "Save"))
