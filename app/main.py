import os, sys

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.pyqt5.QtWidgets import *
from app.utils.pyqt5.QtCore import *
from app.utils.pyqt5.QtGui import *
from app.utils.databases import postgres_db
from app.utils.global_variables import *
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
    # TODO: use the fusion style and modify
    _setAppStyleSheet(app)
    
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
            # manage.showFullScreen()
            manage.show()
            app.exec()
            authData = manage.authData
            windowEvent = manage.windowEvent
        else:
            break
                
    print('app has stopped running') 

def _setAppStyleSheet(app:QApplication):
    app.setWindowIcon(QIcon(os.path.abspath('app/views/assets/images/barcode-solid.svg')))
    app.setStyle("Fusion")
    
    qssFilePaths = [
        # os.path.abspath('app/views/assets/styles/dedicated.qss'),
        os.path.abspath('app/views/assets/styles/experimental.qss'),
    ]
    
    styleSheet = ""
    for filePath in qssFilePaths:
        with open(filePath, 'r') as file:
            styleSheet += file.read() + "\n"
    
    app.setStyleSheet(styleSheet)   
    
if __name__ == "__main__":
    _checkDatabaseConnection()
    _startApp()