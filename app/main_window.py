from PySide6.QtWidgets import QMainWindow
from app.ui_main_window import Ui_MainWindow  # Adjust the import based on your structure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Event listeners go here
        self.ui.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print("Button clicked!")
