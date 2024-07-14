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
from app.controllers.widget.Loading import LoadingController

class DatabaseOperationThread(QThread):
    finished = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.widget = None
        self.functionName = None
        self.entry = None
        
    def setup(self, widget, functionName, entry):
        self.widget = widget
        self.functionName = functionName
        self.entry = entry

    def run(self):
        if self.functionName == 'getAllUserWithPaginationByKeyword':
            result = getAllUserWithPaginationByKeyword(self.widget, self.entry)

        self.finished.emit(result)
