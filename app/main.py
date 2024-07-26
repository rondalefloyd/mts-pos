import os, sys
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.components.Tester import Tester
from app.views.components.Login import Login

def _startApp():
    print('app has started running')
    
    app = QApplication(sys.argv)
    windowEvent = 'start/login'
    currentUserData = None

    while True:
        match windowEvent:
            case 'start/setup':
                print('TODO: start/setup')
                
            case 'start/sign-up':
                print('TODO: start/sign-up')
                
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