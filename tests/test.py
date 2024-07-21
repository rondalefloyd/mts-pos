import sys
import os
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import threading

sys.path.append(os.path.abspath(''))
from app.models.model_association import User
from app.utils.crud import CRUDThread

# class WorkerThread(QThread):
#     result_ready = pyqtSignal(object)

#     def __init__(self, db_path, parent=None):
#         super().__init__(parent)
#         self.db_path = db_path
#         self.stop_event = threading.Event()

#     def run(self):
#         session = sessionMaker()
#         print('--A session.is_active():', session.is_active)
#         results = session.query(User).all()
#         session.close()

#         engine.dispose()

#         print('--B session.is_active():', session.is_active)
#         self.result_ready.emit(results)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Example")

        self.label = QLabel("Results will be shown here", self)
        self.label.move(50, 50)

        self.button = QPushButton("Fetch Data", self)
        self.button.move(50, 100)
        self.button.clicked.connect(self.on_button_clicked)


    def on_button_clicked(self):


        self.crudThread = CRUDThread()
        self.crudThread.setRequirements(self, '_getAllUserWithPaginationByKeyword', {
            'keyword': f"",
            'currentPage': 1
        })
        self.crudThread.finished.connect(self.update_label)
        self.crudThread.start()

    def update_label(self, results):
        # Update the GUI with results
        self.label.setText(str(results))

        active_threads = threading.enumerate()
        print("Current running threads:")
        for thread in active_threads:
            print(thread.name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
