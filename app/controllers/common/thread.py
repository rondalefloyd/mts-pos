import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import *
from app.utils.databases import postgres_db

class FetchLoginData(QThread):
    running = pyqtSignal(object)
    finished = pyqtSignal(object)
    
    def __init__(self):
        super().__init__()
        self._is_running = True
        
    def run(self):
        result = {
            'success': False,
            'message': 'N/A',
            'dict_data': {
                'organizations': [],
                'members': [],
                'users': [],
            },
        }
        
        try:
            organizations = Organization.select().order_by(Organization.UpdateTs.desc())
            members = Member.select().order_by(Member.UpdateTs.desc())
            users = User.select().order_by(User.UpdateTs.desc())

            result['message'] = "Please wait..."
            data = result['dict_data']
            
            # fetch organization data
            for i, organization in enumerate(organizations):
                data['organizations'].append({
                    'Id': organization.Id,
                    'TaxId': organization.TaxId,
                    'OrganizationName': organization.OrganizationName,
                    'Address': organization.Address,
                    'MobileNumber': organization.MobileNumber,
                    'AccessCode': organization.AccessCode,
                })
                
                self.running.emit({
                    'message': result['message'],
                    'current_count': i + 1,
                    'total_count': len(organizations),
                })
                
            # fetch member data
            for i, member in enumerate(members):
                data['members'].append({
                    'Id': member.Id,
                    'OrganizationId': member.OrganizationId,
                    'MemberName': member.MemberName,
                    'BirthDate': member.BirthDate,
                    'Address': member.Address,
                    'MobileNumber': member.MobileNumber,
                    'Points': member.Points,
                })
                
                self.running.emit({
                    'message': result['message'],
                    'current_count': i + 1,
                    'total_count': len(members),
                })
                
            # fetch user data
            for i, user in enumerate(users):
                data['users'].append({
                    'Id': user.Id,
                    'OrganizationId': user.OrganizationId,
                    'UserName': user.UserName,
                    'AccessCode': user.AccessCode,
                    'FullName': user.FullName,
                    'BirthDate': user.BirthDate,
                    'MobileNumber': user.MobileNumber,
                    'AccessLevel': user.AccessLevel,
                })
                
                self.running.emit({
                    'message': result['message'],
                    'current_count': i + 1,
                    'total_count': len(users),
                })
            
            result['success'] = True
            result['message'] = f"Success"
            
            self.finished.emit(result)
            
        except Exception as error:
            result['message'] = f"An error occured: {error}"
            
            self.finished.emit(result)
    
    def stop(self):
        self._is_running = False