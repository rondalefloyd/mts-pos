# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\raccoondale\Documents\Personal\Git\mts-pos\app\views\templates\ManageActionButton.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormManageActionButton(object):
    def setupUi(self, FormManageActionButton):
        FormManageActionButton.setObjectName("FormManageActionButton")
        FormManageActionButton.resize(479, 43)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormManageActionButton.sizePolicy().hasHeightForWidth())
        FormManageActionButton.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(FormManageActionButton)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonAdd = QtWidgets.QPushButton(FormManageActionButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAdd.sizePolicy().hasHeightForWidth())
        self.pushButtonAdd.setSizePolicy(sizePolicy)
        self.pushButtonAdd.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout.addWidget(self.pushButtonAdd)
        self.pushButtonEdit = QtWidgets.QPushButton(FormManageActionButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEdit.sizePolicy().hasHeightForWidth())
        self.pushButtonEdit.setSizePolicy(sizePolicy)
        self.pushButtonEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.horizontalLayout.addWidget(self.pushButtonEdit)
        self.pushButtonDiscount = QtWidgets.QPushButton(FormManageActionButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDiscount.sizePolicy().hasHeightForWidth())
        self.pushButtonDiscount.setSizePolicy(sizePolicy)
        self.pushButtonDiscount.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonDiscount.setObjectName("pushButtonDiscount")
        self.horizontalLayout.addWidget(self.pushButtonDiscount)
        self.pushButtonView = QtWidgets.QPushButton(FormManageActionButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonView.sizePolicy().hasHeightForWidth())
        self.pushButtonView.setSizePolicy(sizePolicy)
        self.pushButtonView.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonView.setObjectName("pushButtonView")
        self.horizontalLayout.addWidget(self.pushButtonView)
        self.pushButtonDelete = QtWidgets.QPushButton(FormManageActionButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDelete.sizePolicy().hasHeightForWidth())
        self.pushButtonDelete.setSizePolicy(sizePolicy)
        self.pushButtonDelete.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        self.pushButtonVoid = QtWidgets.QPushButton(FormManageActionButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonVoid.sizePolicy().hasHeightForWidth())
        self.pushButtonVoid.setSizePolicy(sizePolicy)
        self.pushButtonVoid.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonVoid.setObjectName("pushButtonVoid")
        self.horizontalLayout.addWidget(self.pushButtonVoid)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(FormManageActionButton)
        QtCore.QMetaObject.connectSlotsByName(FormManageActionButton)

    def retranslateUi(self, FormManageActionButton):
        _translate = QtCore.QCoreApplication.translate
        FormManageActionButton.setWindowTitle(_translate("FormManageActionButton", "Form"))
        self.pushButtonAdd.setToolTip(_translate("FormManageActionButton", "<html><head/><body><p>Add</p></body></html>"))
        self.pushButtonAdd.setText(_translate("FormManageActionButton", "Add"))
        self.pushButtonEdit.setToolTip(_translate("FormManageActionButton", "<html><head/><body><p>Edit</p></body></html>"))
        self.pushButtonEdit.setText(_translate("FormManageActionButton", "Edit"))
        self.pushButtonDiscount.setToolTip(_translate("FormManageActionButton", "<html><head/><body><p>Discount</p></body></html>"))
        self.pushButtonDiscount.setText(_translate("FormManageActionButton", "Discount"))
        self.pushButtonView.setToolTip(_translate("FormManageActionButton", "<html><head/><body><p>View</p></body></html>"))
        self.pushButtonView.setText(_translate("FormManageActionButton", "View"))
        self.pushButtonDelete.setToolTip(_translate("FormManageActionButton", "<html><head/><body><p>Delete</p></body></html>"))
        self.pushButtonDelete.setText(_translate("FormManageActionButton", "Delete"))
        self.pushButtonVoid.setToolTip(_translate("FormManageActionButton", "<html><head/><body><p>Void</p></body></html>"))
        self.pushButtonVoid.setText(_translate("FormManageActionButton", "Void"))
