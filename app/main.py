import os, sys
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.abspath('')) # required to change the default path

def _startApp():
    print('app has started running')
    
    app = QApplication(sys.argv)
    windowEvent = 'START_LOGIN'
    currentUserData = None

    print('app has stopped running')    
    
if __name__ == "__main__":
    _startApp()