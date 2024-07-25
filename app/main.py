import os, sys
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.abspath('')) # required to change the default path
from app.views.components.Tester import Tester

def _startApp():
    print('app has started running')
    
    app = QApplication(sys.argv)
    windowEvent = 'START_LOGIN'
    currentUserData = None

    while True:
        if windowEvent == 'START_SETUP':
            print('TODO: START_SETUP')
            pass
        if windowEvent == 'START_LOGOUT':
            print('TODO: START_LOGOUT')
            pass
        if windowEvent == 'START_LOGIN':
            print('TODO: START_LOGIN')
            pass
        if windowEvent == 'START_MANAGE':
            print('TODO: START_MANAGE')
            pass
        if windowEvent == 'START_TESTER':
            tester = Tester()
            tester.exec()

    print('app has stopped running')    
    
if __name__ == "__main__":
    _startApp()