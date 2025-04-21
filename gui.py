import sys
from PySide6.QtWidgets import (QWidget, QApplication, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox)
from PySide6.QtCore import Slot, QObject
from PySide6.QtGui import QKeyEvent
from __feature__ import snake_case, true_property

my_app = QApplication([])


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.window_title = 'Final Project GUI Test'
        hbox = QHBoxLayout()
        my_btn1 = QPushButton('A')
        my_btn2 = QPushButton('B')
        my_btn3 = QPushButton('C')
        my_btn4 = QPushButton('D')
        my_btn5 = QPushButton('E')
        my_btn6 = QPushButton('F')
        my_btn7 = QPushButton('G')
        my_btn8 = QPushButton('A')
        hbox.add_widget(my_btn1)
        hbox.add_widget(my_btn2)
        hbox.add_widget(my_btn3)
        hbox.add_widget(my_btn4)
        hbox.add_widget(my_btn5)
        hbox.add_widget(my_btn6)
        hbox.add_widget(my_btn7)
        hbox.add_widget(my_btn8)
        self.set_layout(hbox)
    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        print(f"Found key {key}!")


app = GUI()
app.show()

sys.exit(my_app.exec())
