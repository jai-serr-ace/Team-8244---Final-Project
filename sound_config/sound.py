import sounddevice as sd
import numpy as np
from chromatic_lib import note_dict

def generate_sine_wave(frequency, duration, sample_rate=44100):
    """Generates a sine wave at a given frequency for a specified duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    amplitude = 0.5 * np.sin(2 * np.pi * frequency * t)
    return amplitude

def notePlayer(my_note, length):
    duration_seconds = length
    sample_rate = 48000
    sine_wave = generate_sine_wave(my_note, duration_seconds, sample_rate)
    sd.play(sine_wave, sample_rate)
    sd.wait()


def scaleplayer(index_note):
    scale = note_dict
    major_scale_step = [0,2,4,5,7,9,11,12]
    minor_scale_step = [0,2,3,5,7,8,10,12]
    harmonic_minor_scale_step = [0,2,3,5,7,8,11,12]
    for note in harmonic_minor_scale_step:
        notePlayer(scale[index_note+note][0],1)
    harmonic_minor_scale_step.sort(reverse=True)
    for note in harmonic_minor_scale_step:
        notePlayer(scale[index_note+note][0],1)



