import sys
from PySide6.QtWidgets import (QWidget, QApplication, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox)
from PySide6.QtCore import Slot, QObject, Qt, QUrl
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtGui import QKeyEvent
import numpy as np
import sounddevice as sd
from playsound import playsound



def generate_sine_wave(frequency, duration, sample_rate):
    """Generates a sine wave at a given frequency for a specified duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    amplitude = 50 * np.sin(2 * np.pi * frequency * t)
    #the 2 on amplitude shifts the pitch; so dont move. The 5 value changes the strength of the
    #wave of the note, and as it right now it sounds like 8-bit
    return amplitude

def notePlayer(my_note, length):
    duration_seconds = length
    sample_rate = 48000
    sine_wave = generate_sine_wave(my_note, duration_seconds, sample_rate)
    sd.play(sine_wave, sample_rate)
    sd.save()
    sd.wait()



class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.windowTitle = 'Final Project GUI Test'
        hbox = QHBoxLayout()
        my_btn1 = QPushButton('A')
        my_btn2 = QPushButton('B')
        my_btn3 = QPushButton('C')
        my_btn4 = QPushButton('D')
        my_btn5 = QPushButton('E')
        my_btn6 = QPushButton('F')
        my_btn7 = QPushButton('G')
        my_btn8 = QPushButton('A')
        hbox.addWidget(my_btn1)
        hbox.addWidget(my_btn2)
        hbox.addWidget(my_btn3)
        hbox.addWidget(my_btn4)
        hbox.addWidget(my_btn5)
        hbox.addWidget(my_btn6)
        hbox.addWidget(my_btn7)
        hbox.addWidget(my_btn8)
        self.setLayout(hbox)
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_A:
            # notePlayer(440, 2)
            global effect
            effect = QSoundEffect()
            effect.setSource(QUrl.fromLocalFile("C:/Users/dougi/cst205/Team-8244---Final-Project/testAudios/a4.wav"))
            # effect.setVolume(2)
            effect.play()
        if event.key() == Qt.Key.Key_D:
            # notePlayer(830.61, 2)
            global effect2
            effect2 = QSoundEffect()
            effect2.setSource(QUrl.fromLocalFile("C:/Users/dougi/cst205/Team-8244---Final-Project/testAudios/e5.wav"))
            # effect.setVolume(2)
            effect2.play()
        if event.key() == Qt.Key.Key_S:
            # notePlayer(554.37, 2)
            global effect3
            effect3 = QSoundEffect()
            effect3.setSource(QUrl.fromLocalFile("C:/Users/dougi/cst205/Team-8244---Final-Project/testAudios/c#.wav"))
            # effect.setVolume(2)
            effect3.play()
        if event.key() == Qt.Key.Key_F:
            # notePlayer(659.255, 2)
            global effect4
            effect4 = QSoundEffect()
            effect4.setSource(QUrl.fromLocalFile("C:/Users/dougi/cst205/Team-8244---Final-Project/testAudios/ab.wav"))
            # effect.setVolume(2)
            effect4.play()

my_app = QApplication([])
app = GUI()
app.show()
sys.exit(my_app.exec())