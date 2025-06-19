import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
