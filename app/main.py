import os, sys
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.abspath('')) # required to change the default path

def startApp():
    print('app has started running')

    app = QApplication(sys.argv)
    
    from app.controllers.dialogs.Login import LoginController
    
    windowEvent = 'START_LOGIN'
    userId = None

    while True:
        if (windowEvent == 'START_LOGIN'):
            login = LoginController()
            login.exec()
            windowEvent = login.windowEvent
            userId = login.userId

        if (windowEvent == 'NO_EVENT'):
            break

    print('app has stopped running')    
    

if __name__ == "__main__":
    startApp()