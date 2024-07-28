import os, sys
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.database import postgres_db
from app.views.components.Tester import Tester
from app.views.components.Setup import Setup
from app.views.components.SignUp import SignUp
from app.views.components.Login import Login
from app.views.components.Manage import Manage

def _checkDatabaseConnection():
    try:
        postgres_db.connect()
        if postgres_db.is_connection_usable():
            print("Database is open.")
        else:
            print("Database is closed.")
            
    except Exception as error:
        print(f"Failed to connect to the database: {error}")
    finally:
        postgres_db.close()

def _startApp():
    print('app has started running')
        
    app = QApplication(sys.argv)
    windowEvent = 'start/login'
    userData = None

    while True:
        match windowEvent:
            case 'start/setup':
                setup = Setup()
                setup.exec()
                windowEvent = setup.windowEvent
                
            case 'start/sign-up':
                signUp = SignUp()
                signUp.exec()
                windowEvent = signUp.windowEvent
                
            case 'start/login':
                login = Login()
                login.exec()
                userData = login.userData
                windowEvent = login.windowEvent
                
            case 'start/manage':
                manage = Manage(userData)
                manage.show()
                app.exec()
                userData = manage.userData
                windowEvent = manage.windowEvent
                
            case 'start/tester':
                tester = Tester()
                tester.exec()
                
            case _:
                break
                
    print('app has stopped running')    
    
if __name__ == "__main__":
    _checkDatabaseConnection()
    _startApp()
    
    
# TODO: continue doing the Sales (Items, Stock), Transaction (Sales)