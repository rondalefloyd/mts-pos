# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\EditItem.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogEditItem(object):
    def setupUi(self, DialogEditItem):
        DialogEditItem.setObjectName("DialogEditItem")
        DialogEditItem.resize(699, 720)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogEditItem)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(DialogEditItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.scrollArea = QtWidgets.QScrollArea(DialogEditItem)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 650))
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
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line_2)
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
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.comboBoxSupplierName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxSupplierName.setEditable(True)
        self.comboBoxSupplierName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxSupplierName.setObjectName("comboBoxSupplierName")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBoxSupplierName)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.comboBoxSalesGroupName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxSalesGroupName.setEnabled(False)
        self.comboBoxSalesGroupName.setEditable(True)
        self.comboBoxSalesGroupName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxSalesGroupName.setObjectName("comboBoxSalesGroupName")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.comboBoxSalesGroupName)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEditCapital = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditCapital.setObjectName("lineEditCapital")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEditCapital)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditPrice = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditPrice.setObjectName("lineEditPrice")
        self.horizontalLayout_3.addWidget(self.lineEditPrice)
        self.checkBoxApplyPromo = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBoxApplyPromo.setObjectName("checkBoxApplyPromo")
        self.horizontalLayout_3.addWidget(self.checkBoxApplyPromo)
        self.formLayout.setLayout(10, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.dateEditEffectiveDate = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEditEffectiveDate.setCalendarPopup(True)
        self.dateEditEffectiveDate.setObjectName("dateEditEffectiveDate")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.dateEditEffectiveDate)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.line_4)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.comboBoxPromoName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxPromoName.setEnabled(False)
        self.comboBoxPromoName.setEditable(True)
        self.comboBoxPromoName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxPromoName.setObjectName("comboBoxPromoName")
        self.comboBoxPromoName.addItem("")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.comboBoxPromoName)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditDiscountRate = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditDiscountRate.setEnabled(False)
        self.lineEditDiscountRate.setObjectName("lineEditDiscountRate")
        self.horizontalLayout_2.addWidget(self.lineEditDiscountRate)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.lineEditDiscount = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditDiscount.setEnabled(False)
        self.lineEditDiscount.setObjectName("lineEditDiscount")
        self.horizontalLayout_2.addWidget(self.lineEditDiscount)
        self.formLayout.setLayout(14, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEditNewPrice = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditNewPrice.setEnabled(False)
        self.lineEditNewPrice.setObjectName("lineEditNewPrice")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.lineEditNewPrice)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.dateEditStartDate = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEditStartDate.setEnabled(False)
        self.dateEditStartDate.setCalendarPopup(True)
        self.dateEditStartDate.setObjectName("dateEditStartDate")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.dateEditStartDate)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.dateEditEndDate = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEditEndDate.setEnabled(False)
        self.dateEditEndDate.setCalendarPopup(True)
        self.dateEditEndDate.setObjectName("dateEditEndDate")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.dateEditEndDate)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogEditItem)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.pushButtonSave = QtWidgets.QPushButton(DialogEditItem)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogEditItem)
        QtCore.QMetaObject.connectSlotsByName(DialogEditItem)
        DialogEditItem.setTabOrder(self.scrollArea, self.pushButtonCancel)
        DialogEditItem.setTabOrder(self.pushButtonCancel, self.pushButtonSave)

    def retranslateUi(self, DialogEditItem):
        _translate = QtCore.QCoreApplication.translate
        DialogEditItem.setWindowTitle(_translate("DialogEditItem", "Sign up"))
        self.label_6.setText(_translate("DialogEditItem", "MTS POS"))
        self.label.setText(_translate("DialogEditItem", "Item name"))
        self.checkBoxTrackInventory.setText(_translate("DialogEditItem", "Track inventory"))
        self.label_2.setText(_translate("DialogEditItem", "Barcode"))
        self.label_3.setText(_translate("DialogEditItem", "Expiry date"))
        self.dateEditExpireDate.setDisplayFormat(_translate("DialogEditItem", "yyyy-MM-dd"))
        self.label_4.setText(_translate("DialogEditItem", "Type"))
        self.label_5.setText(_translate("DialogEditItem", "Brand"))
        self.label_9.setText(_translate("DialogEditItem", "Supplier"))
        self.label_12.setText(_translate("DialogEditItem", "Sale group"))
        self.label_10.setText(_translate("DialogEditItem", "Capital"))
        self.label_8.setText(_translate("DialogEditItem", "Price"))
        self.checkBoxApplyPromo.setText(_translate("DialogEditItem", "Apply promo"))
        self.label_7.setText(_translate("DialogEditItem", "Effective date"))
        self.dateEditEffectiveDate.setDisplayFormat(_translate("DialogEditItem", "yyyy-MM-dd"))
        self.label_13.setText(_translate("DialogEditItem", "Promo name"))
        self.comboBoxPromoName.setItemText(0, _translate("DialogEditItem", "N/A"))
        self.label_11.setText(_translate("DialogEditItem", "Discount rate"))
        self.label_17.setText(_translate("DialogEditItem", "="))
        self.label_14.setText(_translate("DialogEditItem", "New price"))
        self.label_15.setText(_translate("DialogEditItem", "Start date"))
        self.dateEditStartDate.setDisplayFormat(_translate("DialogEditItem", "yyyy-MM-dd"))
        self.label_16.setText(_translate("DialogEditItem", "End date"))
        self.dateEditEndDate.setDisplayFormat(_translate("DialogEditItem", "yyyy-MM-dd"))
        self.pushButtonCancel.setText(_translate("DialogEditItem", "Cancel"))
        self.pushButtonSave.setText(_translate("DialogEditItem", "Save"))
