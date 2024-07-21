import os, sys, math, threading
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

sys.path.append(os.path.abspath(''))
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
    updateUserActiveStatus,
    addNewUser,
    addNewOrganization,
)
from app.utils.turso import engine, scopedSession

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
                result = getOneUserByUserId(scopedSession, self.parentWidget, self.entry)
            case 'getOneUserByUserNameAccessCode':
                result = getOneUserByUserNameAccessCode(scopedSession, self.parentWidget, self.entry)
            case 'getOneOrganizationByOrganizationId':
                result = getOneOrganizationByOrganizationId(scopedSession, self.parentWidget, self.entry)
            case 'getOneOrganizationByOrganizationName':
                result = getOneOrganizationByOrganizationName(scopedSession, self.parentWidget, self.entry)
            case 'getAllUserWithPaginationByKeyword':
                result = getAllUserWithPaginationByKeyword(scopedSession, self.parentWidget, self.entry)
            case 'getAllUser':
                result = getAllUser(scopedSession, self.parentWidget, self.entry)
            case 'getAllOrganization':
                result = getAllOrganization(scopedSession, self.parentWidget, self.entry)
            case _:
                print('invalid crud function...')
            
        print(f"crud function used: {self.functionName}...")
        
        self.finished.emit(result)

class DeleteDataThread(QThread):
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
            case 'deleteUser':
                result = deleteUser(scopedSession, self.parentWidget, self.entry)
            case _:
                print('invalid crud function...')
            
        print(f"crud function used: {self.functionName}...")
        
        self.finished.emit(result)

class UpdateDataThread(QThread):
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
            case 'updateOrganization':
                result = updateOrganization(scopedSession, self.parentWidget, self.entry)
            case 'updateUser':
                result = updateUser(scopedSession, self.parentWidget, self.entry)
            case 'updateUserActiveStatus':
                result = updateUserActiveStatus(scopedSession, self.parentWidget, self.entry)
            case _:
                print('invalid crud function...')
            
        print(f"crud function used: {self.functionName}...")
        
        self.finished.emit(result)

class AddDataThread(QThread):
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
            case 'addNewUser':
                result = addNewUser(scopedSession, self.parentWidget, self.entry)
            case 'addNewOrganization':
                result = addNewOrganization(scopedSession, self.parentWidget, self.entry)
            case _:
                print('invalid crud function...')
            
        print(f"crud function used: {self.functionName}...")
        
        self.finished.emit(result)
