import os, sys
from sqlalchemy import desc
from PyQt5.QtWidgets import QDialog, QMessageBox

sys.path.append(os.path.abspath(''))
from app.models.model_association import session, User, Organization, Authentication

def getManageTypeByIndex(index):
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

def getOneUserWithUserNameAccessCode(parent, input):
    output = {
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
            (User.UserName == input['userName']) &
            (User.AccessCode == input['accessCode'])
        ).one()
        
        if existingUser:
            output = {
                'userId': existingUser.Id,
                'userName': existingUser.UserName,
                'accessCode': existingUser.AccessCode,
                'fullName': existingUser.FullName,
                'birthDate': existingUser.BirthDate,
                'mobileNumber': existingUser.MobileNumber,
                'accessLevel': existingUser.AccessLevel,
            }
        
        return output
    
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return output
        
    finally:
        print('Session closing...')
        session.close()

def getOneOrganizationWithOrganizationName(parent, input):
    output = {
        'organizationId': None,
        'taxId': None,
        'organizationName': None,
        'address': None,
        'mobileNumber': None,
        'accessCode': None,
    }
    
    try:
        existingOrganization = session.query(Organization).filter(Organization.OrganizationName == input['organizationName']).one()
        
        if existingOrganization:
            output = {
                'organizationId': existingOrganization.Id,
                'taxId': existingOrganization.TaxId,
                'organizationName': existingOrganization.OrganizationName,
                'address': existingOrganization.Address,
                'mobileNumber': existingOrganization.MobileNumber,
                'accessCode': existingOrganization.AccessCode,
            }
        
        return output
    
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return output
        
    finally:
        print('Session closing...')
        session.close()

def getAllOrganization(parent):
    output = []
    
    try:
        existingOrganization = session.query(Organization).order_by(desc(Organization.UpdateTs)).all()
        
        if existingOrganization:
            for organization in existingOrganization:
                output.append({
                    'organizationId': organization.Id,
                    'taxId': organization.TaxId,
                    'organizationName': organization.OrganizationName,
                    'address': organization.Address,
                    'mobileNumber': organization.MobileNumber,
                    'accessCode': organization.AccessCode,
                })
        
        return output
    
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        return output
        
    finally:
        print('Session closing...')
        session.close()

def updateUser(parent, input):
    try:
        user = session.query(User).filter(User.Id == input['userId'])
        user.UserName = input['userName']
        user.AccessCode = input['accessCode']
        user.FullName = input['fullName']
        user.BirthDate = input['birthDate']
        user.MobileNumber = input['mobileNumber']
        user.AccessLevel = input['accessLevel']
        user.ActiveStatus = input['activeStatus']
        user.LastLoginTs = input['lastLoginTs']
        user.LastLogoutTs = input['lastLogoutTs']
        
        session.commit()
        
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        
    finally:
        print('Session closing...')
        session.close()

def addNewUser(parent, input):
    try:
        existingUser = session.query(User).filter(
            (User.FullName == input['fullName']) |
            (User.UserName == input['userName'])
        ).first()
        
        if existingUser:
            if existingUser.FullName == input['fullName']:
                QMessageBox.critical(parent, 'Error', f"{input['fullName']} already exist.")
                
            if existingUser.UserName == input['userName']:
                QMessageBox.critical(parent, 'Error', f"{input['userName']} already exist.")
                
            return
        
        user = User()
        user.OrganizationId = session.query(Organization.Id).filter(Organization.OrganizationName == input['organizationName'])
        user.UserName = input['userName']
        user.AccessCode = input['accessCode']
        user.FullName = input['fullName']
        user.BirthDate = input['birthDate']
        user.MobileNumber = input['mobileNumber']
        user.AccessLevel = input['accessLevel']
        
        session.add(user)
        session.commit()
        
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        
    finally:
        print('Session closing...')
        session.close()

def addNewOrganization(parent, input):
    try:
        existingOrganization = session.query(Organization).filter(Organization.OrganizationName == input['organizationName']).first()
        
        if existingOrganization:
            if existingOrganization.OrganizationName == input['organizationName']:
                QMessageBox.critical(parent, 'Error', f"{input['organizationName']} already exist.")
                
            return
        
        organization = Organization()
        organization.TaxId = input['taxId']
        organization.OrganizationName = input['organizationName']
        organization.Address = input['address']
        organization.MobileNumber = input['mobileNumber']
        organization.AccessCode = input['accessCode']
        
        session.add(organization)
        session.commit()
        
    except Exception as error:
        print('Error:', error)
        print('Session rolling back...')
        session.rollback()
        
    finally:
        print('Session closing...')
        session.close()
