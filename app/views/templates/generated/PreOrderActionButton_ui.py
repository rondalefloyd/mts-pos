# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\raccoondale\Documents\Personal\Git\mts-pos\app\views\templates\generated\PreOrderActionButton.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormPreOrderActionButton(object):
    def setupUi(self, FormPreOrderActionButton):
        FormPreOrderActionButton.setObjectName("FormPreOrderActionButton")
        FormPreOrderActionButton.resize(352, 72)
        FormPreOrderActionButton.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(FormPreOrderActionButton)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonAddOne = QtWidgets.QPushButton(FormPreOrderActionButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddOne.sizePolicy().hasHeightForWidth())
        self.pushButtonAddOne.setSizePolicy(sizePolicy)
        self.pushButtonAddOne.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonAddOne.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButtonAddOne.setObjectName("pushButtonAddOne")
        self.gridLayout.addWidget(self.pushButtonAddOne, 0, 0, 1, 1)
        self.pushButtonDeleteOne = QtWidgets.QPushButton(FormPreOrderActionButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeleteOne.sizePolicy().hasHeightForWidth())
        self.pushButtonDeleteOne.setSizePolicy(sizePolicy)
        self.pushButtonDeleteOne.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonDeleteOne.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButtonDeleteOne.setObjectName("pushButtonDeleteOne")
        self.gridLayout.addWidget(self.pushButtonDeleteOne, 0, 1, 1, 1)
        self.pushButtonAddExact = QtWidgets.QPushButton(FormPreOrderActionButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddExact.sizePolicy().hasHeightForWidth())
        self.pushButtonAddExact.setSizePolicy(sizePolicy)
        self.pushButtonAddExact.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonAddExact.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButtonAddExact.setObjectName("pushButtonAddExact")
        self.gridLayout.addWidget(self.pushButtonAddExact, 1, 0, 1, 1)
        self.pushButtonDeleteAll = QtWidgets.QPushButton(FormPreOrderActionButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeleteAll.sizePolicy().hasHeightForWidth())
        self.pushButtonDeleteAll.setSizePolicy(sizePolicy)
        self.pushButtonDeleteAll.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonDeleteAll.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButtonDeleteAll.setObjectName("pushButtonDeleteAll")
        self.gridLayout.addWidget(self.pushButtonDeleteAll, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(FormPreOrderActionButton)
        QtCore.QMetaObject.connectSlotsByName(FormPreOrderActionButton)

    def retranslateUi(self, FormPreOrderActionButton):
        _translate = QtCore.QCoreApplication.translate
        FormPreOrderActionButton.setWindowTitle(_translate("FormPreOrderActionButton", "Form"))
        self.pushButtonAddOne.setText(_translate("FormPreOrderActionButton", "Add One"))
        self.pushButtonDeleteOne.setText(_translate("FormPreOrderActionButton", "Delete One"))
        self.pushButtonAddExact.setText(_translate("FormPreOrderActionButton", "Add Exact"))
        self.pushButtonDeleteAll.setText(_translate("FormPreOrderActionButton", "Delete All"))
