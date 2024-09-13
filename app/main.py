import os, sys
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.databases import postgres_db
from app.utils.global_variables import *
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
    
    qssFilePaths = [
        os.path.abspath('app/views/assets/styles/common.qss'),
        os.path.abspath('app/views/assets/styles/dedicated.qss'),
    ]
    
    # Read and concatenate QSS files
    styleSheet = ""
    for filePath in qssFilePaths:
        with open(filePath, 'r') as file:
            styleSheet += file.read() + "\n"
    
    # Apply the concatenated QSS to the application
    app.setStyleSheet(styleSheet)
    
    windowEvent = EVENT_START_LOGIN
    authData = None

    while True:
        if windowEvent == EVENT_START_SETUP:
            setup = Setup()
            setup.exec()
            windowEvent = setup.windowEvent
        elif windowEvent == EVENT_START_SIGNUP:
            signUp = SignUp()
            signUp.exec()
            windowEvent = signUp.windowEvent
        elif windowEvent == EVENT_START_LOGIN:
            login = Login()
            login.exec()
            authData = login.authData
            windowEvent = login.windowEvent
        elif windowEvent == EVENT_START_MANAGE:
            manage = Manage(authData)
            manage.show()
            app.exec()
            authData = manage.authData
            windowEvent = manage.windowEvent
        elif windowEvent == EVENT_START_TESTER:
            tester = Tester()
            tester.exec()
        else:
            break
                
    print('app has stopped running')    
    
if __name__ == "__main__":
    _checkDatabaseConnection()
    _startApp()
    
# TODO: implement infra where theres a master and slave server (requires two devices)
# TODO: add design to the UI
# TODO: write a cleaner version of the managesales codes especially the data entries object etc.
# TODO: add populate combobox in the components that doesnt have it
# TODO: check the variable names
# TODO: set clear button enabled for all line edit
# TODO: fix the sizes of the QTableWidgetItems in all table widgets
# TODO: add peso sign in each bill formatted labels