# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\raccoondale\Documents\Personal\Git\mts-pos\app\views\templates\generated\ManageUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormManageUser(object):
    def setupUi(self, FormManageUser):
        FormManageUser.setObjectName("FormManageUser")
        FormManageUser.resize(897, 486)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(FormManageUser)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditFilter = QtWidgets.QLineEdit(FormManageUser)
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout.addWidget(self.lineEditFilter)
        self.pushButtonFilter = QtWidgets.QPushButton(FormManageUser)
        self.pushButtonFilter.setObjectName("pushButtonFilter")
        self.horizontalLayout.addWidget(self.pushButtonFilter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgetData = QtWidgets.QTableWidget(FormManageUser)
        self.tableWidgetData.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetData.setAlternatingRowColors(True)
        self.tableWidgetData.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetData.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidgetData.setShowGrid(False)
        self.tableWidgetData.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetData.setWordWrap(False)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(8)
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
        self.tableWidgetData.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetData.verticalHeader().setVisible(False)
        self.tableWidgetData.verticalHeader().setDefaultSectionSize(50)
        self.tableWidgetData.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidgetData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonPrev = QtWidgets.QPushButton(FormManageUser)
        self.pushButtonPrev.setEnabled(False)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout_2.addWidget(self.pushButtonPrev)
        self.labelPageIndicator = QtWidgets.QLabel(FormManageUser)
        self.labelPageIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPageIndicator.setObjectName("labelPageIndicator")
        self.horizontalLayout_2.addWidget(self.labelPageIndicator)
        self.pushButtonNext = QtWidgets.QPushButton(FormManageUser)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.frameRegister = QtWidgets.QFrame(FormManageUser)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 436, 427))
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
        self.lineEditUserName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditUserName)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditPassword = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditFullName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditFullName.setObjectName("lineEditFullName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditFullName)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dateEditBirthDate = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEditBirthDate.setCalendarPopup(True)
        self.dateEditBirthDate.setObjectName("dateEditBirthDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateEditBirthDate)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEditMobileNumber = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditMobileNumber.setObjectName("lineEditMobileNumber")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditMobileNumber)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBoxAccessLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxAccessLevel.setObjectName("comboBoxAccessLevel")
        self.comboBoxAccessLevel.addItem("")
        self.comboBoxAccessLevel.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBoxAccessLevel)
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

        self.retranslateUi(FormManageUser)
        QtCore.QMetaObject.connectSlotsByName(FormManageUser)

    def retranslateUi(self, FormManageUser):
        _translate = QtCore.QCoreApplication.translate
        FormManageUser.setWindowTitle(_translate("FormManageUser", "Manage user"))
        self.pushButtonFilter.setText(_translate("FormManageUser", "Filter"))
        self.tableWidgetData.setSortingEnabled(False)
        item = self.tableWidgetData.verticalHeaderItem(0)
        item.setText(_translate("FormManageUser", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(1)
        item.setText(_translate("FormManageUser", "New Row"))
        item = self.tableWidgetData.verticalHeaderItem(2)
        item.setText(_translate("FormManageUser", "New Row"))
        item = self.tableWidgetData.horizontalHeaderItem(0)
        item.setText(_translate("FormManageUser", "Action"))
        item = self.tableWidgetData.horizontalHeaderItem(1)
        item.setText(_translate("FormManageUser", "UserName"))
        item = self.tableWidgetData.horizontalHeaderItem(2)
        item.setText(_translate("FormManageUser", "Password"))
        item = self.tableWidgetData.horizontalHeaderItem(3)
        item.setText(_translate("FormManageUser", "FullName"))
        item = self.tableWidgetData.horizontalHeaderItem(4)
        item.setText(_translate("FormManageUser", "BirthDate"))
        item = self.tableWidgetData.horizontalHeaderItem(5)
        item.setText(_translate("FormManageUser", "MobileNumber"))
        item = self.tableWidgetData.horizontalHeaderItem(6)
        item.setText(_translate("FormManageUser", "AccessLevel"))
        item = self.tableWidgetData.horizontalHeaderItem(7)
        item.setText(_translate("FormManageUser", "UpdateTs"))
        self.pushButtonPrev.setText(_translate("FormManageUser", "Prev"))
        self.labelPageIndicator.setText(_translate("FormManageUser", "<CurrentPage>/<TotalPage>"))
        self.pushButtonNext.setText(_translate("FormManageUser", "Next"))
        self.label_8.setText(_translate("FormManageUser", "Organization"))
        self.label_3.setText(_translate("FormManageUser", "Username"))
        self.label_4.setText(_translate("FormManageUser", "Password"))
        self.label_2.setText(_translate("FormManageUser", "Full name"))
        self.label_5.setText(_translate("FormManageUser", "Birthdate"))
        self.dateEditBirthDate.setDisplayFormat(_translate("FormManageUser", "yyyy-MM-dd"))
        self.label_6.setText(_translate("FormManageUser", "Mobile number"))
        self.label_7.setText(_translate("FormManageUser", "Level"))
        self.comboBoxAccessLevel.setItemText(0, _translate("FormManageUser", "1"))
        self.comboBoxAccessLevel.setItemText(1, _translate("FormManageUser", "2"))
        self.pushButtonClear.setText(_translate("FormManageUser", "Clear"))
        self.pushButtonAdd.setText(_translate("FormManageUser", "Add"))
