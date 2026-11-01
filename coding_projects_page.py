from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QFrame, QVBoxLayout, QPushButton


class Coding_Projects_Page(QWidget):
#creating page layout
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
#creating frame / card for page
        self.card=QFrame()
        self.card.setObjectName("card_for_coding_projects")
        self.layout.addWidget(self.card)
#creating layout for card's content
        self.layout_for_cards_contents=QVBoxLayout()
        self.card.setLayout(self.layout_for_cards_contents)
#creating labels/text for going inside the card
        self.project1=QLabel("Project 1")
        self.project1.setObjectName("project_1")
        self.project2=QLabel("Project 2")
        self.project2.setObjectName("project_2")
        self.project3=QLabel("Project 3")
        self.project3.setObjectName("project_3")
        self.project4=QLabel("Project 4")
        self.project4.setObjectName("project_4")
#adding widgets to layout
        self.layout_for_cards_contents.addWidget(self.project1)
        self.layout_for_cards_contents.addWidget(self.project2)
        self.layout_for_cards_contents.addWidget(self.project3)
        self.layout_for_cards_contents.addWidget(self.project4)


