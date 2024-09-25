# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/mimoy/Documents/GitHub/mts-pos/app/views/templates/generated\Manage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5 import QtWidgets, QtCore, QtGui


class Ui_MainWindowManage(object):
    def setupUi(self, MainWindowManage):
        MainWindowManage.setObjectName("MainWindowManage")
        MainWindowManage.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindowManage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidgetManage = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidgetManage.setObjectName("stackedWidgetManage")
        self.pageSales = QtWidgets.QWidget()
        self.pageSales.setObjectName("pageSales")
        self.stackedWidgetManage.addWidget(self.pageSales)
        self.pageTransaction = QtWidgets.QWidget()
        self.pageTransaction.setObjectName("pageTransaction")
        self.stackedWidgetManage.addWidget(self.pageTransaction)
        self.pageItem = QtWidgets.QWidget()
        self.pageItem.setObjectName("pageItem")
        self.stackedWidgetManage.addWidget(self.pageItem)
        self.pageStock = QtWidgets.QWidget()
        self.pageStock.setObjectName("pageStock")
        self.stackedWidgetManage.addWidget(self.pageStock)
        self.pagePromo = QtWidgets.QWidget()
        self.pagePromo.setObjectName("pagePromo")
        self.stackedWidgetManage.addWidget(self.pagePromo)
        self.pageReward = QtWidgets.QWidget()
        self.pageReward.setObjectName("pageReward")
        self.stackedWidgetManage.addWidget(self.pageReward)
        self.pageMember = QtWidgets.QWidget()
        self.pageMember.setObjectName("pageMember")
        self.stackedWidgetManage.addWidget(self.pageMember)
        self.pageUser = QtWidgets.QWidget()
        self.pageUser.setObjectName("pageUser")
        self.stackedWidgetManage.addWidget(self.pageUser)
        self.verticalLayout.addWidget(self.stackedWidgetManage)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.labelFullName = QtWidgets.QLabel(self.centralwidget)
        self.labelFullName.setObjectName("labelFullName")
        self.horizontalLayout_4.addWidget(self.labelFullName)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.labelMobileNumber = QtWidgets.QLabel(self.centralwidget)
        self.labelMobileNumber.setObjectName("labelMobileNumber")
        self.horizontalLayout_5.addWidget(self.labelMobileNumber)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelDatabaseSource = QtWidgets.QLabel(self.centralwidget)
        self.labelDatabaseSource.setObjectName("labelDatabaseSource")
        self.horizontalLayout_3.addWidget(self.labelDatabaseSource)
        self.progressBarStorage = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarStorage.setProperty("value", 24)
        self.progressBarStorage.setObjectName("progressBarStorage")
        self.horizontalLayout_3.addWidget(self.progressBarStorage)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindowManage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowManage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage = QtWidgets.QMenu(self.menubar)
        self.menuManage.setObjectName("menuManage")
        self.menuItem = QtWidgets.QMenu(self.menuManage)
        self.menuItem.setObjectName("menuItem")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindowManage.setMenuBar(self.menubar)
        self.actionSales = QtWidgets.QAction(MainWindowManage)
        self.actionSales.setCheckable(True)
        self.actionSales.setObjectName("actionSales")
        self.actionTransaction = QtWidgets.QAction(MainWindowManage)
        self.actionTransaction.setCheckable(True)
        self.actionTransaction.setObjectName("actionTransaction")
        self.actionStock = QtWidgets.QAction(MainWindowManage)
        self.actionStock.setCheckable(True)
        self.actionStock.setObjectName("actionStock")
        self.actionPromo = QtWidgets.QAction(MainWindowManage)
        self.actionPromo.setCheckable(True)
        self.actionPromo.setObjectName("actionPromo")
        self.actionReward = QtWidgets.QAction(MainWindowManage)
        self.actionReward.setCheckable(True)
        self.actionReward.setObjectName("actionReward")
        self.actionMember = QtWidgets.QAction(MainWindowManage)
        self.actionMember.setCheckable(True)
        self.actionMember.setObjectName("actionMember")
        self.actionLogout = QtWidgets.QAction(MainWindowManage)
        self.actionLogout.setCheckable(False)
        self.actionLogout.setObjectName("actionLogout")
        self.actionUser = QtWidgets.QAction(MainWindowManage)
        self.actionUser.setCheckable(True)
        self.actionUser.setObjectName("actionUser")
        self.actionCurrentOrganization = QtWidgets.QAction(MainWindowManage)
        self.actionCurrentOrganization.setObjectName("actionCurrentOrganization")
        self.actionCurrentUser = QtWidgets.QAction(MainWindowManage)
        self.actionCurrentUser.setObjectName("actionCurrentUser")
        self.actionItem = QtWidgets.QAction(MainWindowManage)
        self.actionItem.setObjectName("actionItem")
        self.actionItemType = QtWidgets.QAction(MainWindowManage)
        self.actionItemType.setObjectName("actionItemType")
        self.actionBrand = QtWidgets.QAction(MainWindowManage)
        self.actionBrand.setObjectName("actionBrand")
        self.actionSupplier = QtWidgets.QAction(MainWindowManage)
        self.actionSupplier.setObjectName("actionSupplier")
        self.actionGeneral = QtWidgets.QAction(MainWindowManage)
        self.actionGeneral.setObjectName("actionGeneral")
        self.menuItem.addAction(self.actionGeneral)
        self.menuItem.addSeparator()
        self.menuItem.addAction(self.actionItem)
        self.menuItem.addAction(self.actionItemType)
        self.menuItem.addAction(self.actionBrand)
        self.menuItem.addAction(self.actionSupplier)
        self.menuManage.addAction(self.actionSales)
        self.menuManage.addAction(self.actionTransaction)
        self.menuManage.addSeparator()
        self.menuManage.addAction(self.menuItem.menuAction())
        self.menuManage.addAction(self.actionStock)
        self.menuManage.addAction(self.actionPromo)
        self.menuManage.addAction(self.actionReward)
        self.menuManage.addAction(self.actionMember)
        self.menuManage.addSeparator()
        self.menuManage.addAction(self.actionUser)
        self.menuManage.addSeparator()
        self.menuManage.addAction(self.actionLogout)
        self.menuSettings.addAction(self.actionCurrentOrganization)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionCurrentUser)
        self.menubar.addAction(self.menuManage.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindowManage)
        QtCore.QMetaObject.connectSlotsByName(MainWindowManage)

    def retranslateUi(self, MainWindowManage):
        _translate = QtCore.QCoreApplication.translate
        MainWindowManage.setWindowTitle(_translate("MainWindowManage", "Management"))
        self.label_2.setText(_translate("MainWindowManage", "User:"))
        self.labelFullName.setText(_translate("MainWindowManage", "<FullName>"))
        self.label.setText(_translate("MainWindowManage", "Mobile number:"))
        self.labelMobileNumber.setText(_translate("MainWindowManage", "<MobileNumber>"))
        self.labelDatabaseSource.setText(_translate("MainWindowManage", "<DatabaseSouce>"))
        self.menuManage.setTitle(_translate("MainWindowManage", "<PageName>"))
        self.menuItem.setTitle(_translate("MainWindowManage", "Product"))
        self.menuSettings.setTitle(_translate("MainWindowManage", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindowManage", "Help"))
        self.actionSales.setText(_translate("MainWindowManage", "Sale"))
        self.actionTransaction.setText(_translate("MainWindowManage", "Transaction"))
        self.actionStock.setText(_translate("MainWindowManage", "Stock"))
        self.actionPromo.setText(_translate("MainWindowManage", "Promo"))
        self.actionReward.setText(_translate("MainWindowManage", "Reward"))
        self.actionMember.setText(_translate("MainWindowManage", "Member"))
        self.actionLogout.setText(_translate("MainWindowManage", "Logout"))
        self.actionUser.setText(_translate("MainWindowManage", "User"))
        self.actionCurrentOrganization.setText(_translate("MainWindowManage", "<OrganizationName>"))
        self.actionCurrentUser.setText(_translate("MainWindowManage", "<UserName>"))
        self.actionItem.setText(_translate("MainWindowManage", "Item"))
        self.actionItemType.setText(_translate("MainWindowManage", "ItemType"))
        self.actionBrand.setText(_translate("MainWindowManage", "Brand"))
        self.actionSupplier.setText(_translate("MainWindowManage", "Supplier"))
        self.actionGeneral.setText(_translate("MainWindowManage", "General"))
