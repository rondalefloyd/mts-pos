import os, sys, logging, math, json, pandas as pd
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import *
from app.utils.databases import postgres_db


class PrintThread(QThread):
    running = pyqtSignal(object)
    finished = pyqtSignal(object)
    
    def __init__(self, function_route, entry=None):
        super().__init__()
        self.function_route = function_route
        self.entry = entry
        self.isActive = True
    
    def run(self):
        result = {
            'success': False,
            'message': 'N/A',
            'dictData': {},
            'listData': [],
        }
         
        try:
            with postgres_db:
                if self.function_route == 'print_receipt':
                    result = self.print_receipt(self.entry, result)
                else:
                    result['message'] = f"'{self.function_route}' is an invalid function..."
                        
            logging.info('database operation done...')
            
        except Exception as exception:
            result['message'] = f"An error occured: {exception}"
            postgres_db.rollback()
            logging.error('exception: %s', exception)
            logging.info('database operation rolled back...')
            
        finally:
            postgres_db.close()
            logging.info('database closed...')
            
        self.finished.emit(result)
        # print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))

    def stop(self):
        self.isActive = False  # Set the flag to stop the thread
        
    # add function here
    def print_receipt(self, entry=None, result=None):
        try:
            result['success'] = True
            result['message'] = 'Items loaded'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
        