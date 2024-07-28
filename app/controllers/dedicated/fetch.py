import os, sys, logging, math
from peewee import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import Users, Organizations
from app.controllers.common.messages import (
    class_error_message, 
    function_route_error_message,
    function_route_not_exist,
)
from app.utils.database import postgres_db

logging.basicConfig(level=logging.INFO)

class FetchThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function_route, entry=None):
        super().__init__()
        self.function_route = function_route
        self.entry = entry
    
    def run(self):
        result = {
            'success': False,
            'message': class_error_message(self.__class__.__name__),
            'data': [],
        }
        try:
            with postgres_db:
                match self.function_route:
                    case 'pos/fetch/user/all':
                        result = fetch_user()
                    case 'pos/fetch/organization/all':
                        result = fetch_organization()
                    case 'pos/fetch/user/all/keyword/paginated':
                        result = fetch_user_with_pagination_by_keyword(self.entry)
                    case _:
                        result['message'] = function_route_not_exist(self.function_route, self.__class__.__name__)


            self.finished.emit(result)
            
        except Exception as error:
            result['message'] = function_route_error_message(self.function_route, error)
            postgres_db.rollback()
            self.finished.emit(result)
            logging.error('error: ', error)
            logging.info('database rolled back...')
            
        finally:
            postgres_db.close()
            logging.info('database closed...')

def fetch_user():
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': []
    }
    
    try:
        users = Users.select().order_by(Users.UpdateTs.desc())
        
        for user in users:
            result['success'] = True
            result['message'] = 'Fetch successful.'
            result['data'].append({
                'id': user.Id,
                'organizationId': user.OrganizationId,
                'userName': user.UserName,
                'accessCode': user.AccessCode,
                'fullName': user.FullName,
                'birthDate': user.BirthDate,
                'mobileNumber': user.MobileNumber,
                'accessLevel': user.AccessLevel,
                'updateTs': user.UpdateTs,
            })
        
    except Users.DoesNotExist:
        result['message'] = 'Fetch failed. Users not found.'
        
    return result

def fetch_organization():
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': []
    }
    
    try:
        organizations = Organizations.select().order_by(Organizations.UpdateTs.desc())
        
        for organization in organizations:
            result['success'] = True
            result['message'] = 'Fetch successful.'
            result['data'].append({
                'id': organization.Id,
                'taxId': organization.TaxId,
                'organizationName': organization.OrganizationName,
                'address': organization.Address,
                'mobileNumber': organization.MobileNumber,
                'accessCode': organization.AccessCode,
                'updateTs': organization.UpdateTs,
            })
        
    except Organizations.DoesNotExist:
        result['message'] = 'Fetch failed. Organizations not found.'
        
    return result

def fetch_user_with_pagination_by_keyword(entry):
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': [],
        'totalPages': 1,
    }
    
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        query = Users.select().where(
            (Users.UserName.cast('TEXT').like(keyword)) |
            (Users.AccessCode.cast('TEXT').like(keyword)) |
            (Users.FullName.cast('TEXT').like(keyword)) |
            (Users.BirthDate.cast('TEXT').like(keyword)) |
            (Users.MobileNumber.cast('TEXT').like(keyword)) |
            (Users.AccessLevel.cast('TEXT').like(keyword)) |
            (Users.UpdateTs.cast('TEXT').like(keyword))
        ).order_by(Users.UpdateTs.desc())
        
        total_count = query.count()
        
        paginated_users = query.limit(limit).offset(offset)
        
        for user in paginated_users:
            result['data'].append({
                'id': user.Id,
                'userName': user.UserName,
                'accessCode': user.AccessCode,
                'fullName': user.FullName,
                'birthDate': user.BirthDate,
                'mobileNumber': user.MobileNumber,
                'accessLevel': user.AccessLevel,
                'updateTs': user.UpdateTs,
            })
        
        result['totalPages'] = math.ceil(total_count / limit)
        
        result['success'] = True
        result['message'] = 'Fetch successful.'
        
    except Users.DoesNotExist:
        result['message'] = 'Fetch failed. Users not found.'
        
    return result