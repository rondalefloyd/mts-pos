import os, sys
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.abspath('')) # required to change the default path
from app.controllers.Login import LoginController
from app.controllers.SignUp import SignUpController
from app.controllers.Manage import ManageController
from app.controllers.Setup import SetupController

def _startApp():
    print('app has started running')
    
    app = QApplication(sys.argv)
    windowEvent = 'START_LOGIN'
    currentUserData = None

    while True:
        if (windowEvent == 'START_LOGIN'):
            login = LoginController()
            login.exec()
            windowEvent = login.windowEvent
            currentUserData = login.currentUserData

        if (windowEvent == 'START_SETUP'):
            setup = SetupController()
            setup.exec()
            windowEvent = setup.windowEvent

        if (windowEvent == 'START_SIGNUP'):
            signup = SignUpController()
            signup.exec()
            windowEvent = signup.windowEvent

        if (windowEvent == 'START_MANAGE'):
            manage = ManageController(currentUserData)
            manage.show()
            app.exec()
            windowEvent = manage.windowEvent
            currentUserData = manage.currentUserData
            
        if (windowEvent == 'NO_EVENT'):
            break

    print('app has stopped running')    
    

if __name__ == "__main__":
    _startApp()