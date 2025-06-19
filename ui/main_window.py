from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Hello PySide6!")
        central_widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Welcome to PySide6!")
        layout.addWidget(label)

        central_widget.setLayout(layout)
        MainWindow.setCentralWidget(central_widget)
