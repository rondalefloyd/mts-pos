# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mimoy\Documents\GitHub\mts-pos\app\views\templates\generated\Manage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowManage(object):
    def setupUi(self, MainWindowManage):
        MainWindowManage.setObjectName("MainWindowManage")
        MainWindowManage.resize(912, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindowManage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
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
        self.widgetStatusBar = QtWidgets.QWidget(self.centralwidget)
        self.widgetStatusBar.setObjectName("widgetStatusBar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetStatusBar)
        self.horizontalLayout_3.setContentsMargins(-1, 4, -1, 4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widgetStatusBar)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.labelFullName = QtWidgets.QLabel(self.widgetStatusBar)
        self.labelFullName.setObjectName("labelFullName")
        self.horizontalLayout_4.addWidget(self.labelFullName)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.widgetStatusBar)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.widgetStatusBar)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.labelMobileNumber = QtWidgets.QLabel(self.widgetStatusBar)
        self.labelMobileNumber.setObjectName("labelMobileNumber")
        self.horizontalLayout_5.addWidget(self.labelMobileNumber)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widgetStatusBar)
        MainWindowManage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowManage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 912, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage = QtWidgets.QMenu(self.menubar)
        self.menuManage.setObjectName("menuManage")
        self.menuProducts = QtWidgets.QMenu(self.menuManage)
        self.menuProducts.setObjectName("menuProducts")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindowManage.setMenuBar(self.menubar)
        self.actionSales = QtWidgets.QAction(MainWindowManage)
        self.actionSales.setCheckable(True)
        self.actionSales.setObjectName("actionSales")
        self.actionTransactions = QtWidgets.QAction(MainWindowManage)
        self.actionTransactions.setCheckable(True)
        self.actionTransactions.setObjectName("actionTransactions")
        self.actionStocks = QtWidgets.QAction(MainWindowManage)
        self.actionStocks.setCheckable(True)
        self.actionStocks.setObjectName("actionStocks")
        self.actionPromos = QtWidgets.QAction(MainWindowManage)
        self.actionPromos.setCheckable(True)
        self.actionPromos.setObjectName("actionPromos")
        self.actionRewards = QtWidgets.QAction(MainWindowManage)
        self.actionRewards.setCheckable(True)
        self.actionRewards.setObjectName("actionRewards")
        self.actionMembers = QtWidgets.QAction(MainWindowManage)
        self.actionMembers.setCheckable(True)
        self.actionMembers.setObjectName("actionMembers")
        self.actionLogout = QtWidgets.QAction(MainWindowManage)
        self.actionLogout.setCheckable(False)
        self.actionLogout.setObjectName("actionLogout")
        self.actionUsers = QtWidgets.QAction(MainWindowManage)
        self.actionUsers.setCheckable(True)
        self.actionUsers.setObjectName("actionUsers")
        self.actionCurrentOrganization = QtWidgets.QAction(MainWindowManage)
        self.actionCurrentOrganization.setObjectName("actionCurrentOrganization")
        self.actionCurrentUser = QtWidgets.QAction(MainWindowManage)
        self.actionCurrentUser.setObjectName("actionCurrentUser")
        self.actionItems = QtWidgets.QAction(MainWindowManage)
        self.actionItems.setCheckable(True)
        self.actionItems.setObjectName("actionItems")
        self.actionItemTypes = QtWidgets.QAction(MainWindowManage)
        self.actionItemTypes.setCheckable(True)
        self.actionItemTypes.setObjectName("actionItemTypes")
        self.actionBrands = QtWidgets.QAction(MainWindowManage)
        self.actionBrands.setCheckable(True)
        self.actionBrands.setObjectName("actionBrands")
        self.actionSuppliers = QtWidgets.QAction(MainWindowManage)
        self.actionSuppliers.setCheckable(True)
        self.actionSuppliers.setObjectName("actionSuppliers")
        self.actionAll = QtWidgets.QAction(MainWindowManage)
        self.actionAll.setCheckable(True)
        self.actionAll.setObjectName("actionAll")
        self.menuProducts.addAction(self.actionAll)
        self.menuProducts.addSeparator()
        self.menuProducts.addAction(self.actionItems)
        self.menuProducts.addAction(self.actionItemTypes)
        self.menuProducts.addAction(self.actionBrands)
        self.menuProducts.addAction(self.actionSuppliers)
        self.menuManage.addAction(self.actionSales)
        self.menuManage.addAction(self.actionTransactions)
        self.menuManage.addSeparator()
        self.menuManage.addAction(self.menuProducts.menuAction())
        self.menuManage.addAction(self.actionStocks)
        self.menuManage.addAction(self.actionPromos)
        self.menuManage.addAction(self.actionRewards)
        self.menuManage.addAction(self.actionMembers)
        self.menuManage.addSeparator()
        self.menuManage.addAction(self.actionUsers)
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
        self.menuManage.setTitle(_translate("MainWindowManage", "<PageName>"))
        self.menuProducts.setTitle(_translate("MainWindowManage", "Products"))
        self.menuSettings.setTitle(_translate("MainWindowManage", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindowManage", "Help"))
        self.actionSales.setText(_translate("MainWindowManage", "Sales"))
        self.actionTransactions.setText(_translate("MainWindowManage", "Transactions"))
        self.actionStocks.setText(_translate("MainWindowManage", "Stocks"))
        self.actionPromos.setText(_translate("MainWindowManage", "Promos"))
        self.actionRewards.setText(_translate("MainWindowManage", "Rewards"))
        self.actionMembers.setText(_translate("MainWindowManage", "Members"))
        self.actionLogout.setText(_translate("MainWindowManage", "Logout"))
        self.actionUsers.setText(_translate("MainWindowManage", "Users"))
        self.actionCurrentOrganization.setText(_translate("MainWindowManage", "<OrganizationName>"))
        self.actionCurrentUser.setText(_translate("MainWindowManage", "<UserName>"))
        self.actionItems.setText(_translate("MainWindowManage", "Items"))
        self.actionItemTypes.setText(_translate("MainWindowManage", "Types"))
        self.actionBrands.setText(_translate("MainWindowManage", "Brands"))
        self.actionSuppliers.setText(_translate("MainWindowManage", "Suppliers"))
        self.actionAll.setText(_translate("MainWindowManage", "All"))
