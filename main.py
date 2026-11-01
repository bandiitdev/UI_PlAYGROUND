import sys
from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication

app=QApplication(sys.argv)
with open("style.qss", "r") as file:
    contents = file.read()
app.setStyleSheet(contents)
w=MainWindow()
w.show()
app.exec()
