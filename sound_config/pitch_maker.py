from pydub import AudioSegment
import numpy as np
import os

chromatic_scale = ["C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4","A#4","B4","C5"]
print(chromatic_scale)

def change_pitch(input_file, output_file, semitones):
    """Changes the pitch of an audio file using sample rate manipulation (changes duration)"""
    try:
        audio = AudioSegment.from_wav(input_file)
        new_sample_rate = int(audio.frame_rate * (2 ** (semitones / 12.0)))
        new_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})
        new_audio.export(output_file, format='wav')
        print(f"Pitch-changed audio saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

def semitoneMaker(note_name, semitone, path):
    input_wav = "C4.wav"  # Replace with your input WAV file
    output_wav = f"{path}/{note_name}.wav"
    semitones_to_shift = semitone # Shift up by 3 semitones
    change_pitch(input_wav, output_wav, semitones_to_shift)


def pitch_maker():
    folder_name = "my_notes" 
    existing_files = [f for f in chromatic_scale if os.path.exists(f"{folder_name}/{f}.wav")]
    if len(existing_files) ==  len(chromatic_scale):
        print("Files already exists!") #If all the files are already created
    else: #if the program needs to create the files
        folder_name = "my_notes"
        os.makedirs(folder_name, exist_ok=True) #Creates the folder were the sounds will be created
        ind = 0
        for note in chromatic_scale:
            semitoneMaker(note, ind, folder_name)
            ind += 1
            if ind == 13:
                print("Files created succesfully!")

pitch_maker()