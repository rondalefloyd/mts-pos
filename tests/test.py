import sys, os
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sqlite3
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import registry, sessionmaker

sys.path.append(os.path.abspath(''))
from app.models.model_association import session, status, User, Organization, Authentication


class WorkerThread(QThread):
    result_ready = pyqtSignal(object)
    
    def __init__(self, db_path, parent=None):
        super().__init__(parent)
        self.db_path = db_path

    def run(self):
        # Perform database operations here
        url = os.getenv("TURSO_DATABASE_URL")
        auth_token = os.getenv("TURSO_AUTH_TOKEN")

        connection = sqlite3.connect('C:/Users/mimoy/Documents/GitHub/mts-pos/tests/database/pos.db')
        cursor = connection.cursor()
        
        # Example operation
        cursor.execute("SELECT * FROM User")
        results = cursor.fetchall()
        
        connection.close()
        
        # onlineUrl = f"{os.getenv('ONLINE_SQLALCHEMY_BASE_URL')}://{os.getenv('TURSO_DB_URL')}/?authToken={os.getenv('TURSO_DB_AUTH_TOKEN')}"
        # session = sessionmaker(bind=create_engine(
        #     url = onlineUrl, 
        #     connect_args = {'check_same_thread': False}, 
        #     echo = True
        # ))()

        # results = session.query(User).all()
        # Emit results to be handled by the main thread
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
            self.thread.quit()
            self.thread.wait()
        
        self.thread = WorkerThread("path_to_your_database.db")
        self.thread.result_ready.connect(self.update_label)
        self.thread.start()

    def update_label(self, results):
        # Update the GUI with results
        self.label.setText(str(results))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
