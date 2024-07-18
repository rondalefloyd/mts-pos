import os, sys
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.abspath('')) # required to change the default path

def startApp():
    print('app has started running')

    app = QApplication(sys.argv)
    
    from app.controllers.Login import LoginController
    from app.controllers.Manage import ManageController
    
    windowEvent = 'START_LOGIN'
    currentUserData = None

    while True:
        if (windowEvent == 'START_LOGIN'):
            login = LoginController()
            login.exec()
            windowEvent = login.windowEvent
            currentUserData = login.currentUserData
            
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
    startApp()