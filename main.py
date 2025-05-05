import sys
from PySide6.QtWidgets import (QWidget, QApplication, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox)
from PySide6.QtGui import QFont
from PySide6.QtCore import Slot
# Need to import keyboard press and piano keys in order for open piano button to work as intended.

# Need to also create branch for tutorials, as well as import that for tutorials button to work.
from user_tutorials import open_window as open_tutorials
# from __feature__ import true_property

my_app = QApplication([])

# Temporary class, used as a test, will implement the actual piano portion
class PianoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Piano')
        self .resize(800,400)

        vbox = QVBoxLayout()

        self.label = QLabel('Piano Time!')
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        vbox.addWidget(self.label)
        self.setLayout(vbox)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        vbox = QVBoxLayout()
        lbl_hbox = QHBoxLayout()
        btn_hbox = QHBoxLayout()

        self.label = QLabel('Where would you like to go to?')
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        lbl_hbox.addStretch(1)
        lbl_hbox.addWidget(self.label)
        lbl_hbox.addStretch(1)

        pianoBtn = QPushButton('Open Piano')
        tutorialBtn = QPushButton('Open Tutorials')
        btn_hbox.addStretch(1)
        btn_hbox.addWidget(pianoBtn)
        btn_hbox.addWidget(tutorialBtn)
        btn_hbox.addStretch(1)

        pianoBtn.clicked.connect(self.onPianoWindow)
        tutorialBtn.clicked.connect(self.onTutorialWindow)

        vbox.addLayout(lbl_hbox)
        vbox.addLayout(btn_hbox)

        self.setLayout(vbox)
        self.resize(800, 400)

        self.tutorial_window = None
        self.piano_window = None

    @Slot()
    def onPianoWindow(self):
        self.label.setText("Piano")
        self.openPianoWindow()

    def openPianoWindow(self):
        if self.piano_window is None:
            self.piano_window = PianoWindow()
            self.piano_window.show()
        else:
            self.piano_window.raise_()
            self.piano_window.activateWindow()

    @Slot()
    def onTutorialWindow(self):
        self.label.setText("Tutorials")
        self.openTutorialWindow()
    
    def openTutorialWindow(self):
        open_tutorials()

main_window = MainWindow()
main_window.show()

sys.exit(my_app.exec())