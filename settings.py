from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFrame, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QStackedLayout,QGridLayout
from PySide6.QtGui import QIcon
from PySide6.QtGui import QFont


class Settings_Page(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.layout=QHBoxLayout()
        self.setLayout(self.layout)

        self.card_1 = QFrame()
        self.second_widget=QWidget()
        self.second_widget.setObjectName("second_widget")
        self.second_layout = QGridLayout()
        self.second_widget.setLayout(self.second_layout)


        self.card_1.setObjectName("card_1_settings_page")
        self.layout.addWidget(self.card_1)
        self.card_1.setMaximumHeight(500)
        self.card_1.setMaximumWidth(500)

        self.card_2=QFrame()
        self.card_2.setObjectName("card_2_settings_page")
        self.layout.addWidget(self.card_2)
        self.card_2.setMaximumWidth(500)
        self.card_2.setMaximumHeight(500)



        self.frame_layout=QVBoxLayout()
        self.frame_layout.setContentsMargins(0,0,0,0)
        self.frame_layout.addWidget(self.second_widget)
        self.card_1.setLayout(self.frame_layout)

        self.frame2_layout = QVBoxLayout()
        self.card_2.setLayout(self.frame2_layout)
        self.frame2_layout.setSpacing(12)

        self.description_1 = QLabel()
        self.description_1.setObjectName("description_1")
        self.description_1.setText("Bandit OS")


        self.second_layout.addWidget(self.description_1,0,0,Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        self.second_layout.setContentsMargins(20,25,0,0)

        self.description_2 = QLabel()
        self.description_2.setObjectName("description_2")
        self.description_2.setText("This is a practice project to learn more about PySide6 GUI's"
                                   "\n\n\n\nClick below to learn more about the application")
        self.frame2_layout.addWidget(self.description_2)
        self.frame2_layout.addStretch()

        self.description_2.setContentsMargins(10,20,10,0)
        self.frame2_layout.setContentsMargins(20, 0, 20, 60)



        self.about_button=QPushButton("About")
        self.about_button.setObjectName("about_button")
        self.about_button.setIcon(QIcon("images/info.png"))
        self.frame2_layout.addWidget(self.about_button)


        self.system_info=QFrame()
        self.system_info.setObjectName("system_info")
        self.frame2_layout.addWidget(self.system_info)
        self.layout_3=QVBoxLayout()
        self.system_info.setLayout(self.layout_3)
        self.about_button.clicked.connect(self.toggle_system_info)
        self.system_info.hide()
        self.application=QLabel()
        self.application.setObjectName("app")
        self.application.setText("Application")
        self.application_name=QLabel()
        self.application_name.setObjectName("application_name")
        self.application_name.setText("Bandit OS")
        self.row_layout=QHBoxLayout()
        self.row_layout.addWidget(self.application)
        self.row_layout.addStretch()
        self.row_layout.addWidget(self.application_name)
        self.layout_3.addLayout(self.row_layout)




    def toggle_system_info(self):
        self.system_info.setVisible(not self.system_info.isVisible())























