# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/mimoy/Documents/GitHub/mts-pos/app/views/templates/generated\EditStock.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_DialogEditStock(object):
    def setupUi(self, DialogEditStock):
        DialogEditStock.setObjectName("DialogEditStock")
        DialogEditStock.resize(699, 506)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogEditStock)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(DialogEditStock)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 699, 465))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditItemName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditItemName.setEnabled(False)
        self.lineEditItemName.setObjectName("lineEditItemName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditItemName)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditOnHand = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditOnHand.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOnHand.setObjectName("lineEditOnHand")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditOnHand)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditAvailable = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditAvailable.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditAvailable.setObjectName("lineEditAvailable")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditAvailable)
        self.comboBoxSalesGroupName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxSalesGroupName.setEnabled(False)
        self.comboBoxSalesGroupName.setEditable(True)
        self.comboBoxSalesGroupName.setObjectName("comboBoxSalesGroupName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxSalesGroupName)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.widgetConfirmationButton = QtWidgets.QWidget(DialogEditStock)
        self.widgetConfirmationButton.setObjectName("widgetConfirmationButton")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetConfirmationButton)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.pushButtonSave = QtWidgets.QPushButton(self.widgetConfirmationButton)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_2.addWidget(self.pushButtonSave)
        self.verticalLayout.addWidget(self.widgetConfirmationButton)

        self.retranslateUi(DialogEditStock)
        QtCore.QMetaObject.connectSlotsByName(DialogEditStock)

    def retranslateUi(self, DialogEditStock):
        _translate = QtCore.QCoreApplication.translate
        DialogEditStock.setWindowTitle(_translate("DialogEditStock", "Edit stock"))
        self.label_3.setText(_translate("DialogEditStock", "Item name"))
        self.label_2.setText(_translate("DialogEditStock", "OnHand"))
        self.label_4.setText(_translate("DialogEditStock", "Available"))
        self.label.setText(_translate("DialogEditStock", "Sale group"))
        self.pushButtonCancel.setText(_translate("DialogEditStock", "Cancel"))
        self.pushButtonSave.setText(_translate("DialogEditStock", "Save"))
