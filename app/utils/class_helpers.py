import os, sys, math
from sqlalchemy import desc
from PyQt5.QtCore import QThread, pyqtSignal
from datetime import datetime

from app.utils.function_helpers import (
    getOneUserByUserId,
    getOneUserByUserNameAccessCode,
    getOneOrganizationByOrganizationId,
    getOneOrganizationByOrganizationName,
    getAllUserWithPaginationByKeyword,
    getAllUser,
    getAllOrganization,
    deleteUser,
    updateOrganization,
    updateUserActiveStatus,
    updateUser,
    addNewUser,
    addNewOrganization
)

class DatabaseHandlerThread(QThread):
    finished = pyqtSignal(dict)

    def __init__(self, functionName, widget, entry):
        super().__init__()
        self.functionName = functionName
        self.widget = widget
        self.entry = entry

    def run(self):
        match self.functionName:
            case 'getOneUserByUserId':
                result = getOneUserByUserId(self.widget, self.entry)
                
            case 'getOneUserByUserNameAccessCode':
                result = getOneUserByUserNameAccessCode(self.widget, self.entry)
                
            case 'getOneOrganizationByOrganizationId':
                result = getOneOrganizationByOrganizationId(self.widget, self.entry)
                
            case 'getOneOrganizationByOrganizationName':
                result = getOneOrganizationByOrganizationName(self.widget, self.entry)
                
            case 'getAllUserWithPaginationByKeyword':
                result = getAllUserWithPaginationByKeyword(self.widget, self.entry)
                
            case 'getAllUser':
                result = getAllUser(self.widget)
                
            case 'getAllOrganization':
                result = getAllOrganization(self.widget)
                
            case 'deleteUser':
                result = deleteUser(self.widget, self.entry)
                
            case 'updateOrganization':
                result = updateOrganization(self.widget, self.entry)
                
            case 'updateUserActiveStatus':
                result = updateUserActiveStatus(self.widget, self.entry)
                
            case 'updateUser':
                result = updateUser(self.widget, self.entry)
                
            case 'addNewUser':
                result = addNewUser(self.widget, self.entry)
                
            case 'addNewOrganization':
                result = addNewOrganization(self.widget, self.entry)
    
        self.finished.emit(result)