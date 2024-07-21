import os, sys, math
from sqlalchemy import desc
from PyQt5.QtWidgets import QWidget

sys.path.append(os.path.abspath(''))
from app.models.model_association import User, Organization, Authentication
from app.controllers.Loading import LoadingController

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
        case _:
            return 'Unavailable'
