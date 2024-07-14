import os, sys, math
from sqlalchemy import desc
from PyQt5.QtWidgets import QWidget, QMessageBox
from datetime import datetime

sys.path.append(os.path.abspath(''))
from app.models.model_association import session, User, Organization, Authentication
from app.controllers.widget.Loading import LoadingController

def getManageTypeByIndex(index:int):
    match index:
        case 0:
            return 'Sales'
        case 1:
            return 'Transaction'
        case 2:
            return 'Item'
        case 3:
            return 'Stock'
        case 4:
            return 'Promo'
        case 5:
            return 'Reward'
        case 6:
            return 'Member'
        case 7:
            return 'User'

def updatePaginationInfo(parent:QWidget):
    parent.labelPageIndicator.setText(f"{parent.currentPage}/{parent.totalPages}")
    parent.pushButtonNext.setEnabled(parent.currentPage < parent.totalPages)
    parent.pushButtonPrev.setEnabled(parent.currentPage > 1)
