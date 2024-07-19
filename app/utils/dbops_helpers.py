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
        
    def _getAllUserWithPaginationByKeyword(self):
        result = {
            'data': [],
            'totalPages': 0
        }
        
        try:       
            existingUser = session.query(User).filter(
                (User.OrganizationId.like(f"%{self.entry['keyword']}%")) |
                (User.UserName.like(f"%{self.entry['keyword']}%")) |
                (User.AccessCode.like(f"%{self.entry['keyword']}%")) |
                (User.FullName.like(f"%{self.entry['keyword']}%")) |
                (User.BirthDate.like(f"%{self.entry['keyword']}%")) |
                (User.MobileNumber.like(f"%{self.entry['keyword']}%")) |
                (User.AccessLevel.like(f"%{self.entry['keyword']}%")) |
                (User.ActiveStatus.like(f"%{self.entry['keyword']}%")) |
                (User.LastLoginTs.like(f"%{self.entry['keyword']}%")) |
                (User.LastLogoutTs.like(f"%{self.entry['keyword']}%")) |
                (User.UpdateTs.like(f"%{self.entry['keyword']}%"))
            ).order_by(desc(User.UpdateTs))
            
            limit = 30
            offset = (self.entry['currentPage'] - 1) * limit
            paginatedExistingUser = existingUser.limit(limit).offset(offset).all()
            
            if paginatedExistingUser:
                for user in paginatedExistingUser:
                    result['data'].append({
                        'userId': f"{user.Id}",
                        'organizationId': f"{user.OrganizationId}",
                        'organizationName': session.query(Organization.OrganizationName).filter(Organization.Id == f"{user.OrganizationId}").scalar(),
                        'userName': f"{user.UserName}",
                        'accessCode': f"{user.AccessCode}",
                        'fullName': f"{user.FullName}",
                        'birthDate': f"{user.BirthDate}",
                        'mobileNumber': f"{user.MobileNumber}",
                        'accessLevel': f"{user.AccessLevel}",
                        'activeStatus': f"{user.ActiveStatus}",
                        'lastLoginTs': f"{user.LastLoginTs}",
                        'lastLogoutTs': f"{user.LastLogoutTs}",
                        'updateTs': f"{user.UpdateTs}",
                    })
                
                result['totalPages'] = math.ceil(existingUser.count() / limit)
                
            return result
        
        except Exception as error:
            QMessageBox.critical(self.parentWidget, 'Error', f"An error occured: {error}")
            session.rollback()
            print('session rolled back...')
            return result
            
        finally:
            session.close()
            print('session closed...')
        
    def _getOneUserByUserNameAccessCode(self):
        result = {
            'userId': None,
            'organizationId': None,
            'organizationName': None,
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
                'userId': f"{existingUser.Id}",
                'organizationId': f"{existingUser.OrganizationId}",
                'organizationName': session.query(Organization.OrganizationName).filter(Organization.Id == f"{existingUser.OrganizationId}").scalar(),
                'userName': f"{existingUser.UserName}",
                'accessCode': f"{existingUser.AccessCode}",
                'fullName': f"{existingUser.FullName}",
                'birthDate': f"{existingUser.BirthDate}",
                'mobileNumber': f"{existingUser.MobileNumber}",
                'accessLevel': f"{existingUser.AccessLevel}",
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
        
    def _getOneOrganizationById(self):
        result = {
            'organizationId': None,
            'taxId': None,
            'organizationName': None,
            'address': None,
            'mobileNumber': None,
            'accessCode': None,
        }
        
        try:
            existingOrganization = session.query(Organization).filter(Organization.OrganizationName == self.entry['organizationId']).one_or_none()
            
            if not existingOrganization:
                print('Organization not found...')
                session.rollback()
                return result
                
            result = {
                'organizationId': existingOrganization.Id,
                'taxId': existingOrganization.TaxId,
                'organizationName': existingOrganization.OrganizationName,
                'address': existingOrganization.Address,
                'mobileNumber': existingOrganization.MobileNumber,
                'accessCode': existingOrganization.AccessCode,
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
            case '_getAllUserWithPaginationByKeyword':
                result = self._getAllUserWithPaginationByKeyword()
            case '_getOneUserByUserNameAccessCode':
                result = self._getOneUserByUserNameAccessCode()
            case '_getOneOrganizationById':
                result = self._getOneOrganizationById()
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