import sys
import os
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import threading

sys.path.append(os.path.abspath(''))
from app.models.model_association import User

onlineUrl = f"{os.getenv('ONLINE_SQLALCHEMY_BASE_URL')}://{os.getenv('TURSO_DB_URL')}/?authToken={os.getenv('TURSO_DB_AUTH_TOKEN')}"

try:
    engine = create_engine(url=onlineUrl, echo=True)
    sessionMaker = sessionmaker(bind=engine)
    status = 'ONLINE'
except Exception as error:
    print('error:', error)


class WorkerThread(QThread):
    result_ready = pyqtSignal(object)

    def __init__(self, db_path, parent=None):
        super().__init__(parent)
        self.db_path = db_path
        self.stop_event = threading.Event()

    def run(self):
        session = sessionMaker()
        print('--A session.is_active():', session.is_active)
        results = session.query(User).all()
        session.close()

        engine.dispose()

        print('--B session.is_active():', session.is_active)
        self.result_ready.emit(results)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Example")

        self.label = QLabel("Results will be shown here", self)
        self.label.move(50, 50)

        self.button = QPushButton("Fetch Data", self)
        self.button.move(50, 100)
        self.button.clicked.connect(self.on_button_clicked)

        self.thread = None

    def on_button_clicked(self):
        if self.thread is not None and self.thread.isRunning():
            self.thread.stop()  # Stop the thread gracefully
            self.thread.wait()

        self.thread = WorkerThread("path_to_your_database.db")
        self.thread.result_ready.connect(self.update_label)
        self.thread.start()

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
