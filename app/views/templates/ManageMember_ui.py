# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\ManageMember.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormManageMember(object):
    def setupUi(self, FormManageMember):
        FormManageMember.setObjectName("FormManageMember")
        FormManageMember.resize(994, 629)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(FormManageMember)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditFilter = QtWidgets.QLineEdit(FormManageMember)
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout.addWidget(self.lineEditFilter)
        self.pushButtonFilter = QtWidgets.QPushButton(FormManageMember)
        self.pushButtonFilter.setObjectName("pushButtonFilter")
        self.horizontalLayout.addWidget(self.pushButtonFilter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgetData = QtWidgets.QTableWidget(FormManageMember)
        self.tableWidgetData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(7)
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
        self.tableWidgetData.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetData.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidgetData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonPrev = QtWidgets.QPushButton(FormManageMember)
        self.pushButtonPrev.setEnabled(False)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout_2.addWidget(self.pushButtonPrev)
        self.labelPageIndicator = QtWidgets.QLabel(FormManageMember)
        self.labelPageIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPageIndicator.setObjectName("labelPageIndicator")
        self.horizontalLayout_2.addWidget(self.labelPageIndicator)
        self.pushButtonNext = QtWidgets.QPushButton(FormManageMember)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(FormManageMember)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(FormManageMember)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 476, 576))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBoxOrganizationName = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxOrganizationName.setEnabled(False)
        self.comboBoxOrganizationName.setEditable(True)
        self.comboBoxOrganizationName.setMaxVisibleItems(2147483647)
        self.comboBoxOrganizationName.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxOrganizationName.setObjectName("comboBoxOrganizationName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxOrganizationName)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditMemberName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditMemberName.setObjectName("lineEditMemberName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditMemberName)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dateEditBirthDate = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEditBirthDate.setCalendarPopup(True)
        self.dateEditBirthDate.setObjectName("dateEditBirthDate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEditBirthDate)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditAddress = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditAddress)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEditMobileNumber = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditMobileNumber.setObjectName("lineEditMobileNumber")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditMobileNumber)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButtonClear = QtWidgets.QPushButton(FormManageMember)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_3.addWidget(self.pushButtonClear)
        self.pushButtonAdd = QtWidgets.QPushButton(FormManageMember)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout_3.addWidget(self.pushButtonAdd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(FormManageMember)
        QtCore.QMetaObject.connectSlotsByName(FormManageMember)

    def retranslateUi(self, FormManageMember):
        _translate = QtCore.QCoreApplication.translate
        FormManageMember.setWindowTitle(_translate("FormManageMember", "Manage member"))
        self.pushButtonFilter.setText(_translate("FormManageMember", "Filter"))
        self.tableWidgetData.setSortingEnabled(False)
        item = self.tableWidgetData.verticalHeaderItem(0)
        item.setText(_translate("FormManageMember", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(1)
        item.setText(_translate("FormManageMember", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(2)
        item.setText(_translate("FormManageMember", "New Row"))
        item = self.tableWidgetData.horizontalHeaderItem(0)
        item.setText(_translate("FormManageMember", "Action"))
        item = self.tableWidgetData.horizontalHeaderItem(1)
        item.setText(_translate("FormManageMember", "MemberName"))
        item = self.tableWidgetData.horizontalHeaderItem(2)
        item.setText(_translate("FormManageMember", "BirthDate"))
        item = self.tableWidgetData.horizontalHeaderItem(3)
        item.setText(_translate("FormManageMember", "Address"))
        item = self.tableWidgetData.horizontalHeaderItem(4)
        item.setText(_translate("FormManageMember", "MobileNumber"))
        item = self.tableWidgetData.horizontalHeaderItem(5)
        item.setText(_translate("FormManageMember", "Points"))
        item = self.tableWidgetData.horizontalHeaderItem(6)
        item.setText(_translate("FormManageMember", "UpdateTs"))
        self.pushButtonPrev.setText(_translate("FormManageMember", "Prev"))
        self.labelPageIndicator.setText(_translate("FormManageMember", "<CurrentPage>/<TotalPage>"))
        self.pushButtonNext.setText(_translate("FormManageMember", "Next"))
        self.label_8.setText(_translate("FormManageMember", "Organization"))
        self.label_3.setText(_translate("FormManageMember", "Member name"))
        self.label_5.setText(_translate("FormManageMember", "Birthdate"))
        self.dateEditBirthDate.setDisplayFormat(_translate("FormManageMember", "yyyy-MM-dd"))
        self.label.setText(_translate("FormManageMember", "Address"))
        self.label_6.setText(_translate("FormManageMember", "Mobile number"))
        self.pushButtonClear.setText(_translate("FormManageMember", "Clear"))
        self.pushButtonAdd.setText(_translate("FormManageMember", "Add"))
