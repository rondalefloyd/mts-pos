# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\raccoondale\Documents\Personal\Git\mts-pos\app\views\templates\generated\ManageItem.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormManageItem(object):
    def setupUi(self, FormManageItem):
        FormManageItem.setObjectName("FormManageItem")
        FormManageItem.resize(738, 373)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(FormManageItem)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditFilter = QtWidgets.QLineEdit(FormManageItem)
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout.addWidget(self.lineEditFilter)
        self.pushButtonFilter = QtWidgets.QPushButton(FormManageItem)
        self.pushButtonFilter.setObjectName("pushButtonFilter")
        self.horizontalLayout.addWidget(self.pushButtonFilter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgetData = QtWidgets.QTableWidget(FormManageItem)
        self.tableWidgetData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetData.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setShowGrid(False)
        self.tableWidgetData.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetData.setWordWrap(False)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(9)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(8, item)
        self.tableWidgetData.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetData.verticalHeader().setVisible(False)
        self.tableWidgetData.verticalHeader().setDefaultSectionSize(50)
        self.tableWidgetData.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidgetData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonPrev = QtWidgets.QPushButton(FormManageItem)
        self.pushButtonPrev.setEnabled(False)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout_2.addWidget(self.pushButtonPrev)
        self.labelPageIndicator = QtWidgets.QLabel(FormManageItem)
        self.labelPageIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPageIndicator.setObjectName("labelPageIndicator")
        self.horizontalLayout_2.addWidget(self.labelPageIndicator)
        self.pushButtonNext = QtWidgets.QPushButton(FormManageItem)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.frameRegister = QtWidgets.QFrame(FormManageItem)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 311, 314))
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

        self.retranslateUi(FormManageItem)
        QtCore.QMetaObject.connectSlotsByName(FormManageItem)

    def retranslateUi(self, FormManageItem):
        _translate = QtCore.QCoreApplication.translate
        FormManageItem.setWindowTitle(_translate("FormManageItem", "Manage item"))
        self.pushButtonFilter.setText(_translate("FormManageItem", "Filter"))
        self.tableWidgetData.setSortingEnabled(False)
        item = self.tableWidgetData.verticalHeaderItem(0)
        item.setText(_translate("FormManageItem", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(1)
        item.setText(_translate("FormManageItem", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(2)
        item.setText(_translate("FormManageItem", "New Row"))
        item = self.tableWidgetData.horizontalHeaderItem(0)
        item.setText(_translate("FormManageItem", "Action"))
        item = self.tableWidgetData.horizontalHeaderItem(1)
        item.setText(_translate("FormManageItem", "ItemName"))
        item = self.tableWidgetData.horizontalHeaderItem(2)
        item.setText(_translate("FormManageItem", "Barcode"))
        item = self.tableWidgetData.horizontalHeaderItem(3)
        item.setText(_translate("FormManageItem", "ExpireDate"))
        item = self.tableWidgetData.horizontalHeaderItem(4)
        item.setText(_translate("FormManageItem", "ItemTypeName"))
        item = self.tableWidgetData.horizontalHeaderItem(5)
        item.setText(_translate("FormManageItem", "BrandName"))
        item = self.tableWidgetData.horizontalHeaderItem(6)
        item.setText(_translate("FormManageItem", "SupplierName"))
        item = self.tableWidgetData.horizontalHeaderItem(7)
        item.setText(_translate("FormManageItem", "SalesGroupName"))
        item = self.tableWidgetData.horizontalHeaderItem(8)
        item.setText(_translate("FormManageItem", "UpdateTs"))
        self.pushButtonPrev.setText(_translate("FormManageItem", "Prev"))
        self.labelPageIndicator.setText(_translate("FormManageItem", "<CurrentPage>/<TotalPage>"))
        self.pushButtonNext.setText(_translate("FormManageItem", "Next"))
        self.label_3.setText(_translate("FormManageItem", "Item name"))
        self.label_2.setText(_translate("FormManageItem", "Barcode"))
        self.label.setText(_translate("FormManageItem", "ExpireDate"))
        self.dateEditExpireDate.setDisplayFormat(_translate("FormManageItem", "yyyy-MM-dd"))
        self.label_4.setText(_translate("FormManageItem", "Type"))
        self.label_5.setText(_translate("FormManageItem", "Brand"))
        self.label_9.setText(_translate("FormManageItem", "Supplier"))
        self.label_12.setText(_translate("FormManageItem", "Sale group"))
        self.pushButtonClear.setText(_translate("FormManageItem", "Clear"))
        self.pushButtonAdd.setText(_translate("FormManageItem", "Add"))
