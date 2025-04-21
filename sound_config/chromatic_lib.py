def frequency_to_note_table(frequencies):
  """Converts a list of frequencies to a 2D list of [frequency, note, octave].

  Args:
    frequencies: A list of frequencies (in Hz).

  Returns:
    A 2D list where each sublist is [frequency, note, octave].
  """

  notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
  note_table = []

  for freq in frequencies:
    # Calculate the number of semitones from A4 (440 Hz)
    semitones = 12 * (math.log2(freq / 440))
    semitones = round(semitones)  # Round to the nearest semitone

    # Calculate the note and octave
    note_index = (semitones % 12)
    octave = 4 + (semitones // 12)

    note = notes[note_index]
    note_table.append([freq, note, octave])

  return note_table

import math

frequencies = [82.41, 87.31, 92.5, 98.0, 103.83, 110.0, 116.54, 123.47, 130.81, 138.59, 146.83, 155.56, 164.82, 174.62, 185.0, 196.0, 207.66, 220.0, 233.08, 246.94, 261.62, 277.18, 293.66, 311.12, 329.64, 349.24, 370.0, 392.0, 415.32, 440.0, 466.16, 493.88, 523.24, 554.36, 587.32, 622.24, 659.28, 698.48, 740.0, 784.0, 830.64, 880.0, 932.32, 987.76, 1046.48, 1108.72, 1174.64, 1244.48, 1318.56, 1396.96, 1480.0, 1568.0, 1661.28, 1760.0, 1864.64, 1975.52, 2092.96, 2217.44, 2349.28, 2488.96, 2637.12, 2793.92, 2960.0, 3136.0, 3322.56, 3520.0, 3729.28, 3951.04, 4185.92, 4434.88, 4698.56, 4977.92]

note_dict = frequency_to_note_table(frequencies)