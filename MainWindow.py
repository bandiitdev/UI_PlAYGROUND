
from settings import Settings_Page
from sidebar import Sidebar
from dashboard import Dashboard
from open_button_for_dashboard_top_card import Open_Button
from coding_projects_page import Coding_Projects_Page
from IT_Page import IT_Window
from guitar_page import Guitar_study

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QStackedWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        self.resize(1400, 800)
        self.setWindowTitle("UI_Practice")

        self.sidebar = Sidebar()
        self.layout.addWidget(self.sidebar, 0, Qt.AlignmentFlag.AlignLeft )
        self.sidebar.setMinimumWidth(150)
        self.sidebar.setMaximumWidth(200)
        self.sidebar.show()


        #setup Qstackedwidget onto my layout to allow page switching and added it onto my layout(set current widget allows dashboard to be the defaults page shown when opening app)
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        self.settings_page=Settings_Page()
        self.stacked_widget.addWidget(self.settings_page)

        self.dashboard_page=Dashboard()
        self.stacked_widget.addWidget(self.dashboard_page)
        self.stacked_widget.setCurrentWidget(self.dashboard_page)

        self.open_button=Open_Button()
        self.stacked_widget.addWidget(self.open_button)

        self.coding_projects_page=Coding_Projects_Page()
        self.stacked_widget.addWidget(self.coding_projects_page)

        self.IT_Page=IT_Window()
        self.stacked_widget.addWidget(self.IT_Page)

        self.Guitar_page=Guitar_study()
        self.stacked_widget.addWidget(self.Guitar_page)

        self.sidebar.settings.clicked.connect(self.open_settings)
        self.sidebar.dashboard.clicked.connect(self.dashboard)
        self.dashboard_page.open_button.clicked.connect(self.open_button_page)
        self.dashboard_page.coding_projects_open_projects_button.clicked.connect(self.open_coding_projects_page)
        self.dashboard_page.card2_bottom_open_button.clicked.connect(self.open_it_window)
        self.dashboard_page.card3_button.clicked.connect(self.open_guitar_page)




    def open_settings(self):
        self.stacked_widget.setCurrentWidget(self.settings_page)


    def dashboard(self):
        self.stacked_widget.setCurrentWidget(self.dashboard_page)

    def open_button_page(self):
        self.stacked_widget.setCurrentWidget(self.open_button)

    def open_coding_projects_page(self):
        self.stacked_widget.setCurrentWidget(self.coding_projects_page)

    def open_it_window(self):
        self.stacked_widget.setCurrentWidget(self.IT_Page)

    def open_guitar_page(self):
        self.stacked_widget.setCurrentWidget(self.Guitar_page)
















