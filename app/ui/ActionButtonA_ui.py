# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\ui\widget\ActionButtonA.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormActionButtonA(object):
    def setupUi(self, FormActionButtonA):
        FormActionButtonA.setObjectName("FormActionButtonA")
        FormActionButtonA.resize(417, 41)
        self.horizontalLayout = QtWidgets.QHBoxLayout(FormActionButtonA)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonEdit = QtWidgets.QPushButton(FormActionButtonA)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.horizontalLayout.addWidget(self.pushButtonEdit)
        self.pushButtonView = QtWidgets.QPushButton(FormActionButtonA)
        self.pushButtonView.setObjectName("pushButtonView")
        self.horizontalLayout.addWidget(self.pushButtonView)
        self.pushButtonDelete = QtWidgets.QPushButton(FormActionButtonA)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        self.pushButtonAdd = QtWidgets.QPushButton(FormActionButtonA)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout.addWidget(self.pushButtonAdd)
        self.pushButtonDiscount = QtWidgets.QPushButton(FormActionButtonA)
        self.pushButtonDiscount.setObjectName("pushButtonDiscount")
        self.horizontalLayout.addWidget(self.pushButtonDiscount)

        self.retranslateUi(FormActionButtonA)
        QtCore.QMetaObject.connectSlotsByName(FormActionButtonA)

    def retranslateUi(self, FormActionButtonA):
        _translate = QtCore.QCoreApplication.translate
        FormActionButtonA.setWindowTitle(_translate("FormActionButtonA", "Form"))
        self.pushButtonEdit.setText(_translate("FormActionButtonA", "Edit"))
        self.pushButtonView.setText(_translate("FormActionButtonA", "View"))
        self.pushButtonDelete.setText(_translate("FormActionButtonA", "Delete"))
        self.pushButtonAdd.setText(_translate("FormActionButtonA", "Add"))
        self.pushButtonDiscount.setText(_translate("FormActionButtonA", "Discount"))