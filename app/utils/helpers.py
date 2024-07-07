import os, sys
from sqlalchemy import desc
from PyQt5.QtWidgets import QWidget, QMessageBox
from datetime import datetime

sys.path.append(os.path.abspath(''))
from app.models.model_association import session, User, Organization, Authentication

def getManageTypeByIndex(index:int):
    match index:
        case 0:
            return 'Sales'
        case 1:
            return 'Transaction'
        case 2:
            return 'Item'
        case 3:
            return 'Stock'
        case 4:
            return 'Promo'
        case 5:
            return 'Reward'
        case 6:
            return 'Member'
        case 7:
            return 'User'

def getOneUserWithUserId(parent:QWidget, entry:object):
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

def getOneUserWithUserNameAccessCode(parent:QWidget, entry:object):
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

def getOneOrganizationWithOrganizationId(parent:QWidget, entry:object):
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

def getOneOrganizationWithOrganizationName(parent:QWidget, entry:object):
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
        
# TODO: add a checker if the input already exist
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
            ((User.FullName == entry['fullName']) |
            (User.UserName == entry['userName']))
        ).first()
        
        if existingUser:
            if existingUser.FullName == entry['fullName']:
                QMessageBox.critical(parent, 'Error', f"{entry['fullName']} already exist.")
                
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
        existingUser = session.query(User).filter(
            (User.FullName == entry['fullName']) |
            (User.UserName == entry['userName'])
        ).first()
        
        if existingUser:
            if existingUser.FullName == entry['fullName']:
                QMessageBox.critical(parent, 'Error', f"{entry['fullName']} already exist.")
                
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
