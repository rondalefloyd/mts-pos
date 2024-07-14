import os, sys, math
from sqlalchemy import desc
from PyQt5.QtCore import QThread, pyqtSignal
from datetime import datetime

from app.utils.database_operation import (
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

class DatabaseOperationThread(QThread):
    finished = pyqtSignal(object)

    def __init__(self, widget, functionName, entry):
        super().__init__()
        self.widget = widget
        self.functionName = functionName
        self.entry = entry

        self.start()
        
    def run(self):
        if self.functionName == 'getOneUserByUserId':
            result = getOneUserByUserId(self.widget, self.entry)
        
        elif self.functionName == 'getOneUserByUserNameAccessCode':
            result = getOneUserByUserNameAccessCode(self.widget, self.entry)
        
        elif self.functionName == 'getOneOrganizationByOrganizationId':
            result = getOneOrganizationByOrganizationId(self.widget, self.entry)
        
        elif self.functionName == 'getOneOrganizationByOrganizationName':
            result = getOneOrganizationByOrganizationName(self.widget, self.entry)
        
        elif self.functionName == 'getAllUserWithPaginationByKeyword':
            result = getAllUserWithPaginationByKeyword(self.widget, self.entry)
        
        elif self.functionName == 'getAllUser':
            result = getAllUser(self.widget)
        
        elif self.functionName == 'getAllOrganization':
            result = getAllOrganization(self.widget)
        
        elif self.functionName == 'deleteUser':
            result = deleteUser(self.widget, self.entry)
        
        elif self.functionName == 'updateOrganization':
            result = updateOrganization(self.widget, self.entry)
        
        elif self.functionName == 'updateUserActiveStatus':
            result = updateUserActiveStatus(self.widget, self.entry)
        
        elif self.functionName == 'updateUser':
            result = updateUser(self.widget, self.entry)
        
        elif self.functionName == 'addNewUser':
            result = addNewUser(self.widget, self.entry)
        
        elif self.functionName == 'addNewOrganization':
            result = addNewOrganization(self.widget, self.entry)

            
        self.finished.emit(result)

