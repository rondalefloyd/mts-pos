import os, sys, logging, math, json, pandas as pd, win32com.client, pythoncom
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from docx import Document

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
            # TODO: clean this up and make sure the code structure follows the standards
            pythoncom.CoInitialize()
            # Load the DOCX template
            template_path = os.path.abspath('app/utils/receipt_template.docx')
            document = Document(template_path)
            
            # Define the mapping of placeholders to their corresponding values from the JSON object
            placeholders = {
                '<OrganizationName>': entry['organization']['organizationName'],
                '<Address>': entry['organization']['address'],
                '<TransactionDate>': datetime.now().strftime('%Y-%m-%d'),  # Example: current date
                '<ReferenceId>': entry['order']['referenceId'],
                '<TaxId>': entry['organization']['taxId'],
                '<MachineId>': '123456',  # Example: static value
                '<Quantity>': '\n'.join([str(item['quantity']) for item in entry['order']['item']]),
                '<ItemName>': '\n'.join([item['itemName'] for item in entry['order']['item']]),
                '<Total>': '\n'.join([str(item['total']) for item in entry['order']['item']]),
                '<Subtotal>': str(entry['summary']['subtotal']),
                '<Discount>': str(entry['summary']['discount']),
                '<Tax>': str(entry['summary']['tax']),
                '<GrandTotal>': str(entry['summary']['grandTotal']),
                '<Amount>': str(entry['payment']['amount']),
                '<Type>': entry['payment']['type'],
                '<Change>': str(entry['payment']['change']),
                '<UserName>': entry['user']['userName'],
                '<MobileNumber>': entry['user']['mobileNumber'],
            }
            
            # Replace placeholders in paragraphs and tables
            elements = document.paragraphs + [paragraph for table in document.tables for row in table.rows for cell in row.cells for paragraph in cell.paragraphs]
            for element in elements:
                for run in element.runs:
                    for placeholder, value in placeholders.items():
                        if placeholder in run.text:
                            run.text = run.text.replace(placeholder, value)
            
            # Save the modified document
            output_path = os.path.abspath('app/utils/output.docx')
            document.save(output_path)
            
            # Print the document (Windows-specific)
            word = win32com.client.Dispatch("Word.Application")
            word.Visible = False
            doc = word.Documents.Open(output_path)
            doc.PrintOut()
            doc.Close(False)
            word.Quit()
            
            pythoncom.CoInitialize()
            
            result['success'] = True
            result['message'] = 'Receipt generated and sent to printer successfully'
            result['dictData'] = placeholders  # Optionally return the placeholders and their values
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
        