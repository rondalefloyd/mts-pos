import os, sys, math
from sqlalchemy import desc
from PyQt5.QtWidgets import QWidget, QMessageBox
from datetime import datetime

sys.path.append(os.path.abspath(''))
from app.models.model_association import User, Organization, Authentication
from app.controllers.Loading import LoadingController
from app.utils.turso import sessionMaker

def _getOneUserByUserId(parent:QWidget, entry:object):
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
        print('error at _getOneUserByUserId:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def _getOneUserByUserNameAccessCode(parent:QWidget, entry:object):
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
        print('error at _getOneUserByUserNameAccessCode:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def _getOneOrganizationByOrganizationId(parent:QWidget, entry:object):
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
        print('error at _getOneOrganizationByOrganizationId:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def _getOneOrganizationByOrganizationName(parent:QWidget, entry:object):
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
        print('error at _getOneOrganizationByOrganizationName:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def _getAllUserWithPaginationByKeyword(parent:QWidget, entry:object):
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
        print('error at _getAllUserWithPaginationByKeyword:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def _getAllUser(parent:QWidget):
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
        print('error at _getAllUser:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def _getAllOrganization(parent:QWidget):
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
        print('error at _getAllOrganization:', error)
        return result
        
    finally:
        session.close()
        print('session closed...')

def _deleteUser(parent:QWidget, entry:object):
    try:
        session = sessionMaker()
        existingUser = session.query(User).filter(User.Id == entry['userId']).first()
        
        session.delete(existingUser)
        session.commit()
        return True
        
    except Exception as error:
        session.rollback()
        print('session rolled back...')
        print('error at _deleteUser:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')

def _updateOrganization(parent:QWidget, entry:object):
    try:
        session = sessionMaker()
        existingOrganization = session.query(Organization).filter(
            (Organization.Id != entry['organizationId']) &
            (Organization.OrganizationName == entry['organizationName'])
        ).first()
        
        if existingOrganization:
            if existingOrganization.OrganizationName == entry['organizationName']:
                QMessageBox.critical(parent, 'Error', f"{entry['organizationName']} already exist.")
                
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
        print('error at _updateOrganization:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')

def _updateUser(parent:QWidget, entry:object):
    try:
        session = sessionMaker()
        existingUser = session.query(User).filter(
            (User.Id != entry['userId']) &
            (User.UserName == entry['userName'])
        ).first()
        
        if existingUser:
            if existingUser.UserName == entry['userName']:
                QMessageBox.critical(parent, 'Error', f"{entry['userName']} already exist.")
                
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
        print('error at _updateUser:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')

def _addNewUser(parent:QWidget, entry:object):
    try:
        session = sessionMaker()
        existingUser = session.query(User).filter((User.UserName == entry['userName'])).first()
        
        if existingUser:        
            if existingUser.UserName == entry['userName']:
                QMessageBox.critical(parent, 'Error', f"{entry['userName']} already exist.")
                
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
        print('error at _addNewUser:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')

def _addNewOrganization(parent:QWidget, entry:object):
    try:
        session = sessionMaker()
        existingOrganization = session.query(Organization).filter(Organization.OrganizationName == entry['organizationName']).first()
        
        if existingOrganization:
            if existingOrganization.OrganizationName == entry['organizationName']:
                QMessageBox.critical(parent, 'Error', f"{entry['organizationName']} already exist.")
                
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
        print('error at _addNewOrganization:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')

def _updateUserActiveStatus(parent:QWidget, entry:object):
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
        print('error at _updateUserActiveStatus:', error)
        return False
        
    finally:
        session.close()
        print('session closed...')

