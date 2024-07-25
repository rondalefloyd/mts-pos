import os, sys
from peewee import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# TODO: move this to models
sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.model_association import User
from app.utils.database import db

# Connect to the database
class Authenticate(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self):
        super().__init__()
        pass
    
    def run(self):        
        db.connect()

        # Query the User table
        users = User.select()

        # Print the users
        print("Users in the database:")
        for user in users:
            print(user.Id, user.UserName, user.FullName)
            
        self.finished.emit(users)

        # Close the database connection
        db.close()
        pass