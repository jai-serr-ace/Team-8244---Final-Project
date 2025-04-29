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

        black_button1 = QPushButton()
        black_button1.setStyleSheet(black_keys)
        black_button1.move(150, 50)
        layout.addWidget(black_button1)

        white_button2 = QPushButton('D')
        white_button2.setStyleSheet(white_keys)
        layout.addWidget(white_button2)

        black_button2 = QPushButton()
        black_button2.setStyleSheet(black_keys)
        layout.addWidget(black_button2)

        white_button3 = QPushButton('E')
        white_button3.setStyleSheet(white_keys)
        layout.addWidget(white_button3)

        white_button4 = QPushButton('G')
        white_button4.setStyleSheet(white_keys)
        layout.addWidget(white_button4)

        black_button3 = QPushButton()
        black_button3.setStyleSheet(black_keys)
        layout.addWidget(black_button3)

        white_button5 = QPushButton('A')
        white_button5.setStyleSheet(white_keys)
        layout.addWidget(white_button5)

        black_button4 = QPushButton()
        black_button4.setStyleSheet(black_keys)
        layout.addWidget(black_button4)

        white_button6 = QPushButton('B')
        white_button6.setStyleSheet(white_keys)
        layout.addWidget(white_button6)

        black_button5 = QPushButton()
        black_button5.setStyleSheet(black_keys)
        layout.addWidget(black_button5)

        white_button7 = QPushButton('C')
        white_button7.setStyleSheet(white_keys)
        layout.addWidget(white_button7)
        
        self.

        self.setLayout(layout)
        self.show()

app = QApplication([])
win = GUI()
sys.exit(app.exec())