from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import os, sys, logging
sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.helpers.validator import *
from app.utils.helpers.formatter import *

class QPushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        QTimer.singleShot(0, self._executeTask)

    def _executeTask(self):
        objectName = self.objectName()
        
        

class QTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        QTimer.singleShot(0, self._executeTask)

    def _executeTask(self):
        objectName = self.objectName()
        
        self.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        self.horizontalHeaderItem(0).setText("")
        self.horizontalHeader().setStretchLastSection(True)
        
        if objectName in ['tableWidgetData']:
            self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        elif objectName in ['tableWidgetOrderItem']:
            self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            pass
        
class QTableWidgetItem(QTableWidgetItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        QTimer.singleShot(0, self._executeTask)

    def _executeTask(self):
        pass
        
        
class QLabel(QLabel):
    def __init__(self, parent=None, objectName="", text=""):
        super().__init__(parent)
        
        self.setObjectName(objectName)
        self.setText(text)
        
        QTimer.singleShot(0, self._executeTask)

    def _executeTask(self):
        objectName = self.objectName()
        
        if objectName in ['tableItem']:
            # self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        pass
        
        
class QLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        QTimer.singleShot(0, self._executeTask)

    def _executeTask(self):
        objectName = self.objectName()
        
        if objectName in [
            'lineEditOrganizationName',
            'lineEditItemName',
            'comboBoxBrandName',
            'comboBoxSupplierName',
            'comboBoxPromoName',
            'lineEditMemberName',
            'lineEditPromoName',
            'lineEditRewardName',
        ]:
            self.setValidator(withSpaceTextDigitFormatValidator())
        
        if objectName in ['lineEditAddress']:
            self.setValidator(addressFormatValidator())
        if objectName in ['lineEditMobileNumber']:
            self.setValidator(mobileNumberValidator())
        if objectName in ['lineEditUserName']:
            self.setValidator(nonSpaceTextWithDigitFormatValidator())
        if objectName in ['lineEditFullName']:
            self.setValidator(fullNameValidator())
        if objectName in ['lineEditBarcode']:
            self.setValidator(withSpaceTextDigitSymbolFormatValidator())
        if objectName in ['comboBoxItemTypeName']:
            self.setValidator(nonSpaceTextFormatValidator())
        if objectName in ['lineEditTaxId']:
            self.setValidator(tinValidator())
        
        
        if objectName in [
            'lineEditCost',
            'lineEditPrice',
            'lineEditPoints',
            'lineEditDiscountRate',
            'lineEditRetailPrice',
            'lineEditWholesalePrice',
            'lineEditCash',
            'lineEditTarget',
        ]:
            self.setValidator(floatFormatValidator())
        
        if objectName in [
            'lineEditOnHand',
            'lineEditAvailable',
        ]:
            self.setValidator(intFormatValidator())
        
            
        
        
        
        
        