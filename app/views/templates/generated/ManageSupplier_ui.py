# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\generated\ManageSupplier.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormManageSupplier(object):
    def setupUi(self, FormManageSupplier):
        FormManageSupplier.setObjectName("FormManageSupplier")
        FormManageSupplier.resize(738, 439)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(FormManageSupplier)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditFilter = QtWidgets.QLineEdit(FormManageSupplier)
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout.addWidget(self.lineEditFilter)
        self.pushButtonFilter = QtWidgets.QPushButton(FormManageSupplier)
        self.pushButtonFilter.setObjectName("pushButtonFilter")
        self.horizontalLayout.addWidget(self.pushButtonFilter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgetData = QtWidgets.QTableWidget(FormManageSupplier)
        self.tableWidgetData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetData.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setShowGrid(False)
        self.tableWidgetData.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetData.setWordWrap(False)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(3)
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
        self.tableWidgetData.horizontalHeader().setStretchLastSection(False)
        self.tableWidgetData.verticalHeader().setVisible(False)
        self.tableWidgetData.verticalHeader().setDefaultSectionSize(50)
        self.tableWidgetData.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidgetData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonPrev = QtWidgets.QPushButton(FormManageSupplier)
        self.pushButtonPrev.setEnabled(False)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout_2.addWidget(self.pushButtonPrev)
        self.labelPageIndicator = QtWidgets.QLabel(FormManageSupplier)
        self.labelPageIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPageIndicator.setObjectName("labelPageIndicator")
        self.horizontalLayout_2.addWidget(self.labelPageIndicator)
        self.pushButtonNext = QtWidgets.QPushButton(FormManageSupplier)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.frameRegister = QtWidgets.QFrame(FormManageSupplier)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 311, 380))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditSupplierName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditSupplierName.setObjectName("lineEditSupplierName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditSupplierName)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.widget = QtWidgets.QWidget(self.frameRegister)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.pushButtonClear = QtWidgets.QPushButton(self.widget)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_5.addWidget(self.pushButtonClear)
        self.pushButtonAdd = QtWidgets.QPushButton(self.widget)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout_5.addWidget(self.pushButtonAdd)
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalLayout_4.addWidget(self.frameRegister)

        self.retranslateUi(FormManageSupplier)
        QtCore.QMetaObject.connectSlotsByName(FormManageSupplier)

    def retranslateUi(self, FormManageSupplier):
        _translate = QtCore.QCoreApplication.translate
        FormManageSupplier.setWindowTitle(_translate("FormManageSupplier", "Manage supplier"))
        self.pushButtonFilter.setText(_translate("FormManageSupplier", "Filter"))
        self.tableWidgetData.setSortingEnabled(False)
        item = self.tableWidgetData.verticalHeaderItem(0)
        item.setText(_translate("FormManageSupplier", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(1)
        item.setText(_translate("FormManageSupplier", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(2)
        item.setText(_translate("FormManageSupplier", "New Row"))
        item = self.tableWidgetData.horizontalHeaderItem(0)
        item.setText(_translate("FormManageSupplier", "Action"))
        item = self.tableWidgetData.horizontalHeaderItem(1)
        item.setText(_translate("FormManageSupplier", "SupplierName"))
        item = self.tableWidgetData.horizontalHeaderItem(2)
        item.setText(_translate("FormManageSupplier", "UpdateTs"))
        self.pushButtonPrev.setText(_translate("FormManageSupplier", "Prev"))
        self.labelPageIndicator.setText(_translate("FormManageSupplier", "<CurrentPage>/<TotalPage>"))
        self.pushButtonNext.setText(_translate("FormManageSupplier", "Next"))
        self.label_3.setText(_translate("FormManageSupplier", "Supplier name"))
        self.pushButtonClear.setText(_translate("FormManageSupplier", "Clear"))
        self.pushButtonAdd.setText(_translate("FormManageSupplier", "Add"))
