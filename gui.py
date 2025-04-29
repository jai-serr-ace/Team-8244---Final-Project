import sys
import random
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout)
from PySide6.QtCore import Slot
from PySide6.QtGui import QPalette
# from __feature__ import snake_case, true_property

white_keys = 'background-color: white; color: black; border: 5px solid black; height: 1000px; width: 10px; padding: 95px'
black_keys = 'background-color: black; color: white; border: 5px solid white; height: 500px; width: 10px; padding: 20px'

class GUI(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setSpacing(0)

        self.white_button1 = QPushButton('C')
        self.white_button1.setStyleSheet(white_keys)
        layout.addWidget(self.white_button1)

        self.black_button1 = QPushButton()
        self.black_button1.setStyleSheet(black_keys)
        layout.addWidget(self.black_button1)

        self.white_button2 = QPushButton('D')
        self.white_button2.setStyleSheet(white_keys)
        layout.addWidget(self.white_button2)

        self.black_button2 = QPushButton()
        self.black_button2.setStyleSheet(black_keys)
        layout.addWidget(self.black_button2)

        self.white_button3 = QPushButton('E')
        self.white_button3.setStyleSheet(white_keys)
        layout.addWidget(self.white_button3)

        self.white_button4 = QPushButton('G')
        self.white_button4.setStyleSheet(white_keys)
        layout.addWidget(self.white_button4)

        self.black_button3 = QPushButton()
        self.black_button3.setStyleSheet(black_keys)
        layout.addWidget(self.black_button3)

        self.white_button5 = QPushButton('A')
        self.white_button5.setStyleSheet(white_keys)
        layout.addWidget(self.white_button5)

        self.black_button4 = QPushButton()
        self.black_button4.setStyleSheet(black_keys)
        layout.addWidget(self.black_button4)

        self.white_button6 = QPushButton('B')
        self.white_button6.setStyleSheet(white_keys)
        layout.addWidget(self.white_button6)

        self.black_button5 = QPushButton()
        self.black_button5.setStyleSheet(black_keys)
        layout.addWidget(self.black_button5)

        self.white_button7 = QPushButton('C')
        self.white_button7.setStyleSheet(white_keys)
        layout.addWidget(self.white_button7)
        

        self.setLayout(layout)
        self.show()

app = QApplication([])
win = GUI()
sys.exit(app.exec())