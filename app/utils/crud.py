import os, sys, math
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from datetime import datetime

sys.path.append(os.path.abspath(''))
from app.models.model_association import User, Organization, Authentication
from app.utils.turso import engine, sessionMaker

tursoUrl = f"{os.getenv('ONLINE_SQLALCHEMY_BASE_URL')}://{os.getenv('TURSO_DB_URL')}/?authToken={os.getenv('TURSO_DB_AUTH_TOKEN')}"
engine = create_engine(url=tursoUrl, echo=False)
sessionMaker = sessionmaker(bind=engine)
status = 'ONLINE'
    
# TODO: fix threading
class CRUDThread(QThread):
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
                result = self.getOneUserByUserId(sessionMaker, self.parentWidget, self.entry)
            case 'getOneUserByUserNameAccessCode':
                result = self.getOneUserByUserNameAccessCode(sessionMaker, self.parentWidget, self.entry)
            case 'getOneOrganizationByOrganizationId':
                result = self.getOneOrganizationByOrganizationId(sessionMaker, self.parentWidget, self.entry)
            case 'getOneOrganizationByOrganizationName':
                result = self.getOneOrganizationByOrganizationName(sessionMaker, self.parentWidget, self.entry)
            case 'getAllUserWithPaginationByKeyword':
                result = self.getAllUserWithPaginationByKeyword(sessionMaker, self.parentWidget, self.entry)
            case 'getAllUser':
                result = self.getAllUser(sessionMaker, self.parentWidget, self.entry)
            case 'getAllOrganization':
                result = self.getAllOrganization(sessionMaker, self.parentWidget, self.entry)
            case 'deleteUser':
                result = self.deleteUser(sessionMaker, self.parentWidget, self.entry)
            case 'updateOrganization':
                result = self.updateOrganization(sessionMaker, self.parentWidget, self.entry)
            case 'updateUser':
                result = self.updateUser(sessionMaker, self.parentWidget, self.entry)
            case 'updateUserActiveStatus':
                result = self.updateUserActiveStatus(sessionMaker, self.parentWidget, self.entry)
            case 'addNewUser':
                result = self.addNewUser(sessionMaker, self.parentWidget, self.entry)
            case 'addNewOrganization':
                result = self.addNewOrganization(sessionMaker, self.parentWidget, self.entry)
            case _:
                print('invalid crud function...')
            
        print(f"crud function used: {self.functionName}...")
        
        self.finished.emit(result)

    def getOneUserByUserId(self, sessionMaker, parentWidget, entry):
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
            'updateTs': None,
        }
        
        try:
            session = sessionMaker()
            existingUser = session.query(User).filter(User.Id == entry['userId']).one_or_none()
            
            if existingUser:
                result = {
                    'userId': existingUser.Id,
                    'organizationId': existingUser.OrganizationId,
                    'organizationName': session.query(Organization.OrganizationName).filter(Organization.Id == existingUser.OrganizationId).scalar(),
                    'userName': existingUser.UserName,
                    'accessCode': existingUser.AccessCode,
                    'fullName': existingUser.FullName,
                    'birthDate': existingUser.BirthDate,
                    'mobileNumber': existingUser.MobileNumber,
                    'accessLevel': existingUser.AccessLevel,
                    'updateTs': existingUser.UpdateTs,
                }
            
            return result
        
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at getOneUserByUserId:', error)
            return result
            
        finally:
            session.close()
            print('session closed...')

    def getOneUserByUserNameAccessCode(self, sessionMaker, parentWidget, entry):
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
            'updateTs': None,
        }
        
        try:
            session = sessionMaker()
            existingUser = session.query(User).filter(
                (User.UserName == entry['userName']) &
                (User.AccessCode == entry['accessCode'])
            ).one_or_none()
            
            if existingUser:
                result = {
                    'userId': existingUser.Id,
                    'organizationId': existingUser.OrganizationId,
                    'organizationName': session.query(Organization.OrganizationName).filter(Organization.Id == existingUser.OrganizationId).scalar(),
                    'userName': existingUser.UserName,
                    'accessCode': existingUser.AccessCode,
                    'fullName': existingUser.FullName,
                    'birthDate': existingUser.BirthDate,
                    'mobileNumber': existingUser.MobileNumber,
                    'accessLevel': existingUser.AccessLevel,
                    'updateTs': existingUser.UpdateTs,
                }
            
            return result
        
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at getOneUserByUserNameAccessCode:', error)
            return result
            
        finally:
            session.close()
            print('session closed...')

    def getOneOrganizationByOrganizationId(self, sessionMaker, parentWidget, entry):
        result = {
            'organizationId': None,
            'taxId': None,
            'organizationName': None,
            'address': None,
            'mobileNumber': None,
            'accessCode': None,
            'updateTs': None,
        }
        
        try:
            session = sessionMaker()
            existingOrganization = session.query(Organization).filter(Organization.Id == entry['organizationId']).one_or_none()
            
            if existingOrganization:
                result = {
                    'organizationId': existingOrganization.Id,
                    'taxId': existingOrganization.TaxId,
                    'organizationName': existingOrganization.OrganizationName,
                    'address': existingOrganization.Address,
                    'mobileNumber': existingOrganization.MobileNumber,
                    'accessCode': existingOrganization.AccessCode,
                    'updateTs': existingOrganization.UpdateTs,
                }
            
            return result
        
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at getOneOrganizationByOrganizationId:', error)
            return result
            
        finally:
            session.close()
            print('session closed...')

    def getOneOrganizationByOrganizationName(self, sessionMaker, parentWidget, entry):
        result = {
            'organizationId': None,
            'taxId': None,
            'organizationName': None,
            'address': None,
            'mobileNumber': None,
            'accessCode': None,
            'updateTs': None,
        }
        
        try:
            session = sessionMaker()
            existingOrganization = session.query(Organization).filter(Organization.OrganizationName == entry['organizationName']).one_or_none()
            
            if existingOrganization:
                result = {
                    'organizationId': existingOrganization.Id,
                    'taxId': existingOrganization.TaxId,
                    'organizationName': existingOrganization.OrganizationName,
                    'address': existingOrganization.Address,
                    'mobileNumber': existingOrganization.MobileNumber,
                    'accessCode': existingOrganization.AccessCode,
                    'updateTs': existingOrganization.UpdateTs,
                }
            
            return result
        
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at getOneOrganizationByOrganizationName:', error)
            return result
            
        finally:
            session.close()
            print('session closed...')

    def getAllUserWithPaginationByKeyword(self, sessionMaker, parentWidget, entry):
        result = {
            'data': [],
            'totalPages': 1
        }
        
        try:
            session = sessionMaker()
            existingUser = session.query(User).filter(
                (User.OrganizationId.like(f"%{entry['keyword']}%")) |
                (User.UserName.like(f"%{entry['keyword']}%")) |
                (User.AccessCode.like(f"%{entry['keyword']}%")) |
                (User.FullName.like(f"%{entry['keyword']}%")) |
                (User.BirthDate.like(f"%{entry['keyword']}%")) |
                (User.MobileNumber.like(f"%{entry['keyword']}%")) |
                (User.AccessLevel.like(f"%{entry['keyword']}%")) |
                (User.ActiveStatus.like(f"%{entry['keyword']}%")) |
                (User.LastLoginTs.like(f"%{entry['keyword']}%")) |
                (User.LastLogoutTs.like(f"%{entry['keyword']}%")) |
                (User.UpdateTs.like(f"%{entry['keyword']}%"))
            ).order_by(desc(User.UpdateTs))
            
            limit = 30
            offset = (entry['currentPage'] - 1) * limit
            paginatedExistingUser = existingUser.limit(limit).offset(offset).all()
            
            if paginatedExistingUser:
                for user in paginatedExistingUser:
                    result['data'].append({
                        'userId': user.Id,
                        'organizationName': session.query(Organization.OrganizationName).filter(Organization.Id == user.OrganizationId).scalar(),
                        'userName': user.UserName,
                        'accessCode': user.AccessCode,
                        'fullName': user.FullName,
                        'birthDate': user.BirthDate,
                        'mobileNumber': user.MobileNumber,
                        'accessLevel': user.AccessLevel,
                        'activeStatus': user.ActiveStatus,
                        'lastLoginTs': user.LastLoginTs,
                        'lastLogoutTs': user.LastLogoutTs,
                        'updateTs': user.UpdateTs,
                    })
                
                result['totalPages'] = math.ceil(existingUser.count() / limit)
                
            return result
        
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at getAllUserWithPaginationByKeyword:', error)
            return result
            
        finally:
            session.close()
            print('session closed...')

    def getAllUser(self, sessionMaker, parentWidget):
        result = []
        
        try:
            session = sessionMaker()
            existingUser = session.query(User).order_by(desc(User.UpdateTs)).all()
            
            if existingUser:
                for user in existingUser:
                    result.append({
                        'userId': user.Id,
                        'organizationId': user.OrganizationId,
                        'organizationName': user.OrganizationName,
                        'userName': user.UserName,
                        'accessCode': user.AccessCode,
                        'fullName': user.FullName,
                        'birthDate': user.BirthDate,
                        'mobileNumber': user.MobileNumber,
                        'accessLevel': user.AccessLevel,
                        'activeStatus': user.ActiveStatus,
                        'lastLoginTs': user.LastLoginTs,
                        'lastLogoutTs': user.LastLogoutTs,
                        'updateTs': user.UpdateTs,
                    })
            
            return result
        
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at getAllUser:', error)
            return result
            
        finally:
            session.close()
            print('session closed...')

    def getAllOrganization(self, sessionMaker, parentWidget):
        result = []
        
        try:
            session = sessionMaker()
            existingOrganization = session.query(Organization).order_by(desc(Organization.UpdateTs)).all()
            
            if existingOrganization:
                for organization in existingOrganization:
                    result.append({
                        'organizationId': organization.Id,
                        'taxId': organization.TaxId,
                        'organizationName': organization.OrganizationName,
                        'address': organization.Address,
                        'mobileNumber': organization.MobileNumber,
                        'accessCode': organization.AccessCode,
                        'updateTs': organization.UpdateTs,
                    })
            
            return result
        
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at getAllOrganization:', error)
            return result
            
        finally:
            session.close()
            print('session closed...')

    def deleteUser(self, sessionMaker, parentWidget, entry):
        try:
            session = sessionMaker()
            existingUser = session.query(User).filter(User.Id == entry['userId']).first()
            
            session.delete(existingUser)
            session.commit()
            return True
            
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at deleteUser:', error)
            return False
            
        finally:
            session.close()
            print('session closed...')

    def updateOrganization(self, sessionMaker, parentWidget, entry):
        try:
            session = sessionMaker()
            existingOrganization = session.query(Organization).filter(
                (Organization.Id != entry['organizationId']) &
                (Organization.OrganizationName == entry['organizationName'])
            ).first()
            
            if existingOrganization:
                if existingOrganization.OrganizationName == entry['organizationName']:
                    QMessageBox.critical(parentWidget, 'Error', f"{entry['organizationName']} already exist.")
                    
                session.rollback()
                return False
            
            organization = session.query(Organization).filter(Organization.Id == entry['organizationId']).one_or_none()
            organization.TaxId = entry['taxId']
            organization.OrganizationName = entry['organizationName']
            organization.Address = entry['address']
            organization.MobileNumber = entry['mobileNumber']
            organization.AccessCode = entry['accessCode']
            
            session.add(organization)
            session.commit()
            return True
            
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at updateOrganization:', error)
            return False
            
        finally:
            session.close()
            print('session closed...')

    def updateUser(self, sessionMaker, parentWidget, entry):
        try:
            session = sessionMaker()
            existingUser = session.query(User).filter(
                (User.Id != entry['userId']) &
                (User.UserName == entry['userName'])
            ).first()
            
            if existingUser:
                if existingUser.UserName == entry['userName']:
                    QMessageBox.critical(parentWidget, 'Error', f"{entry['userName']} already exist.")
                    
                session.rollback()
                return False
            
            user = session.query(User).filter(User.Id == entry['userId']).one_or_none()
            user.UserName = entry['userName']
            user.AccessCode = entry['accessCode']
            user.FullName = entry['fullName']
            user.BirthDate = entry['birthDate']
            user.MobileNumber = entry['mobileNumber']
            
            session.commit()
            return True
            
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at updateUser:', error)
            return False
            
        finally:
            session.close()
            print('session closed...')

    def updateUserActiveStatus(self, sessionMaker, parentWidget, entry):
        try:
            session = sessionMaker()
            user = session.query(User).filter(User.Id == entry['userId']).one_or_none()
            
            user.ActiveStatus = entry['activeStatus']
            currentTs = f"{datetime.now()}"
            
            if user.ActiveStatus == 0:
                user.LastLogoutTs = currentTs
                
            elif user.ActiveStatus == 1:
                user.LastLoginTs = currentTs
            
            session.commit()
            return True
            
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at updateUserActiveStatus:', error)
            return False
            
        finally:
            session.close()
            print('session closed...')

    def addNewUser(self, sessionMaker, parentWidget, entry):
        try:
            session = sessionMaker()
            existingUser = session.query(User).filter((User.UserName == entry['userName'])).first()
            
            if existingUser:        
                if existingUser.UserName == entry['userName']:
                    QMessageBox.critical(parentWidget, 'Error', f"{entry['userName']} already exist.")
                    
                session.rollback()
                return False

            user = User()
            user.OrganizationId = session.query(Organization.Id).filter(Organization.OrganizationName == entry['organizationName'])
            user.UserName = entry['userName']
            user.AccessCode = entry['accessCode']
            user.FullName = entry['fullName']
            user.BirthDate = entry['birthDate']
            user.MobileNumber = entry['mobileNumber']
            user.AccessLevel = entry['accessLevel']
            
            session.add(user)
            session.commit()
            return True
            
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at addNewUser:', error)
            return False
            
        finally:
            session.close()
            print('session closed...')

    def addNewOrganization(self, sessionMaker, parentWidget, entry):
        try:
            session = sessionMaker()
            existingOrganization = session.query(Organization).filter(Organization.OrganizationName == entry['organizationName']).first()
            
            if existingOrganization:
                if existingOrganization.OrganizationName == entry['organizationName']:
                    QMessageBox.critical(parentWidget, 'Error', f"{entry['organizationName']} already exist.")
                    
                session.rollback()
                return False
            
            organization = Organization()
            organization.TaxId = entry['taxId']
            organization.OrganizationName = entry['organizationName']
            organization.Address = entry['address']
            organization.MobileNumber = entry['mobileNumber']
            organization.AccessCode = entry['accessCode']
            
            session.add(organization)
            session.commit()
            return True
            
        except Exception as error:
            session.rollback()
            print('session rolled back...')
            print('error at addNewOrganization:', error)
            return False
            
        finally:
            session.close()
            print('session closed...')


def getOneUserByUserId(parentWidget, entry):
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
        'updateTs': None,
    }
    
    try:
        session = sessionMaker()
        existingUser = session.query(User).filter(User.Id == entry['userId']).one_or_none()
        
        if existingUser:
            result = {
                'userId': existingUser.Id,
                'organizationId': existingUser.OrganizationId,
                'organizationName': session.query(Organization.OrganizationName).filter(Organization.Id == existingUser.OrganizationId).scalar(),
                'userName': existingUser.UserName,
                'accessCode': existingUser.AccessCode,
                'fullName': existingUser.FullName,
                'birthDate': existingUser.BirthDate,
                'mobileNumber': existingUser.MobileNumber,
                'accessLevel': existingUser.AccessLevel,
                'updateTs': existingUser.UpdateTs,
            }
        
        return result
    
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at getOneUserByUserId:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def getOneUserByUserNameAccessCode(parentWidget, entry):
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
        'updateTs': None,
    }
    
    try:
        session = sessionMaker()
        existingUser = session.query(User).filter(
            (User.UserName == entry['userName']) &
            (User.AccessCode == entry['accessCode'])
        ).one_or_none()
        
        if existingUser:
            result = {
                'userId': existingUser.Id,
                'organizationId': existingUser.OrganizationId,
                'organizationName': session.query(Organization.OrganizationName).filter(Organization.Id == existingUser.OrganizationId).scalar(),
                'userName': existingUser.UserName,
                'accessCode': existingUser.AccessCode,
                'fullName': existingUser.FullName,
                'birthDate': existingUser.BirthDate,
                'mobileNumber': existingUser.MobileNumber,
                'accessLevel': existingUser.AccessLevel,
                'updateTs': existingUser.UpdateTs,
            }
        
        return result
    
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at getOneUserByUserNameAccessCode:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def getOneOrganizationByOrganizationId(parentWidget, entry):
    result = {
        'organizationId': None,
        'taxId': None,
        'organizationName': None,
        'address': None,
        'mobileNumber': None,
        'accessCode': None,
        'updateTs': None,
    }
    
    try:
        session = sessionMaker()
        existingOrganization = session.query(Organization).filter(Organization.Id == entry['organizationId']).one_or_none()
        
        if existingOrganization:
            result = {
                'organizationId': existingOrganization.Id,
                'taxId': existingOrganization.TaxId,
                'organizationName': existingOrganization.OrganizationName,
                'address': existingOrganization.Address,
                'mobileNumber': existingOrganization.MobileNumber,
                'accessCode': existingOrganization.AccessCode,
                'updateTs': existingOrganization.UpdateTs,
            }
        
        return result
    
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at getOneOrganizationByOrganizationId:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def getOneOrganizationByOrganizationName(parentWidget, entry):
    result = {
        'organizationId': None,
        'taxId': None,
        'organizationName': None,
        'address': None,
        'mobileNumber': None,
        'accessCode': None,
        'updateTs': None,
    }
    
    try:
        session = sessionMaker()
        existingOrganization = session.query(Organization).filter(Organization.OrganizationName == entry['organizationName']).one_or_none()
        
        if existingOrganization:
            result = {
                'organizationId': existingOrganization.Id,
                'taxId': existingOrganization.TaxId,
                'organizationName': existingOrganization.OrganizationName,
                'address': existingOrganization.Address,
                'mobileNumber': existingOrganization.MobileNumber,
                'accessCode': existingOrganization.AccessCode,
                'updateTs': existingOrganization.UpdateTs,
            }
        
        return result
    
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at getOneOrganizationByOrganizationName:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def getAllUserWithPaginationByKeyword(parentWidget, entry):
    result = {
        'data': [],
        'totalPages': 1
    }
    
    try:
        session = sessionMaker()
        existingUser = session.query(User).filter(
            (User.OrganizationId.like(f"%{entry['keyword']}%")) |
            (User.UserName.like(f"%{entry['keyword']}%")) |
            (User.AccessCode.like(f"%{entry['keyword']}%")) |
            (User.FullName.like(f"%{entry['keyword']}%")) |
            (User.BirthDate.like(f"%{entry['keyword']}%")) |
            (User.MobileNumber.like(f"%{entry['keyword']}%")) |
            (User.AccessLevel.like(f"%{entry['keyword']}%")) |
            (User.ActiveStatus.like(f"%{entry['keyword']}%")) |
            (User.LastLoginTs.like(f"%{entry['keyword']}%")) |
            (User.LastLogoutTs.like(f"%{entry['keyword']}%")) |
            (User.UpdateTs.like(f"%{entry['keyword']}%"))
        ).order_by(desc(User.UpdateTs))
        
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        paginatedExistingUser = existingUser.limit(limit).offset(offset).all()
        
        if paginatedExistingUser:
            for user in paginatedExistingUser:
                result['data'].append({
                    'userId': user.Id,
                    'organizationName': session.query(Organization.OrganizationName).filter(Organization.Id == user.OrganizationId).scalar(),
                    'userName': user.UserName,
                    'accessCode': user.AccessCode,
                    'fullName': user.FullName,
                    'birthDate': user.BirthDate,
                    'mobileNumber': user.MobileNumber,
                    'accessLevel': user.AccessLevel,
                    'activeStatus': user.ActiveStatus,
                    'lastLoginTs': user.LastLoginTs,
                    'lastLogoutTs': user.LastLogoutTs,
                    'updateTs': user.UpdateTs,
                })
            
            result['totalPages'] = math.ceil(existingUser.count() / limit)
            
        return result
    
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at getAllUserWithPaginationByKeyword:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def getAllUser(parentWidget):
    result = []
    
    try:
        session = sessionMaker()
        existingUser = session.query(User).order_by(desc(User.UpdateTs)).all()
        
        if existingUser:
            for user in existingUser:
                result.append({
                    'userId': user.Id,
                    'organizationId': user.OrganizationId,
                    'organizationName': user.OrganizationName,
                    'userName': user.UserName,
                    'accessCode': user.AccessCode,
                    'fullName': user.FullName,
                    'birthDate': user.BirthDate,
                    'mobileNumber': user.MobileNumber,
                    'accessLevel': user.AccessLevel,
                    'activeStatus': user.ActiveStatus,
                    'lastLoginTs': user.LastLoginTs,
                    'lastLogoutTs': user.LastLogoutTs,
                    'updateTs': user.UpdateTs,
                })
        
        return result
    
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at getAllUser:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def getAllOrganization(parentWidget):
    result = []
    
    try:
        session = sessionMaker()
        existingOrganization = session.query(Organization).order_by(desc(Organization.UpdateTs)).all()
        
        if existingOrganization:
            for organization in existingOrganization:
                result.append({
                    'organizationId': organization.Id,
                    'taxId': organization.TaxId,
                    'organizationName': organization.OrganizationName,
                    'address': organization.Address,
                    'mobileNumber': organization.MobileNumber,
                    'accessCode': organization.AccessCode,
                    'updateTs': organization.UpdateTs,
                })
        
        return result
    
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at getAllOrganization:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def deleteUser(parentWidget, entry):
    try:
        session = sessionMaker()
        existingUser = session.query(User).filter(User.Id == entry['userId']).first()
        
        session.delete(existingUser)
        session.commit()
        return True
        
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at deleteUser:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')

def updateOrganization(parentWidget, entry):
    try:
        session = sessionMaker()
        existingOrganization = session.query(Organization).filter(
            (Organization.Id != entry['organizationId']) &
            (Organization.OrganizationName == entry['organizationName'])
        ).first()
        
        if existingOrganization:
            if existingOrganization.OrganizationName == entry['organizationName']:
                QMessageBox.critical(parentWidget, 'Error', f"{entry['organizationName']} already exist.")
                
            session.rollback()
            return False
        
        organization = session.query(Organization).filter(Organization.Id == entry['organizationId']).one_or_none()
        organization.TaxId = entry['taxId']
        organization.OrganizationName = entry['organizationName']
        organization.Address = entry['address']
        organization.MobileNumber = entry['mobileNumber']
        organization.AccessCode = entry['accessCode']
        
        session.add(organization)
        session.commit()
        return True
        
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at updateOrganization:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')

def updateUser(parentWidget, entry):
    try:
        session = sessionMaker()
        existingUser = session.query(User).filter(
            (User.Id != entry['userId']) &
            (User.UserName == entry['userName'])
        ).first()
        
        if existingUser:
            if existingUser.UserName == entry['userName']:
                QMessageBox.critical(parentWidget, 'Error', f"{entry['userName']} already exist.")
                
            session.rollback()
            return False
        
        user = session.query(User).filter(User.Id == entry['userId']).one_or_none()
        user.UserName = entry['userName']
        user.AccessCode = entry['accessCode']
        user.FullName = entry['fullName']
        user.BirthDate = entry['birthDate']
        user.MobileNumber = entry['mobileNumber']
        
        session.commit()
        return True
        
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at updateUser:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')

def updateUserActiveStatus(parentWidget, entry):
    try:
        session = sessionMaker()
        user = session.query(User).filter(User.Id == entry['userId']).one_or_none()
        
        user.ActiveStatus = entry['activeStatus']
        currentTs = f"{datetime.now()}"
        
        if user.ActiveStatus == 0:
            user.LastLogoutTs = currentTs
            
        elif user.ActiveStatus == 1:
            user.LastLoginTs = currentTs
        
        session.commit()
        return True
        
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at updateUserActiveStatus:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')

def addNewUser(parentWidget, entry):
    try:
        session = sessionMaker()
        existingUser = session.query(User).filter((User.UserName == entry['userName'])).first()
        
        if existingUser:        
            if existingUser.UserName == entry['userName']:
                QMessageBox.critical(parentWidget, 'Error', f"{entry['userName']} already exist.")
                
            session.rollback()
            return False

        user = User()
        user.OrganizationId = session.query(Organization.Id).filter(Organization.OrganizationName == entry['organizationName'])
        user.UserName = entry['userName']
        user.AccessCode = entry['accessCode']
        user.FullName = entry['fullName']
        user.BirthDate = entry['birthDate']
        user.MobileNumber = entry['mobileNumber']
        user.AccessLevel = entry['accessLevel']
        
        session.add(user)
        session.commit()
        return True
        
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at addNewUser:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')

def addNewOrganization(parentWidget, entry):
    try:
        session = sessionMaker()
        existingOrganization = session.query(Organization).filter(Organization.OrganizationName == entry['organizationName']).first()
        
        if existingOrganization:
            if existingOrganization.OrganizationName == entry['organizationName']:
                QMessageBox.critical(parentWidget, 'Error', f"{entry['organizationName']} already exist.")
                
            session.rollback()
            return False
        
        organization = Organization()
        organization.TaxId = entry['taxId']
        organization.OrganizationName = entry['organizationName']
        organization.Address = entry['address']
        organization.MobileNumber = entry['mobileNumber']
        organization.AccessCode = entry['accessCode']
        
        session.add(organization)
        session.commit()
        return True
        
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at addNewOrganization:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')
