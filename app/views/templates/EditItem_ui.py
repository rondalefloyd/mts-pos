# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/views/templates/generated\EditItem.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_DialogEditItem(object):
    def setupUi(self, DialogEditItem):
        DialogEditItem.setObjectName("DialogEditItem")
        DialogEditItem.resize(699, 506)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogEditItem)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(DialogEditItem)
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
        self.lineEditItemName.setObjectName("lineEditItemName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditItemName)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditBarcode = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditBarcode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditBarcode.setObjectName("lineEditBarcode")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditBarcode)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.dateEditExpireDate = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEditExpireDate.setCalendarPopup(True)
        self.dateEditExpireDate.setObjectName("dateEditExpireDate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEditExpireDate)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBoxItemTypeName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxItemTypeName.setEditable(True)
        self.comboBoxItemTypeName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxItemTypeName.setObjectName("comboBoxItemTypeName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBoxItemTypeName)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBoxBrandName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxBrandName.setEditable(True)
        self.comboBoxBrandName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxBrandName.setObjectName("comboBoxBrandName")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBoxBrandName)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.comboBoxSupplierName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxSupplierName.setEditable(True)
        self.comboBoxSupplierName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxSupplierName.setObjectName("comboBoxSupplierName")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBoxSupplierName)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.comboBoxSalesGroupName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxSalesGroupName.setEnabled(True)
        self.comboBoxSalesGroupName.setEditable(False)
        self.comboBoxSalesGroupName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxSalesGroupName.setObjectName("comboBoxSalesGroupName")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBoxSalesGroupName)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.widgetConfirmationButton = QtWidgets.QWidget(DialogEditItem)
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

        self.retranslateUi(DialogEditItem)
        QtCore.QMetaObject.connectSlotsByName(DialogEditItem)

    def retranslateUi(self, DialogEditItem):
        _translate = QtCore.QCoreApplication.translate
        DialogEditItem.setWindowTitle(_translate("DialogEditItem", "Edit item"))
        self.label_3.setText(_translate("DialogEditItem", "Item name"))
        self.label_2.setText(_translate("DialogEditItem", "Barcode"))
        self.label.setText(_translate("DialogEditItem", "ExpireDate"))
        self.dateEditExpireDate.setDisplayFormat(_translate("DialogEditItem", "yyyy-MM-dd"))
        self.label_4.setText(_translate("DialogEditItem", "Type"))
        self.label_5.setText(_translate("DialogEditItem", "Brand"))
        self.label_9.setText(_translate("DialogEditItem", "Supplier"))
        self.label_12.setText(_translate("DialogEditItem", "Sale group"))
        self.pushButtonCancel.setText(_translate("DialogEditItem", "Cancel"))
        self.pushButtonSave.setText(_translate("DialogEditItem", "Save"))
