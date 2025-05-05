import sys
from PySide6.QtWidgets import (QWidget, QApplication, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox, QMainWindow, QStackedLayout)
from PySide6.QtGui import QFont
from PySide6.QtCore import Slot

class TutorialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tutorials')
        self.resize(800, 400)

        main_layout = QVBoxLayout()

        # stacked layout for pgs
        self.stacked_layout = QStackedLayout()
        self.pages = []  # stores reference to each page

        # actual tutorial pages
        self.add_page(
            "Tutorials!!",
            (
                "Welcome to the tutorials window!\n\n"
                "Here you'll learn the basics of piano and music theory concepts.\n\n"
                "Let's start off with the musical alphabet, which only contains the letters A-G, which we call notes.\n\n"
                "All of these notes have natural and flat / sharp versions.\n\n"
                "Natural meaning a basic pitch, that is unmodified by sharps / flats.\n\n"
                "Sharps refer to an accidental, altering a note's pitch by raising it a semitone (half-step).\n\n"
                "Flats also refer to an accidental, altering a note's pitch by lowering it a semitone (half-step).\n"
            )
        )
        self.add_page(
            "Keys!", 
            (
                "Piano keys are discernible through their colors and spacing.\n\n"
                "For instance, white keys are natural notes.\n\n"
                "Whereas the black keys are sharps & flats.\n\n"
                "When going up the piano, the black keys are sharp, they're flat when going down.\n\n"
                "If you notice, there is a pattern of black keys, going from 2 - break - 3.\n\n"
                "This pattern is useful as it can be used to determine where you are when playing.\n\n"
                "This pattern is also what's known as an octave, which is an interval or series of 8 notes.\n"
            )
        )
        self.add_page( # subject to chage depending on features ++ / --
            "How to Play Using Our Program!!",
            ( 
                "Our program allows for users to play whatever melody comes in their head, as well as just fiddling around.\n\n"
                "To play the white keys / natural notes players must use the keyboard keys: \n\n"
                "To play the black keys / accidental notes players must use the keyboard keys: \n\n"
                "Important to note that the user can play multiple notes, with some latency.\n\n"
                "Have fun playing piano!!!\n\n"
            )
        )

        # nav btns
        nav_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")
        nav_layout.addWidget(self.prev_button)
        nav_layout.addStretch()
        nav_layout.addWidget(self.next_button)

        # connecting
        self.prev_button.clicked.connect(self.go_previous)
        self.next_button.clicked.connect(self.go_next)

        self.prev_button.setEnabled(False) # so prev btn doesnt start on page 1

        # assembly
        main_layout.addLayout(self.stacked_layout)
        main_layout.addLayout(nav_layout)
        self.setLayout(main_layout)

    def add_page(self, title: str, content: str):
        page = QWidget()
        layout = QVBoxLayout()

        title_label = QLabel(title)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)

        content_label = QLabel(content)
        content_font = QFont()
        content_font.setPointSize(12)
        content_label.setFont(content_font)
        content_label.setWordWrap(True)

        layout.addWidget(title_label)
        layout.addWidget(content_label)
        layout.addStretch()
        page.setLayout(layout)

        self.stacked_layout.addWidget(page)
        self.pages.append(page)

    def go_next(self):
        current_index = self.stacked_layout.currentIndex()
        if current_index < len(self.pages) - 1:
            self.stacked_layout.setCurrentIndex(current_index + 1)
            self.prev_button.setEnabled(True)
        if current_index + 1 == len(self.pages) - 1:
            self.next_button.setEnabled(False)

    def go_previous(self):
        current_index = self.stacked_layout.currentIndex()
        if current_index > 0:
            self.stacked_layout.setCurrentIndex(current_index - 1)
            self.next_button.setEnabled(True)
        if current_index - 1 == 0:
            self.prev_button.setEnabled(False)

tutorial_window = None  

def open_window():
    global tutorial_window
    if tutorial_window is None:
        tutorial_window = TutorialWindow()
        tutorial_window.show()
    else:
        tutorial_window.raise_()
        tutorial_window.activateWindow()
