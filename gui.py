import sys
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QHBoxLayout)
from PySide6.QtCore import Slot, QUrl, Qt
from PySide6.QtGui import QPalette
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtGui import QKeyEvent
from sound_config import pitch_maker

#Styles for the piano keys
white_keys = 'background-color: white; color: black; border: 5px solid black; height: 1000px; width: 10px; padding: 70px; font-size: 13pt'
black_keys = 'background-color: black; color: white; border: 5px solid white; height: 500px; width: 10px; padding: 20px; font-size: 8pt'
white_pressed = 'background-color: yellow; color: black; border: 5px solid black; height: 1000px; width: 10px; padding: 70px; font-size: 13pt' #Remove pressed styles in final build
black_pressed = 'background-color: yellow; color: white; border: 5px solid white; height: 500px; width: 10px; padding: 20px; font-size: 8pt'

files = ['sound_config/my_notes/C4.wav', 'sound_config/my_notes/C#4.wav', 'sound_config/my_notes/D4.wav', 'sound_config/my_notes/D#4.wav', 'sound_config/my_notes/E4.wav', 'sound_config/my_notes/F4.wav', 'sound_config/my_notes/F#4.wav', 'sound_config/my_notes/G4.wav', 'sound_config/my_notes/G#4.wav', 'sound_config/my_notes/A4.wav', 'sound_config/my_notes/A#4.wav', 'sound_config/my_notes/B4.wav', 'sound_config/my_notes/C5.wav']

class Piano(QWidget):
    def __init__(self):
        super().__init__()
        pitch_maker.pitch_maker()

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

        self.white_button8 = QPushButton('C')
        self.white_button8.setStyleSheet(white_keys)
        layout.addWidget(self.white_button8)
        
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

        self.white_button8.pressed.connect(self.white_button8_pressed)
        self.white_button8.released.connect(self.white_button8_released)
        

        self.setLayout(layout)
        self.show()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_A:
            self.white_button1_pressed()
            self.white_button1_released()
        elif event.key() == Qt.Key.Key_W:
            self.black_button1_pressed()
            self.black_buton1_released()
        elif event.key() == Qt.Key.Key_S:
            self.white_button2_pressed()
            self.white_button2_released()
        elif event.key() == Qt.Key.Key_E:
            self.black_button2_pressed()
            self.black_button2_released()
        elif event.key() == Qt.Key.Key_D:
            self.white_button3_pressed()
            self.white_button3_released()
        elif event.key() == Qt.Key.Key_F:
            self.white_button4_pressed()
            self.white_button4_released()
        elif event.key() == Qt.Key.Key_T:
            self.black_button3_pressed()
            self.black_button3_released()
        elif event.key() == Qt.Key.Key_G:
            self.white_button5_pressed()
            self.white_button5_released()
        elif event.key() == Qt.Key.Key_Y:
            self.black_button4_pressed()
            self.black_button4_released()
        elif event.key() == Qt.Key.Key_H:
            self.white_button6_pressed()
            self.white_button6_released()
        elif event.key() == Qt.Key.Key_U:
            self.black_button5_pressed()
            self.black_button5_released()
        elif event.key() == Qt.Key.Key_J:
            self.white_button7_pressed()
            self.white_button7_released()
        elif event.key() == Qt.Key.Key_K:
            self.white_button8_pressed()
            self.white_button8_released()

    #Button press tests;
    @Slot()
    def white_button1_pressed(self):
        self.white_button1.setStyleSheet(white_pressed)
        global effect
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(files[0]))
        effect.setVolume(0.4)
        effect.play()
    @Slot()
    def white_button1_released(self):
        self.white_button1.setStyleSheet(white_keys)


    @Slot()
    def black_button1_pressed(self):
        self.black_button1.setStyleSheet(black_pressed)
        global effect2
        effect2 = QSoundEffect()
        effect2.setSource(QUrl.fromLocalFile(files[1]))
        effect2.setVolume(0.4)
        effect2.play()
    @Slot()
    def black_buton1_released(self):
        self.black_button1.setStyleSheet(black_keys)

    # White Button 2
    @Slot()
    def white_button2_pressed(self):
        self.white_button2.setStyleSheet(white_pressed)
        global effect3
        effect3 = QSoundEffect()
        effect3.setSource(QUrl.fromLocalFile(files[2]))
        effect3.setVolume(0.4)
        effect3.play()
    @Slot()
    def white_button2_released(self):
        self.white_button2.setStyleSheet(white_keys)

    # Black Button 2
    @Slot()
    def black_button2_pressed(self):
        self.black_button2.setStyleSheet(black_pressed)
        global effect4
        effect4 = QSoundEffect()
        effect4.setSource(QUrl.fromLocalFile(files[3]))
        effect4.setVolume(0.4)
        effect4.play()
    @Slot()
    def black_button2_released(self):
        self.black_button2.setStyleSheet(black_keys)

    # White Button 3
    @Slot()
    def white_button3_pressed(self):
        self.white_button3.setStyleSheet(white_pressed)
        global effect4
        effect4 = QSoundEffect()
        effect4.setSource(QUrl.fromLocalFile(files[4]))
        effect4.setVolume(0.4)
        effect4.play()
    @Slot()
    def white_button3_released(self):
        self.white_button3.setStyleSheet(white_keys)

    # White Button 4
    @Slot()
    def white_button4_pressed(self):
        self.white_button4.setStyleSheet(white_pressed)
        global effect5
        effect5 = QSoundEffect()
        effect5.setSource(QUrl.fromLocalFile(files[5]))
        effect5.setVolume(0.4)
        effect5.play()
    @Slot()
    def white_button4_released(self):
        self.white_button4.setStyleSheet(white_keys)

    # Black Button 3
    @Slot()
    def black_button3_pressed(self):
        self.black_button3.setStyleSheet(black_pressed)
        global effect6
        effect6 = QSoundEffect()
        effect6.setSource(QUrl.fromLocalFile(files[6]))
        effect6.setVolume(0.4)
        effect6.play()
    @Slot()
    def black_button3_released(self):
        self.black_button3.setStyleSheet(black_keys)

    # White Button 5
    @Slot()
    def white_button5_pressed(self):
        self.white_button5.setStyleSheet(white_pressed)
        global effect7
        effect7 = QSoundEffect()
        effect7.setSource(QUrl.fromLocalFile(files[7]))
        effect7.setVolume(0.4)
        effect7.play()
    @Slot()
    def white_button5_released(self):
        self.white_button5.setStyleSheet(white_keys)

    # Black Button 4
    @Slot()
    def black_button4_pressed(self):
        self.black_button4.setStyleSheet(black_pressed)
        global effect8
        effect8 = QSoundEffect()
        effect8.setSource(QUrl.fromLocalFile(files[8]))
        effect8.setVolume(0.4)
        effect8.play()
    @Slot()
    def black_button4_released(self):
        self.black_button4.setStyleSheet(black_keys)

    # White Button 6
    @Slot()
    def white_button6_pressed(self):
        self.white_button6.setStyleSheet(white_pressed)
        global effect9
        effect9 = QSoundEffect()
        effect9.setSource(QUrl.fromLocalFile(files[9]))
        effect9.setVolume(0.4)
        effect9.play()
    @Slot()
    def white_button6_released(self):
        self.white_button6.setStyleSheet(white_keys)

    # Black Button 5
    @Slot()
    def black_button5_pressed(self):
        self.black_button5.setStyleSheet(black_pressed)
        global effect10
        effect10 = QSoundEffect()
        effect10.setSource(QUrl.fromLocalFile(files[10]))
        effect10.setVolume(0.4)
        effect10.play()
    @Slot()
    def black_button5_released(self):
        self.black_button5.setStyleSheet(black_keys)

    # White Button 7
    @Slot()
    def white_button7_pressed(self):
        self.white_button7.setStyleSheet(white_pressed)
        global effect11
        effect11 = QSoundEffect()
        effect11.setSource(QUrl.fromLocalFile(files[11]))
        effect11.setVolume(0.4)
        effect11.play()
    @Slot()
    def white_button7_released(self):
        self.white_button7.setStyleSheet(white_keys)

    # White Button 8
    @Slot()
    def white_button8_pressed(self):
        self.white_button8.setStyleSheet(white_pressed)
        global effect12
        effect12 = QSoundEffect()
        effect12.setSource(QUrl.fromLocalFile(files[12]))
        effect12.setVolume(0.4)
        effect12.play()
    @Slot()
    def white_button8_released(self):
        self.white_button8.setStyleSheet(white_keys)

#Maybe remove these 3 lines in final build
# app = QApplication([])
# win = Piano()
# sys.exit(app.exec())
