# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\Loading.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormLoading(object):
    def setupUi(self, FormLoading):
        FormLoading.setObjectName("FormLoading")
        FormLoading.setWindowModality(QtCore.Qt.ApplicationModal)
        FormLoading.resize(242, 73)
        self.verticalLayout = QtWidgets.QVBoxLayout(FormLoading)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(FormLoading)
        self.label.setEnabled(True)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(FormLoading)
        QtCore.QMetaObject.connectSlotsByName(FormLoading)

    def retranslateUi(self, FormLoading):
        _translate = QtCore.QCoreApplication.translate
        FormLoading.setWindowTitle(_translate("FormLoading", "Form"))
        self.label.setText(_translate("FormLoading", "Please wait..."))
