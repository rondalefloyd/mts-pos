import os, sys, logging
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import (
    Members,
)
from app.controllers.common.validator import is_entry_valid
from app.controllers.common.messages import (
    exception_error_message,
    integrity_error_message,
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
            'message': 'N/A',
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
            result['message'] = exception_error_message(error)
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
    
    if is_entry_valid(['memberName', 'birthDate', 'address', 'mobileNumber', 'points'], entry) is False:
        result['message'] = 'Fields cannot be empty or blank.'
        return result
    
    try:
        # Check if the member to update exists by ID
        members = Members.select().where(Members.Id == entry['id'])
        
        if not members.exists():
            result['message'] = 'Member does not exist.'
            return result
        
        members = members.first()
        
        # Check if another member with the same name exists
        existingMembers = Members.select().where(Members.MemberName == entry['memberName'])
        
        if existingMembers.exists():
            existingMembers = existingMembers.first()
            if existingMembers.Id != members.Id:
                result['message'] = 'Member already exists with the given name.'
                return result
        
        # Update member details
        members.MemberName = entry['memberName']
        members.BirthDate = entry['birthDate']
        members.Address = entry['address']
        members.MobileNumber = entry['mobileNumber']
        members.Points = entry['points']
        members.save()  # Save the changes to the database
        
        result['success'] = True
        result['message'] = 'Member updated successfully.'
        
    except IntegrityError as error:
        result['message'] = integrity_error_message(error)
        logging.error(error)
        
    except Exception as error:
        result['message'] = exception_error_message(error)
         
    return result


