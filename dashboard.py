from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QFrame, QVBoxLayout, QPushButton


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
#establishing main layout and setting content margins up so I can add text up top
        self.widget_main_layout = QVBoxLayout()
        self.setLayout(self.widget_main_layout)
        self.widget_main_layout.setContentsMargins(20,40,0,0)
        self.widget_main_layout.setSpacing(5)
#creating the cards and the layout for them + naming them to style them up
        self.card1_top= QFrame()
        self.card1_top.setObjectName("card1_top")
        self.card1_bottom = QFrame()
        self.card1_bottom.setObjectName("card1_bottom")
        self.card2_bottom = QFrame()
        self.card2_bottom.setObjectName("card2_bottom")
        self.card3_bottom = QFrame()
        self.card3_bottom.setObjectName("card3_bottom")
        self.layout_for_bottom_cards= QHBoxLayout()
 # creating the QLabels as the text up top
        self.welcome_label = QLabel()
        self.welcome_label.setObjectName("welcome_label")
        self.welcome_label.setText("Welcome Back,Bandit")
#adding card widgets to my main layout and the layouts for them + Welcome Label
        self.widget_main_layout.addWidget(self.welcome_label,0,alignment=Qt.AlignmentFlag.AlignTop)
        self.widget_main_layout.addWidget(self.card1_top,1)
        self.widget_main_layout.addLayout(self.layout_for_bottom_cards,1)
#adding widgets to their own layouts so they can show up how I want it to
        self.layout_for_bottom_cards.addWidget(self.card1_bottom)
        self.layout_for_bottom_cards.addWidget(self.card2_bottom)
        self.layout_for_bottom_cards.addWidget(self.card3_bottom)
#creating a QLabel and Layout for Card1_top's content inside
        self.layout_for_card1_contents= QVBoxLayout()
        self.card1_top.setLayout(self.layout_for_card1_contents)
        self.layout_for_card1_contents.setContentsMargins(20,0,0,30)
        self.welcome_txt= QLabel()
        self.welcome_txt.setObjectName("welcome_txt")
        self.welcome_txt.setText("Welcome Back,Bandit")

        self.welcome_txt_description1=QLabel()
        self.welcome_txt_description1.setObjectName("welcome_txt_description1")
        self.welcome_txt_description1.setText("Your Home Base for Bandit OS")

        self.welcome_txt_description2=QLabel()
        self.welcome_txt_description2.setObjectName("welcome_txt_description2")
        self.welcome_txt_description2.setText("Click Open to Continue")

        self.open_button = QPushButton("Open →")
        self.open_button.setObjectName("open_button")
        self.open_button.setFixedWidth(100)
        #adding all the contents to the layout I created for it
        self.layout_for_card1_contents.addWidget(self.welcome_txt)
        self.layout_for_card1_contents.addWidget(self.welcome_txt_description1)
        self.layout_for_card1_contents.addWidget(self.welcome_txt_description2)
        self.layout_for_card1_contents.addWidget(self.open_button)
#creating a layout and the first card at the bottoms contents
        self.layout_for_card1_bottom_contents= QVBoxLayout()
        self.card1_bottom.setLayout(self.layout_for_card1_bottom_contents)
        self.layout_for_card1_bottom_contents.setContentsMargins(25,55,25,40)

        self.txt1_for_card1_bottom=QLabel("Review")
        self.txt1_for_card1_bottom.setObjectName("txt1_for_card1_bottom")

        self.txt2_for_card1_bottom=QLabel("Coding Projects")
        self.txt2_for_card1_bottom.setObjectName("txt2_for_card1_bottom")

        self.coding_projects_open_projects_button= QPushButton("Open Projects →")
        self.coding_projects_open_projects_button.setObjectName("coding_projects_open_button")

        #adding contents to layout and controlling the spacing between it
        self.layout_for_card1_bottom_contents.addWidget(self.txt1_for_card1_bottom)
        self.layout_for_card1_bottom_contents.addSpacing(10)
        self.layout_for_card1_bottom_contents.addWidget(self.txt2_for_card1_bottom)
        self.layout_for_card1_bottom_contents.addStretch(1)
        self.layout_for_card1_bottom_contents.addWidget(self.coding_projects_open_projects_button)
    # creating the layout and contents for bottom card 2
        self.layout_for_card2_bottom_contents= QVBoxLayout()
        self.card2_bottom.setLayout(self.layout_for_card2_bottom_contents)
        self.layout_for_card2_bottom_contents.setContentsMargins(25,55,25,40)

        self.txt1_for_card2_bottom=QLabel("Prep")
        self.txt1_for_card2_bottom.setObjectName("txt1_for_card2_bottom")
        self.txt2_for_card2_bottom=QLabel("IT")
        self.txt2_for_card2_bottom.setObjectName("txt2_for_card2_bottom")

        self.card2_bottom_open_button= QPushButton("Open Study →")

        self.layout_for_card2_bottom_contents.addWidget(self.txt1_for_card2_bottom)
        self.layout_for_card2_bottom_contents.addSpacing(11)
        self.layout_for_card2_bottom_contents.addWidget(self.txt2_for_card2_bottom)
        self.layout_for_card2_bottom_contents.addStretch()
        self.layout_for_card2_bottom_contents.addWidget(self.card2_bottom_open_button)
# creating the layout and contents for bottom card 3
        self.layout_for_card3_bottom_contents=QVBoxLayout()
        self.card3_bottom.setLayout(self.layout_for_card3_bottom_contents)
        self.layout_for_card3_bottom_contents.setContentsMargins(25,25,25,40)

        self.txt1_for_card3_bottom=QLabel("Learn")
        self.txt1_for_card3_bottom.setObjectName("txt1_for_card3_bottom")
        self.txt2_for_card3_bottom=QLabel("Guitar Practice")
        self.txt2_for_card3_bottom.setObjectName("txt2_for_card3_bottom")

        self.card3_button=QPushButton("Open Work →")
        self.card3_button.setObjectName("card3_button")

        self.layout_for_card3_bottom_contents.addWidget(self.txt1_for_card3_bottom)
        self.layout_for_card3_bottom_contents.addSpacing(10)
        self.layout_for_card3_bottom_contents.addWidget(self.txt2_for_card3_bottom)
        self.layout_for_card3_bottom_contents.addStretch()
        self.layout_for_card3_bottom_contents.addWidget(self.card3_button)




