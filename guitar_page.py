from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QFrame, QVBoxLayout, QPushButton



class Guitar_study(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
 #creating the card
        self.card=QFrame()
        self.card.setObjectName("guitar_card")
        self.layout.addWidget(self.card)
#creating the layout for the cards txt a
        self.layout_for_card_txt=QVBoxLayout()
        self.card.setLayout(self.layout_for_card_txt)
 #creating the txt and adding it to created layout
        self.txt=QLabel("Lets Work on that Major Scale Broski")
        self.txt.setObjectName("guitar_card_txt")
        self.layout_for_card_txt.addWidget(self.txt)