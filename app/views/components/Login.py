# import
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.config import *
from app.views.templates.Login_ui import Ui_DialogLogin
from app.views.components.Loading import Loading
from app.views.validator import nonSpaceTextFormatValidator
from app.controllers.common.thread import *
from app.controllers.dedicated.authenticate import *

class Login(Ui_DialogLogin, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.source_data = None
        self.window_event = EVENT_NO_EVENT
        self.loading = Loading()
        
        self._fetchLoginData()
        
        self.pushButtonLogin.clicked.connect(self._onPushButtonLoginClicked)
        
    def _onPushButtonLoginClicked(self):
        print('self.source_data:', json.dumps(self.source_data, indent=4, default=str))
        
    def _fetchLoginData(self):
        self.fetchLoginData = FetchLoginData()
        self.fetchLoginData.start()
        self.fetchLoginData.running.connect(self._onFetchLoginDataRunning)
        self.fetchLoginData.finished.connect(self._onFetchLoginDataFinished)
        self.loading.exec()
        
    def _onFetchLoginDataRunning(self, status):
        self.loading.labelMessage.setText(f"{status['message']}")
        self.loading.progressBarCount.setValue(status['current_count'])
        self.loading.progressBarCount.setMaximum(status['total_count'])
        print('status:', status)
        pass
    def _onFetchLoginDataFinished(self, result):
        if result['success'] is False:
            self.loading.close()
            print(result['message'])
            return
            
        self.source_data = result['dict_data']
        self.loading.close()
        print(result['message'])
        