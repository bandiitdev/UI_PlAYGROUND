from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QFrame, QVBoxLayout, QPushButton

#This code is responsible for the page that shows up after you hit open from the dashboard
class Open_Button(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
#creating a card so the page won't just be blank
        self.card1=QFrame()
        self.card1.setObjectName("card1_for_ob")
        self.layout.addWidget(self.card1)
#creating another layout for contents inside of card and actually creating the contents
        self.layout_for_card1=QVBoxLayout()
        self.card1.setLayout(self.layout_for_card1)
        self.txt_for_card1=QLabel("You Clicked Open.Get ready to work hard!")
        self.txt_for_card1.setObjectName("txt_for_card1")
        self.layout_for_card1.addWidget(self.txt_for_card1)




