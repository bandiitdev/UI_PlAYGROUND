from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QFrame, QMainWindow
from PySide6.QtGui import QIcon, QPixmap


class CustomTitleBar(QWidget):
    def __init__(self, parent=QMainWindow()):
        super(CustomTitleBar, self).__init__(parent)