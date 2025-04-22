def frequency_to_note_table(frequencies):

  notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", ]
  note_table = []

  for freq in frequencies:
    # Calculate the number of semitones from A4 (440 Hz)
    semitones = 12 * (math.log2(freq / 440))
    semitones = round(semitones)  # Round to the nearest semitone

    # Calculate the note and octave
    note_index = (semitones % 12)
    octave = 4 + (semitones // 12)
    octave += 1

    note = notes[note_index]
    if notes[note_index] == "A" or notes[note_index] == "A#" or notes[note_index] == "B":
       octave -= 1
    note_table.append([freq, note, octave])

  return note_table

import math

def remove_duplicates_ordered(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def chromatic_geneator():
  base_notes = [27.50,29.14,30.87,32.70,34.65,36.71,38.89,41.20,43.65,46.25,49.00,51.91]
  chromatic_list = []
  for note in base_notes:
    for octave in range(8):
      frequency = note * (2 ** octave)
      chromatic_list.append(frequency)
  chromatic_list.sort()
  remove_duplicates_ordered(chromatic_list)
  del chromatic_list[88:96]
  return chromatic_list

frequencies = chromatic_geneator()

note_dict = frequency_to_note_table(frequencies)
