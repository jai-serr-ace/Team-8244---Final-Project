# Course: CST205 - Multimedia Design & Programming 
# Title: Main Project File
# Authors: Leonardo Lopez / Douglas McDonald
# Date: 5/14/2025
# Description: Main, this creates the main window that greets the user and prompts them with two
# buttons, 'tutorial button' opens user tutorials window, 'piano button' opens the actual Piano gui
import sys
from PySide6.QtWidgets import (QWidget, QApplication, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox)
from PySide6.QtGui import QFont
from PySide6.QtCore import Slot
# Need to import keyboard press and piano keys in order for open piano button to work as intended.
from gui import Piano
# Need to also create branch for tutorials, as well as import that for tutorials button to work.
from user_tutorials import open_window as open_tutorials
# from __feature__ import true_property

my_app = QApplication([])

# Temporary class, used as a test, will implement the actual piano portion / Should've deleted this oops.
class PianoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Piano')
        self.resize(800,400)

        vbox = QVBoxLayout()

        self.label = QLabel('Piano Time!')
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        vbox.addWidget(self.label)
        self.setLayout(vbox)

# This is the actual main window, nothing too fancy just a vbox layout
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        vbox = QVBoxLayout()
        lbl_hbox = QHBoxLayout()
        btn_hbox = QHBoxLayout()

        self.label = QLabel('Where would you like to go to?')
        # Found out about QFont, allows for adjustable font size
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        lbl_hbox.addStretch(1)
        lbl_hbox.addWidget(self.label)
        lbl_hbox.addStretch(1)
        # Creating the button that will lead to the actual Piano
        pianoBtn = QPushButton('Open Piano')
        tutorialBtn = QPushButton('Open Tutorials')
        btn_hbox.addStretch(1) # adds like a bunch of space to so that I can center the button. 
        btn_hbox.addWidget(pianoBtn)
        btn_hbox.addWidget(tutorialBtn)
        btn_hbox.addStretch(1)

        # Connecting the buttons with their respective functions
        pianoBtn.clicked.connect(self.onPianoWindow)
        tutorialBtn.clicked.connect(self.onTutorialWindow)

        # Add the layouts
        vbox.addLayout(lbl_hbox)
        vbox.addLayout(btn_hbox)

        self.setLayout(vbox)
        self.resize(800, 400)

        self.tutorial_window = None
        self.piano_window = None

    @Slot() # when button is clicked do the openPianoWindow func
    def onPianoWindow(self):
        self.label.setText("Piano")
        self.openPianoWindow()

    # Connected the piano gui with this function so it'll you know, work. This also keeps the window open
    # cuz otherwise the window opens and closes immediately
    def openPianoWindow(self):
        if self.piano_window is None:
            self.piano_window = Piano()
            self.piano_window.show()
        else:
            self.piano_window.raise_()
            self.piano_window.activateWindow()

    # Same thing here except with tutorials window, which will be for users
    @Slot()
    def onTutorialWindow(self):
        self.label.setText("Tutorials")
        self.openTutorialWindow()
    
    def openTutorialWindow(self):
        open_tutorials()

# you know the usual execute code / run 
main_window = MainWindow()
main_window.show()

sys.exit(my_app.exec())