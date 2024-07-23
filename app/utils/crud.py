import os, sys, math
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from datetime import datetime

sys.path.append(os.path.abspath(''))
from app.models.model_association import User, Organization, Authentication
from app.utils.turso import engine, session

tursoUrl = f"{os.getenv('ONLINE_SQLALCHEMY_BASE_URL')}://{os.getenv('TURSO_DB_URL')}/?authToken={os.getenv('TURSO_DB_AUTH_TOKEN')}"
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
        engine = create_engine(url=tursoUrl, echo=False)
        sessionMaker = sessionmaker(bind=engine)
        scopedSession = scoped_session(sessionMaker)
        _session = scopedSession()

        try:
            match self.functionName:
                case '_getOneUserByUserId':
                    result = self._getOneUserByUserId(_session, self.parentWidget, self.entry)
                case '_getOneUserByUserNameAccessCode':
                    result = self._getOneUserByUserNameAccessCode(_session, self.parentWidget, self.entry)
                case '_getOneOrganizationByOrganizationId':
                    result = self._getOneOrganizationByOrganizationId(_session, self.parentWidget, self.entry)
                case '_getOneOrganizationByOrganizationName':
                    result = self._getOneOrganizationByOrganizationName(_session, self.parentWidget, self.entry)
                case '_getAllUserWithPaginationByKeyword':
                    result = self._getAllUserWithPaginationByKeyword(_session, self.parentWidget, self.entry)
                case '_getAllUser':
                    result = self._getAllUser(_session, self.parentWidget, self.entry)
                case '_getAllOrganization':
                    result = self._getAllOrganization(_session, self.parentWidget, self.entry)
                case '_deleteUser':
                    result = self._deleteUser(_session, self.parentWidget, self.entry)
                case '_updateOrganization':
                    result = self._updateOrganization(_session, self.parentWidget, self.entry)
                case '_updateUser':
                    result = self._updateUser(_session, self.parentWidget, self.entry)
                case '_updateUserActiveStatus':
                    result = self._updateUserActiveStatus(_session, self.parentWidget, self.entry)
                case '_addNewUser':
                    result = self._addNewUser(_session, self.parentWidget, self.entry)
                case '_addNewOrganization':
                    result = self._addNewOrganization(_session, self.parentWidget, self.entry)
                case _:
                    print('invalid crud function...')
                
            print(f"crud function used: {self.functionName}...")
        
        except Exception as error:
            print('error:', error)
            
        finally:
            session.close()
            scopedSession.remove()
            
        engine.dispose()
        self.finished.emit(result)
            
    def _getOneUserByUserId(self, session, parentWidget, entry):
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
        
    def _getOneUserByUserNameAccessCode(self, session, parentWidget, entry):
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
        
    def _getOneOrganizationByOrganizationId(self, session, parentWidget, entry):
        result = {
            'organizationId': None,
            'taxId': None,
            'organizationName': None,
            'address': None,
            'mobileNumber': None,
            'accessCode': None,
            'updateTs': None,
        }
        
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
    
    def _getOneOrganizationByOrganizationName(self, session, parentWidget, entry):
        result = {
            'organizationId': None,
            'taxId': None,
            'organizationName': None,
            'address': None,
            'mobileNumber': None,
            'accessCode': None,
            'updateTs': None,
        }
    
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
        
    def _getAllUserWithPaginationByKeyword(self, session, parentWidget, entry):
        result = {
            'data': [],
            'totalPages': 1
        }
    
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
        
    def _getAllUser(self, session, parentWidget):
        result = []
        
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
    
    def _getAllOrganization(self, session, parentWidget):
        result = []
        
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
        
    def _deleteUser(self, session, parentWidget, entry):
        existingUser = session.query(User).filter(User.Id == entry['userId']).first()
        
        session.delete(existingUser)
        session.commit()
        return True
        
    def _updateOrganization(self, session, parentWidget, entry):
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
            
    def _updateUser(self, session, parentWidget, entry):
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
            
    def _updateUserActiveStatus(self, session, parentWidget, entry):
        user = session.query(User).filter(User.Id == entry['userId']).one_or_none()
        
        user.ActiveStatus = entry['activeStatus']
        currentTs = f"{datetime.now()}"
        
        if user.ActiveStatus == 0:
            user.LastLogoutTs = currentTs
            
        elif user.ActiveStatus == 1:
            user.LastLoginTs = currentTs
        
        session.commit()
        return True
            
    def _addNewUser(self, session, parentWidget, entry):
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
            
    def _addNewOrganization(self, session, parentWidget, entry):
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
    