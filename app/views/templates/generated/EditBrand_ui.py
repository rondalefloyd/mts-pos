# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\generated\EditBrand.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogEditBrand(object):
    def setupUi(self, DialogEditBrand):
        DialogEditBrand.setObjectName("DialogEditBrand")
        DialogEditBrand.resize(699, 506)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogEditBrand)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(DialogEditBrand)
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
        self.lineEditBrandName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditBrandName.setObjectName("lineEditBrandName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditBrandName)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.widgetConfirmationButton = QtWidgets.QWidget(DialogEditBrand)
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

        self.retranslateUi(DialogEditBrand)
        QtCore.QMetaObject.connectSlotsByName(DialogEditBrand)

    def retranslateUi(self, DialogEditBrand):
        _translate = QtCore.QCoreApplication.translate
        DialogEditBrand.setWindowTitle(_translate("DialogEditBrand", "Edit brand"))
        self.label_3.setText(_translate("DialogEditBrand", "Brand name"))
        self.pushButtonCancel.setText(_translate("DialogEditBrand", "Cancel"))
        self.pushButtonSave.setText(_translate("DialogEditBrand", "Save"))
