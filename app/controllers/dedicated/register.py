import os, sys, logging, re
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import (
    Users, 
    UserSessionInfos, 
    Organizations,
    Members,
    Promos,
    Rewards,
)
from app.controllers.common.validator import is_entry_valid
from app.controllers.common.messages import (
    exception_error_message,
    integrity_error_message,
    function_route_not_exist,
)
from app.utils.database import postgres_db

logging.basicConfig(level=logging.INFO)

class RegisterThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function_route, entry=None):
        super().__init__()
        self.function_route = function_route
        self.entry = entry
    
    def run(self):
        result = {
            'success': False,
            'message': 'N/A',
        }
        try:
            with postgres_db:
                match self.function_route:
                    case 'pos/register/organization':
                        result = register_organization(self.entry)
                    case 'pos/register/user':
                        result = register_user(self.entry)
                    case 'pos/register/member':
                        result = register_member(self.entry)
                    case 'pos/register/promo':
                        result = register_promo(self.entry)
                    case 'pos/register/reward':
                        result = register_reward(self.entry)
                    case _:
                        result['message'] = function_route_not_exist(self.function_route, self.__class__.__name__)


            self.finished.emit(result)

        except Exception as error:
            result['message'] = exception_error_message(error)
            postgres_db.rollback()
            self.finished.emit(result)
            logging.error('error: ', error)
            logging.info('database rolled back...')
            
        finally:
            postgres_db.close()
            logging.info('database closed...')

def register_organization(entry):
    result = {
        'success': False,
        'message': 'Organization registration failed.',
    }
    
    if is_entry_valid(['taxId', 'organizationName', 'address', 'mobileNumber', 'accessCode'], entry) is False:
        result['message'] = 'Fields cannot be empty or blank.'
        return result
    
    try:
        # Create new organization
        organizations = Organizations.create(
            TaxId=entry['taxId'],
            OrganizationName=entry['organizationName'],
            Address=entry['address'],
            MobileNumber=entry['mobileNumber'],
            AccessCode=entry['accessCode']
        )
        
        result['success'] = True
        result['message'] = 'Organization registered successfully.'
        
    except IntegrityError as error:
        result['message'] = integrity_error_message(error)
        logging.error(error)
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def register_user(entry):
    result = {
        'success': False,
        'message': 'Registration failed.',
    }
    
    if is_entry_valid(['organizationName', 'userName', 'accessCode', 'fullName', 'birthDate', 'mobileNumber', 'accessLevel'], entry) is False:
        result['message'] = 'Fields cannot be empty or blank.'
        return result
    
    try:
        # Create new user
        users = Users.create(
            OrganizationId=Organizations.select(Organizations.Id).where(Organizations.OrganizationName == entry['organizationName']).first(),
            UserName=entry['userName'],
            AccessCode=entry['accessCode'],
            FullName=entry['fullName'],
            BirthDate=entry['birthDate'],
            MobileNumber=entry['mobileNumber'],
            AccessLevel=entry['accessLevel']
        )
        
        # Create user session info
        UserSessionInfos.create(
            UserId=users.Id,
            ActiveStatus=0,
        )
        
        result['success'] = True
        result['message'] = 'User registered successfully.'
        
    except IntegrityError as error:
        result['message'] = integrity_error_message(error)
        logging.error(error)
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def register_member(entry):
    result = {
        'success': False,
        'message': 'Registration failed.',
    }
    
    if is_entry_valid(['organizationName', 'memberName', 'birthDate', 'address', 'mobileNumber'], entry) is False:
        result['message'] = 'Fields cannot be empty or blank.'
        return result
    
    try:
        # Create new member
        members = Members.create(
            OrganizationId=Organizations.select(Organizations.Id).where(Organizations.OrganizationName == entry['organizationName']).first(),
            MemberName=entry['memberName'],
            BirthDate=entry['birthDate'],
            Address=entry['address'],
            MobileNumber=entry['mobileNumber'],
            Points=entry['points'],
        )
        
        result['success'] = True
        result['message'] = 'Member registered successfully.'
        
    except IntegrityError as error:
        result['message'] = integrity_error_message(error)
        logging.error(error)
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def register_promo(entry):
    result = {
        'success': False,
        'message': 'Registration failed.',
    }
    
    if is_entry_valid(['promoName', 'discountRate', 'description'], entry) is False:
        result['message'] = 'Fields cannot be empty or blank.'
        return result
    
    try:
        # Create new promo
        promo = Promos.create(
            PromoName=entry['promoName'],
            DiscountRate=entry['discountRate'],
            Description=entry['description'],
        )
        
        result['success'] = True
        result['message'] = 'Promo registered successfully.'
        
    except IntegrityError as error:
        result['message'] = integrity_error_message(error)
        logging.error(error)
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def register_reward(entry):
    result = {
        'success': False,
        'message': 'Registration failed.',
    }
    
    if is_entry_valid(['rewardName', 'points', 'target', 'description'], entry) is False:
        result['message'] = 'Fields cannot be empty or blank.'
        return result
    
    try:
        # Create new reward
        reward = Rewards.create(
            RewardName=entry['rewardName'],
            Points=entry['points'],
            Target=entry['target'],
            Description=entry['description'],
        )
        
        result['success'] = True
        result['message'] = 'Reward registered successfully.'
        
    except IntegrityError as error:
        result['message'] = integrity_error_message(error)
        logging.error(error)
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result


