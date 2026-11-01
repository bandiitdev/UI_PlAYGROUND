from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QFrame, QVBoxLayout, QPushButton

#creating the layout for the page
class IT_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
#creating the card and adding it to the mian layout
        self.card=QFrame()
        self.card.setObjectName("IT_Page_Card")
        self.layout.addWidget(self.card)
#creating a layout for the inner contents / txt of our card
        self.layout_for_card=QVBoxLayout()
        self.card.setLayout(self.layout_for_card)
        #added txt to my card
        self.txt=QLabel("Help Desk on the way Bandit!")
        self.txt.setObjectName("IT_PAGE_TXT")
        self.layout_for_card.addWidget(self.txt)

