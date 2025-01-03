from PySide6.QtWidgets import QMainWindow, QApplication
from screens.loginScreen_ui import Ui_LoginDialog
import sys

class LoginMain(QMainWindow,Ui_LoginDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginMain()
    window.show()
    app.exec()