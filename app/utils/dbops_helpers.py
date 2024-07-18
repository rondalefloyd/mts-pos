import os, sys, math
from sqlalchemy import desc
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

sys.path.append(os.path.abspath(''))
from app.models.model_association import session, status, User, Organization, Authentication

class GetDataThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self):
        super().__init__()
        print('GetDataThread initialized...')
        self.parentWidget = None
        self.functionName = None
        self.entry = None
        
    def setRequirements(self, parentWidget, functionName, entry):
        self.parentWidget = parentWidget
        self.functionName = functionName
        self.entry = entry
        
    def _getOneUserByUserNameAccessCode(self):
        result = {
            'userId': None,
            'userName': None,
            'accessCode': None,
            'fullName': None,
            'birthDate': None,
            'mobileNumber': None,
            'accessLevel': None,
        }
        
        try:
            existingUser = session.query(User).filter(
                (User.UserName == self.entry['userName']) &
                (User.AccessCode == self.entry['accessCode'])
            ).one_or_none()
            
            if not existingUser:
                print('User not found...')
                session.rollback()
                return result
                
            result = {
                'userId': existingUser.Id,
                'userName': existingUser.UserName,
                'accessCode': existingUser.AccessCode,
                'fullName': existingUser.FullName,
                'birthDate': existingUser.BirthDate,
                'mobileNumber': existingUser.MobileNumber,
                'accessLevel': existingUser.AccessLevel,
            }

            return result
        
        except Exception as error:
            QMessageBox.critical(self.parentWidget, 'Error', f"An error occured: {error}")
            session.rollback()
            print('session rolled back...')
            return result
            
        finally:
            session.close()
            print('session closed...')
        
    def run(self):
        result = None
        
        match self.functionName:
            case '_getOneUserByUserNameAccessCode':
                result = self._getOneUserByUserNameAccessCode()
            case _:
                print('function not found in GetUserThread...')
                
        self.finished.emit(result)
        
class UpdateDataThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, parentWidget, functionName, entry):
        super().__init__()
        self.parentWidget = parentWidget
        self.functionName = functionName
        self.entry = entry
        
    def _updateUserById(self):
        result = False
        
        try:
            pass
        except:
            session.rollback()
            print('session rolled back...')
        finally:
            self.finished.emit(result)
            session.close()
            print('session closed...')
        
    def run(self):
        result = None
        
        match self.functionName:
            case '_updateUserById':
                result = self._updateUserById()
            case _:
                print('function not found in UpdateDataThread...')
                
        self.finished.emit(result)
        
        
class AddDataThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, parentWidget, functionName, entry):
        super().__init__()
        self.parentWidget = parentWidget
        self.functionName = functionName
        self.entry = entry
        
    def _updateUserById(self):
        result = False
        
        try:
            pass
        except:
            session.rollback()
            print('session rolled back...')
        finally:
            self.finished.emit(result)
            session.close()
            print('session closed...')
        
    def run(self):
        result = None
        
        match self.functionName:
            case '_updateUserById':
                result = self._updateUserById()
            case _:
                print('function not found in AddDataThread...')
                
        self.finished.emit(result)
        
        
class DeleteDataThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, parentWidget, functionName, entry):
        super().__init__()
        self.parentWidget = parentWidget
        self.functionName = functionName
        self.entry = entry
        
    def _deleteUserById(self):
        result = False
        
        try:
            pass
        except:
            session.rollback()
            print('session rolled back...')
        finally:
            self.finished.emit(result)
            session.close()
            print('session closed...')
        
    def run(self):
        result = None
        
        match self.functionName:
            case '_deleteUserById':
                result = self._deleteUserById()
            case _:
                print('function not found in DeleteDataThread...')
                
        self.finished.emit(result)