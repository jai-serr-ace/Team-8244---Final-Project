import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy)
from PySide6.QtCore import Slot
from PySide6.QtGui import QPalette
# from __feature__ import snake_case, true_property

white_keys = 'background-color: white; color: black; border: 5px solid black; height: 1000px; width 10px; margin-right: 10px; padding: 50px;'
black_keys = ''

class GUI(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setSpacing(0)

        button1 = QPushButton('C')
        button1.setStyleSheet(white_keys)
        layout.addWidget(button1)

        button2 = QPushButton('D')
        button2.setStyleSheet(white_keys)
        layout.addWidget(button2)

        button3 = QPushButton('E')
        button3.setStyleSheet(white_keys)
        layout.addWidget(button3)

        button4 = QPushButton('G')
        button4.setStyleSheet(white_keys)
        layout.addWidget(button4)

        button5 = QPushButton('A')
        button5.setStyleSheet(white_keys)
        layout.addWidget(button5)

        button6 = QPushButton('B')
        button6.setStyleSheet(white_keys)
        layout.addWidget(button6)

        button7 = QPushButton('C')
        button7.setStyleSheet(white_keys)
        layout.addWidget(button7)

        self.setLayout(layout)
        self.show()

app = QApplication([])
win = GUI()
sys.exit(app.exec())