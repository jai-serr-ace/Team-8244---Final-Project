import sys
from PySide6.QtWidgets import (QWidget, QApplication, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox)
from PySide6.QtCore import Slot, QObject, Qt
from PySide6.QtGui import QKeyEvent
from __feature__ import snake_case

# my_app = QApplication([])


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.window_title = 'Final Project GUI Test'
        hbox = QHBoxLayout(self)
        self.label = QLabel('Hi')
        hbox.add_widget(self.label)
        self.set_layout(hbox)
    # def keyPressEvent(self, event: QKeyEvent):
    #     if event.key() == Qt.Key.Key_A:
    #         self.label.setText("A was pressed")
    #     elif event.key() == Qt.Key.Key_B:
    #         self.label.setText("B was pressed")
    #     elif event.key() == Qt.Key.Key_Escape:
    #         self.close()
    #     else:
    #         self.label.setText("Some other key was pressed")

# app = GUI()
# app.show()
# sys.exit(my_app.exec())



#Online Example (Working)
# from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# from PySide6.QtGui import QKeyEvent
# from PySide6.QtCore import Qt

# class MyWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.label = QLabel("Press a key")
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.label)
#         self.setLayout(layout)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_A:
            self.label.setText("A was pressed")
        elif event.key() == Qt.Key.Key_B:
            self.label.setText("B was pressed")
        elif event.key() == Qt.Key.Key_Escape:
            self.close()
        else:
            self.label.setText("Some other key was pressed")

if __name__ == "__main__":
    app = QApplication([])
    widget = GUI()
    widget.show()
    app.exec()