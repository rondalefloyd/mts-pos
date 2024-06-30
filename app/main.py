import os, sys
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.abspath('')) # required to change the default path
from app.controllers.dialogs.login import Login
from app.controllers.dialogs.signup import SignUp
from app.controllers.forms.manage import Manage
from app.controllers.dialogs.setup import Setup

def startApp():
    print('app has started running')

    app = QApplication(sys.argv)
    windowEvent = 'START_LOGIN'
    userId = None

    while True:
        if (windowEvent == 'START_LOGIN'):
            login = Login()
            login.exec()
            windowEvent = login.windowEvent
            userId = login.userId

        if (windowEvent == 'START_SIGNUP'):
            signup = SignUp()
            signup.exec()
            windowEvent = signup.windowEvent

        if (windowEvent == 'START_MANAGE'):
            manage = Manage(userId)
            manage.show()
            app.exec()
            windowEvent = manage.windowEvent
            userId = manage.userId

        if (windowEvent == 'START_SETUP'):
            setup = Setup()
            setup.exec()
            windowEvent = setup.windowEvent
            
        if (windowEvent == 'NO_EVENT'):
            break

    print('app has stopped running')    
    

if __name__ == "__main__":
    startApp()