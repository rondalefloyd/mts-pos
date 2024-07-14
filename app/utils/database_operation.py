import os, sys, math
from sqlalchemy import desc
from PyQt5.QtWidgets import QWidget, QMessageBox
from datetime import datetime

sys.path.append(os.path.abspath(''))
from app.models.model_association import session, User, Organization, Authentication
from app.controllers.widget.Loading import LoadingController

def getOneUserByUserId(parent:QWidget, entry:object):
    result = {
        'userId': None,
        'organizationId': None,
        'userName': None,
        'accessCode': None,
        'fullName': None,
        'birthDate': None,
        'mobileNumber': None,
        'accessLevel': None,
    }
    
    try:
        existingUser = session.query(User).filter(User.Id == entry['userId']).one()
        
        if existingUser:
            result = {
                'userId': existingUser.Id,
                'organizationId': existingUser.OrganizationId,
                'userName': existingUser.UserName,
                'accessCode': existingUser.AccessCode,
                'fullName': existingUser.FullName,
                'birthDate': existingUser.BirthDate,
                'mobileNumber': existingUser.MobileNumber,
                'accessLevel': existingUser.AccessLevel,
            }
        
        return result
    
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return result
        
    finally:
        print('Session closing...')
        session.close()

def getOneUserByUserNameAccessCode(parent:QWidget, entry:object):
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
            (User.UserName == entry['userName']) &
            (User.AccessCode == entry['accessCode'])
        ).one()
        
        if existingUser:
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
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return result
        
    finally:
        print('Session closing...')
        session.close()

def getOneOrganizationByOrganizationId(parent:QWidget, entry:object):
    result = {
        'organizationId': None,
        'taxId': None,
        'organizationName': None,
        'address': None,
        'mobileNumber': None,
        'accessCode': None,
    }
    
    try:
        existingOrganization = session.query(Organization).filter(Organization.Id == entry['organizationId']).one()
        
        if existingOrganization:
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
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return result
        
    finally:
        print('Session closing...')
        session.close()

def getOneOrganizationByOrganizationName(parent:QWidget, entry:object):
    result = {
        'organizationId': None,
        'taxId': None,
        'organizationName': None,
        'address': None,
        'mobileNumber': None,
        'accessCode': None,
    }
    
    try:
        existingOrganization = session.query(Organization).filter(Organization.OrganizationName == entry['organizationName']).one()
        
        if existingOrganization:
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
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return result
        
    finally:
        print('Session closing...')
        session.close()

def getAllUserWithPaginationByKeyword(parent:QWidget, entry:object):
    result = {
        'data': [],
        'totalPages': 0
    }
    
    try:       
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
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return result
        
    finally:
        print('Session closing...')
        session.close()

def getAllUser(parent:QWidget):
    result = []
    
    try:
        existingUser = session.query(User).order_by(desc(User.UpdateTs)).all()
        
        if existingUser:
            for user in existingUser:
                result.append({
                    'userId': user.Id,
                    'organizationId': user.OrganizationId,
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
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return result
        
    finally:
        print('Session closing...')
        session.close()

def getAllOrganization(parent:QWidget):
    result = []
    
    try:
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
                })
        
        return result
    
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return result
        
    finally:
        print('Session closing...')
        session.close()

def deleteUser(parent:QWidget, entry:object):
    try:
        existingUser = session.query(User).filter(User.Id == entry['userId']).first()
        
        session.delete(existingUser)
        session.commit()
        return True
        
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return False
        
    finally:
        print('Session closing...')
        session.close()

def updateOrganization(parent:QWidget, entry:object):
    try:
        existingOrganization = session.query(Organization).filter(
            (Organization.Id != entry['organizationId']) &
            (Organization.OrganizationName == entry['organizationName'])
        ).first()
        
        if existingOrganization:
            if existingOrganization.OrganizationName == entry['organizationName']:
                QMessageBox.critical(parent, 'Error', f"{entry['organizationName']} already exist.")
                
            session.rollback()
            return False
        
        organization = session.query(Organization).filter(Organization.Id == entry['organizationId']).one()
        organization.TaxId = entry['taxId']
        organization.OrganizationName = entry['organizationName']
        organization.Address = entry['address']
        organization.MobileNumber = entry['mobileNumber']
        organization.AccessCode = entry['accessCode']
        
        session.add(organization)
        session.commit()
        return True
        
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return False
        
    finally:
        print('Session closing...')
        session.close()

def updateUserActiveStatus(parent:QWidget, entry:object):
    try:
        user = session.query(User).filter(User.Id == entry['userId']).one()
        
        user.ActiveStatus = entry['activeStatus']
        currentTs = f"{datetime.now()}"
        
        if user.ActiveStatus == 0:
            user.LastLogoutTs = currentTs
            
        elif user.ActiveStatus == 1:
            user.LastLoginTs = currentTs
        
        session.commit()
        return True
        
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return False
        
    finally:
        print('Session closing...')
        session.close()

def updateUser(parent:QWidget, entry:object):
    try:
        existingUser = session.query(User).filter(
            (User.Id != entry['userId']) &
            (User.UserName == entry['userName'])
        ).first()
        
        if existingUser:
            if existingUser.UserName == entry['userName']:
                QMessageBox.critical(parent, 'Error', f"{entry['userName']} already exist.")
                
            session.rollback()
            return False
        
        user = session.query(User).filter(User.Id == entry['userId']).one()
        user.UserName = entry['userName']
        user.AccessCode = entry['accessCode']
        user.FullName = entry['fullName']
        user.BirthDate = entry['birthDate']
        user.MobileNumber = entry['mobileNumber']
        
        session.commit()
        return True
        
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return False
        
    finally:
        print('Session closing...')
        session.close()

def addNewUser(parent:QWidget, entry:object):
    try:
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
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return False
        
    finally:
        print('Session closing...')
        session.close()

def addNewOrganization(parent:QWidget, entry:object):
    try:
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
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return False
        
    finally:
        print('Session closing...')
        session.close()
