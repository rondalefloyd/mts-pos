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
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
    finally:
        postgres_db.close()

def _startApp():
    print('app has started running')
    
    _checkDatabaseConnection()
    
    app = QApplication(sys.argv)
    windowEvent = 'start/login'
    currentUserData = None

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
                windowEvent = login.windowEvent
                
            case 'start/manage':
                print('TODO: start/manage')
                
            case 'start/tester':
                tester = Tester()
                tester.exec()
                
            case _:
                break
                
    print('app has stopped running')    
    
if __name__ == "__main__":
    _startApp()