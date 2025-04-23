import sounddevice as sd
import numpy as np
from chromatic_lib import note_dict


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

def scaleplayer(index_note, scale_selec, length):
    scale = note_dict
    option = []
    if scale_selec == 'maj':
        option = [0,2,4,5,7,9,11,12]
    elif scale_selec == 'min':
        option == [0,2,3,5,7,8,10,12]
    elif scale_selec == 'har':
        option == [0,2,3,5,7,8,11,12]
    for note in option:
        notePlayer(scale[index_note+note][0],length)
    option.sort(reverse=True)
    for note in option:
        notePlayer(scale[index_note+note][0],length)

