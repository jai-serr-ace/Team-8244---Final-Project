import sys
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QHBoxLayout)
from PySide6.QtCore import Slot, QUrl, Qt
from PySide6.QtGui import QPalette
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtGui import QKeyEvent

#Styles for the piano keys
white_keys = 'background-color: white; color: black; border: 5px solid black; height: 1000px; width: 10px; padding: 70px; font-size: 13pt'
black_keys = 'background-color: black; color: white; border: 5px solid white; height: 500px; width: 10px; padding: 20px; font-size: 8pt'
white_pressed = 'background-color: yellow; color: black; border: 5px solid black; height: 1000px; width: 10px; padding: 70px; font-size: 13pt' #Remove pressed styles in final build
black_pressed = 'background-color: yellow; color: white; border: 5px solid white; height: 500px; width: 10px; padding: 20px; font-size: 8pt'

class Piano(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.white_button1 = QPushButton('C')
        self.white_button1.setStyleSheet(white_keys)
        layout.addWidget(self.white_button1)

        self.black_button1 = QPushButton('C#')
        self.black_button1.setStyleSheet(black_keys)
        layout.addWidget(self.black_button1)

        self.white_button2 = QPushButton('D')
        self.white_button2.setStyleSheet(white_keys)
        layout.addWidget(self.white_button2)

        self.black_button2 = QPushButton('D#')
        self.black_button2.setStyleSheet(black_keys)
        layout.addWidget(self.black_button2)

        self.white_button3 = QPushButton('E')
        self.white_button3.setStyleSheet(white_keys)
        layout.addWidget(self.white_button3)

        self.white_button4 = QPushButton('F')
        self.white_button4.setStyleSheet(white_keys)
        layout.addWidget(self.white_button4)

        self.black_button3 = QPushButton('F#')
        self.black_button3.setStyleSheet(black_keys)
        layout.addWidget(self.black_button3)

        self.white_button5 = QPushButton('G')
        self.white_button5.setStyleSheet(white_keys)
        layout.addWidget(self.white_button5)

        self.black_button4 = QPushButton('G#')
        self.black_button4.setStyleSheet(black_keys)
        layout.addWidget(self.black_button4)

        self.white_button6 = QPushButton('A')
        self.white_button6.setStyleSheet(white_keys)
        layout.addWidget(self.white_button6)

        self.black_button5 = QPushButton('A#')
        self.black_button5.setStyleSheet(black_keys)
        layout.addWidget(self.black_button5)

        self.white_button7 = QPushButton('B')
        self.white_button7.setStyleSheet(white_keys)
        layout.addWidget(self.white_button7)
        
        self.white_button1.pressed.connect(self.white_button1_pressed) #These are to test to see if the button presses work
        self.white_button1.released.connect(self.white_button1_released)

        self.black_button1.pressed.connect(self.black_button1_pressed)
        self.black_button1.released.connect(self.black_buton1_released)

        self.white_button2.pressed.connect(self.white_button2_pressed)
        self.white_button2.released.connect(self.white_button2_released)

        self.black_button2.pressed.connect(self.black_button2_pressed)
        self.black_button2.released.connect(self.black_button2_released)

        self.white_button3.pressed.connect(self.white_button3_pressed)
        self.white_button3.released.connect(self.white_button3_released)

        self.white_button4.pressed.connect(self.white_button4_pressed)
        self.white_button4.released.connect(self.white_button4_released)

        self.black_button3.pressed.connect(self.black_button3_pressed)
        self.black_button3.released.connect(self.black_button3_released)

        self.white_button5.pressed.connect(self.white_button5_pressed)
        self.white_button5.released.connect(self.white_button5_released)

        self.black_button4.pressed.connect(self.black_button4_pressed)
        self.black_button4.released.connect(self.black_button4_released)        

        self.white_button6.pressed.connect(self.white_button6_pressed)
        self.white_button6.released.connect(self.white_button6_released)

        self.black_button5.pressed.connect(self.black_button5_pressed)
        self.black_button5.released.connect(self.black_button5_released)

        self.white_button7.pressed.connect(self.white_button7_pressed)
        self.white_button7.released.connect(self.white_button7_released)
        

        self.setLayout(layout)
        self.show()

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
    #Button press tests;
    @Slot()
    def white_button1_pressed(self):
        self.white_button1.setStyleSheet(white_pressed)
        global effect
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile("testAudios/a4.wav"))
        effect.setVolume(2)
        effect.play()
    @Slot()
    def white_button1_released(self):
        self.white_button1.setStyleSheet(white_keys)


    @Slot()
    def black_button1_pressed(self):
        self.black_button1.setStyleSheet(black_pressed)
        global effect2
        effect2 = QSoundEffect()
        effect2.setSource(QUrl.fromLocalFile("testAudios/c#.wav"))
        effect2.setVolume(2)
        effect2.play()
    @Slot()
    def black_buton1_released(self):
        self.black_button1.setStyleSheet(black_keys)

    # White Button 2
    @Slot()
    def white_button2_pressed(self):
        self.white_button2.setStyleSheet(white_pressed)
    @Slot()
    def white_button2_released(self):
        self.white_button2.setStyleSheet(white_keys)

    # Black Button 2
    @Slot()
    def black_button2_pressed(self):
        self.black_button2.setStyleSheet(black_pressed)
    @Slot()
    def black_button2_released(self):
        self.black_button2.setStyleSheet(black_keys)

    # White Button 3
    @Slot()
    def white_button3_pressed(self):
        self.white_button3.setStyleSheet(white_pressed)
    @Slot()
    def white_button3_released(self):
        self.white_button3.setStyleSheet(white_keys)

    # White Button 4
    @Slot()
    def white_button4_pressed(self):
        self.white_button4.setStyleSheet(white_pressed)
    @Slot()
    def white_button4_released(self):
        self.white_button4.setStyleSheet(white_keys)

    # Black Button 3
    @Slot()
    def black_button3_pressed(self):
        self.black_button3.setStyleSheet(black_pressed)
    @Slot()
    def black_button3_released(self):
        self.black_button3.setStyleSheet(black_keys)

    # White Button 5
    @Slot()
    def white_button5_pressed(self):
        self.white_button5.setStyleSheet(white_pressed)
    @Slot()
    def white_button5_released(self):
        self.white_button5.setStyleSheet(white_keys)

    # Black Button 4
    @Slot()
    def black_button4_pressed(self):
        self.black_button4.setStyleSheet(black_pressed)
    @Slot()
    def black_button4_released(self):
        self.black_button4.setStyleSheet(black_keys)

    # White Button 6
    @Slot()
    def white_button6_pressed(self):
        self.white_button6.setStyleSheet(white_pressed)
    @Slot()
    def white_button6_released(self):
        self.white_button6.setStyleSheet(white_keys)

    # Black Button 5
    @Slot()
    def black_button5_pressed(self):
        self.black_button5.setStyleSheet(black_pressed)
    @Slot()
    def black_button5_released(self):
        self.black_button5.setStyleSheet(black_keys)

    # White Button 7
    @Slot()
    def white_button7_pressed(self):
        self.white_button7.setStyleSheet(white_pressed)
    @Slot()
    def white_button7_released(self):
        self.white_button7.setStyleSheet(white_keys)

#Maybe remove these 3 lines in final build
app = QApplication([])
win = Piano()
sys.exit(app.exec())
