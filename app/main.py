import os, sys
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.abspath('')) # required to change the default path

def startApp():
    print('app has started running')

    app = QApplication(sys.argv)
    
    from app.controllers.dialogs.Login import LoginController
    from app.controllers.dialogs.SignUp import SignUpController
    from app.controllers.forms.Manage import ManageController
    from app.controllers.dialogs.Setup import SetupController
    
    windowEvent = 'START_LOGIN'
    userId = None

    while True:
        if (windowEvent == 'START_LOGIN'):
            login = LoginController()
            login.exec()
            windowEvent = login.windowEvent
            userId = login.userId

        if (windowEvent == 'START_SETUP'):
            setup = SetupController()
            setup.exec()
            windowEvent = setup.windowEvent

        if (windowEvent == 'START_SIGNUP'):
            signup = SignUpController()
            signup.exec()
            windowEvent = signup.windowEvent

        if (windowEvent == 'START_MANAGE'):
            manage = ManageController(userId)
            manage.show()
            app.exec()
            windowEvent = manage.windowEvent
            userId = manage.userId
            
        if (windowEvent == 'NO_EVENT'):
            break

    print('app has stopped running')    
    

if __name__ == "__main__":
    startApp()