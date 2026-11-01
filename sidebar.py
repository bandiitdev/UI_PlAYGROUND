from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
from settings import Settings_Page

class Sidebar(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("Sidebar")
        self.left_side = QVBoxLayout()
        self.left_side.setContentsMargins(0,0,0,0)
        self.left_side.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Hbox = QHBoxLayout()
        self.setLayout(self.Hbox)




        self.logo = QLabel()
        pixmap = QPixmap("images/logo.png")
        scaled_pixmap = pixmap.scaled(
            90,90,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation)
        self.logo.setPixmap(scaled_pixmap)
        self.left_side.addWidget(self.logo,0,Qt.AlignmentFlag.AlignCenter)

        self.dashboard=QPushButton("Dashboard")
        self.dashboard.setIcon(QIcon("images/house.svg"))
        self.dashboard.setMinimumWidth(75)
        self.dashboard.setMaximumWidth(200)
        self.left_side.addWidget(self.dashboard)

        self.left_side.addStretch()

        self.settings=QPushButton("Settings")
        self.settings.setIcon(QIcon("images/settings.svg"))
        self.settings.setMinimumWidth(75)
        self.settings.setMaximumWidth(200)
        self.left_side.addWidget(self.settings,0,Qt.AlignmentFlag.AlignCenter)

        self.vert_line=QFrame()
        self.Hbox.addLayout(self.left_side)
        self.Hbox.addWidget(self.vert_line)




















