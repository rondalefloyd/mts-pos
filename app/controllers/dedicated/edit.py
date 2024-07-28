import os, sys, logging
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import (
    Members,
)
from app.controllers.common.messages import (
    class_error_message, 
    function_route_error_message,
    function_route_not_exist,
)
from app.utils.database import postgres_db

logging.basicConfig(level=logging.INFO)

class EditThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function_route, entry=None):
        super().__init__()
        self.function_route = function_route
        self.entry = entry
    
    def run(self):
        result = {
            'success': False,
            'message': class_error_message(self.__class__.__name__),
        }
        try:
            with postgres_db:
                match self.function_route:
                    case 'pos/edit/member':
                        result = edit_member(self.entry)
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

def edit_member(entry):
    result = {
        'success': False,
        'message': 'Update failed.',
    }
    
    try:
        # Check if the member to update exists by ID
        member = Members.get(Members.Id == entry['id'])
        
        # Check if another member with the same name exists
        try:
            existing_member = Members.get(Members.MemberName == entry['memberName'])
            if existing_member.Id != member.Id:
                result['message'] = 'Member already exists with the given name.'
                return result
        except Members.DoesNotExist:
            pass  # No other member with the same name exists, so we can proceed
        
        # Update member details
        member.MemberName = entry['memberName']
        member.BirthDate = entry['birthDate']
        member.Address = entry['address']
        member.MobileNumber = entry['mobileNumber']
        member.Points = entry['points']
        member.save()  # Save the changes to the database
        
        result['success'] = True
        result['message'] = 'Member updated successfully.'
        
    except Members.DoesNotExist:
        result['message'] = 'Member does not exist.'
        
    except Exception as error:
        result['message'] = f'Update failed due to: {error}'
        
    return result

