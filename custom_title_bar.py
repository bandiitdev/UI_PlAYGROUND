from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QFrame, QMainWindow
from PySide6.QtGui import QIcon, QPixmap, Qt


class CustomTitleBar(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.setObjectName("CustomTitleBar")

        self.layout.setContentsMargins(12,0,12,0)

        self.layout.setSpacing(8)
        self.setFixedHeight(36)

#creating the buttons for our title bar
        self.close_button = QPushButton("x")
        self.close_button.setObjectName("close_button")
        self.minimize_button = QPushButton("-")
        self.minimize_button.setObjectName("minimize_button")
        self.expand_button = QPushButton("+")
        self.expand_button.setObjectName("expand_button")

#adding buttons to layout
        self.layout.addWidget(self.close_button)
        self.layout.addWidget(self.minimize_button)
        self.layout.addWidget(self.expand_button)
        self.layout.addStretch()




