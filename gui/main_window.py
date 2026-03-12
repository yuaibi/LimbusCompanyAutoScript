from PySide6.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AutoBot")
        self.resize(400,300)