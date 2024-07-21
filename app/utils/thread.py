import os, sys, math, threading
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

sys.path.append(os.path.abspath(''))
from app.controllers.Loading import LoadingController
from app.utils.crud import (
    getOneUserByUserId,
    getOneUserByUserNameAccessCode,
    getOneOrganizationByOrganizationId,
    getOneOrganizationByOrganizationName,
    getAllUserWithPaginationByKeyword,
    getAllUser,
    getAllOrganization,
    deleteUser,
    updateOrganization,
    updateUser,
    addNewUser,
    addNewOrganization,
    updateUserActiveStatus,
)
from app.utils.turso import engine

class GetDataThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self):
        super().__init__()
        self.parentWidget = None
        self.functionName = None
        self.entry = None
        
    def setRequirements(self, parentWidget, functionName, entry):
        self.parentWidget = parentWidget
        self.functionName = functionName
        self.entry = entry

    def run(self):
        result = None
        
        match self.functionName:
            case 'getOneUserByUserId':
                result = getOneUserByUserId(self.parentWidget, self.entry)
            case 'getOneUserByUserNameAccessCode':
                result = getOneUserByUserNameAccessCode(self.parentWidget, self.entry)
            case 'getOneOrganizationByOrganizationId':
                result = getOneOrganizationByOrganizationId(self.parentWidget, self.entry)
            case 'getOneOrganizationByOrganizationName':
                result = getOneOrganizationByOrganizationName(self.parentWidget, self.entry)
            case 'getAllUserWithPaginationByKeyword':
                result = getAllUserWithPaginationByKeyword(self.parentWidget, self.entry)
            case 'getAllUser':
                result = getAllUser(self.parentWidget, self.entry)
            case 'getAllOrganization':
                result = getAllOrganization(self.parentWidget, self.entry)
            case _:
                print('invalid crud function...')
            
        print(f"crud function used: {self.functionName}...")
        
        engine.dispose()
        self.finished.emit(result)
