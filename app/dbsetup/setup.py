import sys, os
from PyQt5.QtWidgets import *
from Setup_ui import Ui_DialogSetup

class Setup(Ui_DialogSetup, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButtonAllow.clicked.connect(lambda: self.onPushButtonAllowClicked(self.lineEditDirectory.text()))

    def onPushButtonAllowClicked(self, directory):
        directory = directory.replace('\\', '/')
        directory = "C:/Program Files/PostgreSQL/17/data/" if directory == "" else directory
        pgHbaConfPath = f"{directory}/pg_hba.conf"  # Update to your PostgreSQL version and directory
        postgresqlConfPath = f"{directory}/postgresql.conf"
        
        try:
            self.modifyPgHbaConf(pgHbaConfPath)
            self.modifyPostgreSQLConf(postgresqlConfPath)
            self.restartPostgreSQL(directory)
            
            self.labelStatus.setText('Success')
        except Exception as error:
            self.labelStatus.setText(f'Failed: {error}')
        
    def backupFile(self, filePath):
        backup_path = filePath + ".bak"
        if not os.path.exists(backup_path):
            with open(filePath, 'r') as original, open(backup_path, 'w') as backup:
                backup.write(original.read())
            print(f"Backup created: {backup_path}")
    
    def modifyPgHbaConf(self, filePath):
        self.backupFile(filePath)

        # Define the new rule to be added
        new_rule = "host    all             all             0.0.0.0/0               md5\n"

        # Read the file to check if the rule already exists
        with open(filePath, 'r') as file:
            existing_lines = file.readlines()

        # Check if the rule already exists in the file
        if new_rule not in existing_lines:
            with open(filePath, 'a') as file:
                file.write(new_rule)
                print("Added rule to pg_hba.conf to allow connections from any IP.")
        else:
            print("The rule already exists in pg_hba.conf. No changes made.")

    
    def modifyPostgreSQLConf(self, filePath):
        self.backupFile(filePath)
        
        with open(filePath, 'r') as file:
            lines = file.readlines()
        
        with open(filePath, 'w') as file:
            for line in lines:
                if line.startswith("# listen_addresses") or line.startswith("#listen_addresses") or line.startswith("listen_addresses"):
                    file.write("listen_addresses = '*'\n")  # Set to allow all IPs
                else:
                    file.write(line)
            print("Modified postgresql.conf to listen on all interfaces.")
    
    def restartPostgreSQL(self, directory):
        os.system(f'pg_ctl -D "{directory}" stop')
        os.system(f'pg_ctl -D "{directory}" start')
        QMessageBox.information(self, "Success", "Done. Please double check the server if it's running at services.msc")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Setup()
    window.show()
    sys.exit(app.exec_())