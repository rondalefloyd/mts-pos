# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\raccoondale\Documents\Personal\Git\mts-pos\app\views\templates\ManagePromo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormManagePromo(object):
    def setupUi(self, FormManagePromo):
        FormManagePromo.setObjectName("FormManagePromo")
        FormManagePromo.resize(738, 407)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(FormManagePromo)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditFilter = QtWidgets.QLineEdit(FormManagePromo)
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout.addWidget(self.lineEditFilter)
        self.pushButtonFilter = QtWidgets.QPushButton(FormManagePromo)
        self.pushButtonFilter.setObjectName("pushButtonFilter")
        self.horizontalLayout.addWidget(self.pushButtonFilter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgetData = QtWidgets.QTableWidget(FormManagePromo)
        self.tableWidgetData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetData.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setShowGrid(False)
        self.tableWidgetData.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetData.setWordWrap(False)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(5)
        self.tableWidgetData.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(4, item)
        self.tableWidgetData.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetData.verticalHeader().setVisible(False)
        self.tableWidgetData.verticalHeader().setDefaultSectionSize(50)
        self.tableWidgetData.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidgetData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonPrev = QtWidgets.QPushButton(FormManagePromo)
        self.pushButtonPrev.setEnabled(False)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout_2.addWidget(self.pushButtonPrev)
        self.labelPageIndicator = QtWidgets.QLabel(FormManagePromo)
        self.labelPageIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPageIndicator.setObjectName("labelPageIndicator")
        self.horizontalLayout_2.addWidget(self.labelPageIndicator)
        self.pushButtonNext = QtWidgets.QPushButton(FormManagePromo)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.frameRegister = QtWidgets.QFrame(FormManagePromo)
        self.frameRegister.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frameRegister.setObjectName("frameRegister")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameRegister)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frameRegister)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 311, 348))
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
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.widget = QtWidgets.QWidget(self.frameRegister)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(119, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButtonClear = QtWidgets.QPushButton(self.widget)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_3.addWidget(self.pushButtonClear)
        self.pushButtonAdd = QtWidgets.QPushButton(self.widget)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout_3.addWidget(self.pushButtonAdd)
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalLayout_4.addWidget(self.frameRegister)

        self.retranslateUi(FormManagePromo)
        QtCore.QMetaObject.connectSlotsByName(FormManagePromo)

    def retranslateUi(self, FormManagePromo):
        _translate = QtCore.QCoreApplication.translate
        FormManagePromo.setWindowTitle(_translate("FormManagePromo", "Manage promo"))
        self.pushButtonFilter.setText(_translate("FormManagePromo", "Filter"))
        self.tableWidgetData.setSortingEnabled(False)
        item = self.tableWidgetData.verticalHeaderItem(0)
        item.setText(_translate("FormManagePromo", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(1)
        item.setText(_translate("FormManagePromo", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(2)
        item.setText(_translate("FormManagePromo", "New Row"))
        item = self.tableWidgetData.horizontalHeaderItem(0)
        item.setText(_translate("FormManagePromo", "Action"))
        item = self.tableWidgetData.horizontalHeaderItem(1)
        item.setText(_translate("FormManagePromo", "PromoName"))
        item = self.tableWidgetData.horizontalHeaderItem(2)
        item.setText(_translate("FormManagePromo", "DiscountRate"))
        item = self.tableWidgetData.horizontalHeaderItem(3)
        item.setText(_translate("FormManagePromo", "Description"))
        item = self.tableWidgetData.horizontalHeaderItem(4)
        item.setText(_translate("FormManagePromo", "UpdateTs"))
        self.pushButtonPrev.setText(_translate("FormManagePromo", "Prev"))
        self.labelPageIndicator.setText(_translate("FormManagePromo", "<CurrentPage>/<TotalPage>"))
        self.pushButtonNext.setText(_translate("FormManagePromo", "Next"))
        self.label_3.setText(_translate("FormManagePromo", "Promo name"))
        self.label_2.setText(_translate("FormManagePromo", "Discount rate"))
        self.label.setText(_translate("FormManagePromo", "Description"))
        self.pushButtonClear.setText(_translate("FormManagePromo", "Clear"))
        self.pushButtonAdd.setText(_translate("FormManagePromo", "Add"))
