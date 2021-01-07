import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget


class GUI():
    def __init__(self):
        self.build_gui()

    def build_gui(self):
        app = QApplication(sys.argv)
        window = QWidget()
        window.show()

        app.exec_()
