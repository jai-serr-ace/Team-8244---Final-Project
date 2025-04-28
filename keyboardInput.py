import sys
from PySide6.QtWidgets import (QWidget, QApplication, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox)
from PySide6.QtCore import Slot, QObject, Qt, QUrl
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtGui import QKeyEvent
import numpy as np
# import sounddevice as sd
# from playsound import playsound

# keys = [Qt.Key.Key_A, Qt.Key.Key_W, Qt.Key.Key_S, Qt.Key.Key_E, Qt.Key.Key_D, Qt.Key.Key_F, Qt.Key.Key_T, Qt.Key.Key_G, Qt.Key.Key_Y, Qt.Key.Key_H, Qt.Key.Key_U, Qt.Key.Key_J]
nums = [65, 87, 83, 69, 68, 70, 84, 71, 89, 72, 85, 74]
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
    sd.wait()



class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.windowTitle = 'Final Project GUI Test'
        hbox = QHBoxLayout()
        self.setLayout(hbox)
    def keyPressEvent(self, event: QKeyEvent):
        print(event.key())
        if event.key() == Qt.Key.Key_A:
            # notePlayer(440, 2)
            global effect
            effect = QSoundEffect()
            effect.setSource(QUrl.fromLocalFile("testAudios/a4.wav"))
            effect.setVolume(2)
            effect.play()
        elif event.key() == Qt.Key.Key_D:
            # notePlayer(830.61, 2)
            global effect2
            effect2 = QSoundEffect()
            effect2.setSource(QUrl.fromLocalFile("testAudios/e5.wav"))
            effect.setVolume(2)
            effect2.play()
        elif event.key() == Qt.Key.Key_S:
            # notePlayer(554.37, 2)
            global effect3
            effect3 = QSoundEffect()
            effect3.setSource(QUrl.fromLocalFile("testAudios/c#.wav"))
            effect.setVolume(2)
            effect3.play()
        elif event.key() == Qt.Key.Key_F:
            # notePlayer(659.255, 2)
            global effect4
            effect4 = QSoundEffect()
            effect4.setSource(QUrl.fromLocalFile("testAudios/ab.wav"))
            effect.setVolume(2)
            effect4.play()

my_app = QApplication([])
app = GUI()
app.show()
sys.exit(my_app.exec())