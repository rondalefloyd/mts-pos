# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\EditPromo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_DialogEditPromo(object):
    def setupUi(self, DialogEditPromo):
        DialogEditPromo.setObjectName("DialogEditPromo")
        DialogEditPromo.resize(699, 506)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogEditPromo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(DialogEditPromo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.scrollArea = QtWidgets.QScrollArea(DialogEditPromo)
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
        self.lineEditPromoName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditPromoName.setObjectName("lineEditPromoName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditPromoName)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditDiscountRate = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditDiscountRate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditDiscountRate.setObjectName("lineEditDiscountRate")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditDiscountRate)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditDescription = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditDescription.setObjectName("lineEditDescription")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditDescription)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogEditPromo)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.pushButtonSave = QtWidgets.QPushButton(DialogEditPromo)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogEditPromo)
        QtCore.QMetaObject.connectSlotsByName(DialogEditPromo)
        DialogEditPromo.setTabOrder(self.scrollArea, self.pushButtonCancel)
        DialogEditPromo.setTabOrder(self.pushButtonCancel, self.pushButtonSave)

    def retranslateUi(self, DialogEditPromo):
        _translate = QtCore.QCoreApplication.translate
        DialogEditPromo.setWindowTitle(_translate("DialogEditPromo", "Edit promo"))
        self.label_6.setText(_translate("DialogEditPromo", "MTS POS"))
        self.label_3.setText(_translate("DialogEditPromo", "Promo name"))
        self.label_2.setText(_translate("DialogEditPromo", "Discount rate"))
        self.label.setText(_translate("DialogEditPromo", "Description"))
        self.pushButtonCancel.setText(_translate("DialogEditPromo", "Cancel"))
        self.pushButtonSave.setText(_translate("DialogEditPromo", "Save"))
