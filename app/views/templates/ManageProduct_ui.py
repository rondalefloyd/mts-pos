# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/mimoy/Documents/GitHub/mts-pos/app/views/templates/generated\ManageProduct.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_FormManageProduct(object):
    def setupUi(self, FormManageProduct):
        FormManageProduct.setObjectName("FormManageProduct")
        FormManageProduct.resize(994, 583)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(FormManageProduct)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditFilter = QtWidgets.QLineEdit(FormManageProduct)
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout.addWidget(self.lineEditFilter)
        self.pushButtonFilter = QtWidgets.QPushButton(FormManageProduct)
        self.pushButtonFilter.setObjectName("pushButtonFilter")
        self.horizontalLayout.addWidget(self.pushButtonFilter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgetData = QtWidgets.QTableWidget(FormManageProduct)
        self.tableWidgetData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetData.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setShowGrid(False)
        self.tableWidgetData.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetData.setWordWrap(False)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(14)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetData.setHorizontalHeaderItem(13, item)
        self.tableWidgetData.horizontalHeader().setStretchLastSection(False)
        self.tableWidgetData.verticalHeader().setVisible(False)
        self.tableWidgetData.verticalHeader().setDefaultSectionSize(50)
        self.tableWidgetData.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidgetData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonPrev = QtWidgets.QPushButton(FormManageProduct)
        self.pushButtonPrev.setEnabled(False)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout_2.addWidget(self.pushButtonPrev)
        self.labelPageIndicator = QtWidgets.QLabel(FormManageProduct)
        self.labelPageIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPageIndicator.setObjectName("labelPageIndicator")
        self.horizontalLayout_2.addWidget(self.labelPageIndicator)
        self.pushButtonNext = QtWidgets.QPushButton(FormManageProduct)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(FormManageProduct)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)
        self.frameRegister = QtWidgets.QFrame(FormManageProduct)
        self.frameRegister.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frameRegister.setObjectName("frameRegister")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameRegister)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.pushButtonLoad = QtWidgets.QPushButton(self.frameRegister)
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.horizontalLayout_5.addWidget(self.pushButtonLoad)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.scrollArea = QtWidgets.QScrollArea(self.frameRegister)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 462, 485))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEditItemName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditItemName.setObjectName("lineEditItemName")
        self.horizontalLayout_7.addWidget(self.lineEditItemName)
        self.checkBoxTrackInventory = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBoxTrackInventory.setObjectName("checkBoxTrackInventory")
        self.horizontalLayout_7.addWidget(self.checkBoxTrackInventory)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditBarcode = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditBarcode.setObjectName("lineEditBarcode")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditBarcode)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.dateEditExpireDate = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEditExpireDate.setCalendarPopup(True)
        self.dateEditExpireDate.setObjectName("dateEditExpireDate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEditExpireDate)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBoxItemTypeName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxItemTypeName.setEditable(True)
        self.comboBoxItemTypeName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxItemTypeName.setObjectName("comboBoxItemTypeName")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBoxItemTypeName)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBoxBrandName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxBrandName.setEditable(True)
        self.comboBoxBrandName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxBrandName.setObjectName("comboBoxBrandName")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBoxBrandName)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.comboBoxSupplierName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxSupplierName.setEditable(True)
        self.comboBoxSupplierName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxSupplierName.setObjectName("comboBoxSupplierName")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBoxSupplierName)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEditCapital = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditCapital.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditCapital.setObjectName("lineEditCapital")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEditCapital)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEditRetailPrice = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditRetailPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditRetailPrice.setObjectName("lineEditRetailPrice")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEditRetailPrice)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEditWholesalePrice = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditWholesalePrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditWholesalePrice.setObjectName("lineEditWholesalePrice")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEditWholesalePrice)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.dateEditEffectiveDate = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEditEffectiveDate.setCalendarPopup(True)
        self.dateEditEffectiveDate.setObjectName("dateEditEffectiveDate")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.dateEditEffectiveDate)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.pushButtonClear = QtWidgets.QPushButton(self.frameRegister)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_3.addWidget(self.pushButtonClear)
        self.pushButtonAdd = QtWidgets.QPushButton(self.frameRegister)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout_3.addWidget(self.pushButtonAdd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addWidget(self.frameRegister)

        self.retranslateUi(FormManageProduct)
        QtCore.QMetaObject.connectSlotsByName(FormManageProduct)

    def retranslateUi(self, FormManageProduct):
        _translate = QtCore.QCoreApplication.translate
        FormManageProduct.setWindowTitle(_translate("FormManageProduct", "Manage product"))
        self.pushButtonFilter.setText(_translate("FormManageProduct", "Filter"))
        self.tableWidgetData.setSortingEnabled(False)
        item = self.tableWidgetData.verticalHeaderItem(0)
        item.setText(_translate("FormManageProduct", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(1)
        item.setText(_translate("FormManageProduct", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(2)
        item.setText(_translate("FormManageProduct", "New Row"))
        item = self.tableWidgetData.horizontalHeaderItem(0)
        item.setText(_translate("FormManageProduct", "Action"))
        item = self.tableWidgetData.horizontalHeaderItem(1)
        item.setText(_translate("FormManageProduct", "ItemName"))
        item = self.tableWidgetData.horizontalHeaderItem(2)
        item.setText(_translate("FormManageProduct", "Barcode"))
        item = self.tableWidgetData.horizontalHeaderItem(3)
        item.setText(_translate("FormManageProduct", "ExpireDate"))
        item = self.tableWidgetData.horizontalHeaderItem(4)
        item.setText(_translate("FormManageProduct", "ItemTypeName"))
        item = self.tableWidgetData.horizontalHeaderItem(5)
        item.setText(_translate("FormManageProduct", "BrandName"))
        item = self.tableWidgetData.horizontalHeaderItem(6)
        item.setText(_translate("FormManageProduct", "SupplierName"))
        item = self.tableWidgetData.horizontalHeaderItem(7)
        item.setText(_translate("FormManageProduct", "SalesGroupName"))
        item = self.tableWidgetData.horizontalHeaderItem(8)
        item.setText(_translate("FormManageProduct", "Capital"))
        item = self.tableWidgetData.horizontalHeaderItem(9)
        item.setText(_translate("FormManageProduct", "Price"))
        item = self.tableWidgetData.horizontalHeaderItem(10)
        item.setText(_translate("FormManageProduct", "Discount"))
        item = self.tableWidgetData.horizontalHeaderItem(11)
        item.setText(_translate("FormManageProduct", "EffectiveDate"))
        item = self.tableWidgetData.horizontalHeaderItem(12)
        item.setText(_translate("FormManageProduct", "PromoName"))
        item = self.tableWidgetData.horizontalHeaderItem(13)
        item.setText(_translate("FormManageProduct", "UpdateTs"))
        self.pushButtonPrev.setText(_translate("FormManageProduct", "Prev"))
        self.labelPageIndicator.setText(_translate("FormManageProduct", "<CurrentPage>/<TotalPage>"))
        self.pushButtonNext.setText(_translate("FormManageProduct", "Next"))
        self.pushButtonLoad.setText(_translate("FormManageProduct", "Load"))
        self.label.setText(_translate("FormManageProduct", "Item name"))
        self.checkBoxTrackInventory.setText(_translate("FormManageProduct", "Track inventory"))
        self.label_2.setText(_translate("FormManageProduct", "Barcode"))
        self.label_3.setText(_translate("FormManageProduct", "Expiry date"))
        self.dateEditExpireDate.setDisplayFormat(_translate("FormManageProduct", "yyyy-MM-dd"))
        self.label_4.setText(_translate("FormManageProduct", "Type"))
        self.label_5.setText(_translate("FormManageProduct", "Brand"))
        self.label_6.setText(_translate("FormManageProduct", "Supplier"))
        self.label_10.setText(_translate("FormManageProduct", "Capital"))
        self.label_8.setText(_translate("FormManageProduct", "Retail price"))
        self.label_11.setText(_translate("FormManageProduct", "Wholesale price"))
        self.label_7.setText(_translate("FormManageProduct", "Effective date"))
        self.dateEditEffectiveDate.setDisplayFormat(_translate("FormManageProduct", "yyyy-MM-dd"))
        self.pushButtonClear.setText(_translate("FormManageProduct", "Clear"))
        self.pushButtonAdd.setText(_translate("FormManageProduct", "Add"))
