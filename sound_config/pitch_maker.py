from pydub import AudioSegment
import numpy as np
import os
""" Author: Jaime
    Team: 8244
    Course: CST 205
    Summary: Overall, this code takes a .wav file and makes a chromatic scale out of it"""


#This a chromatic scale that holds the string of the musical notes
chromatic_scale = ["C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4","A#4","B4","C5"]

def change_pitch(input_file, output_file, semitones):
    """Changes the pitch of an audio file using sample rate manipulation (changes duration)"""
    try:
        audio = AudioSegment.from_wav(input_file) #The audio sample for the manipulation
        new_sample_rate = int(audio.frame_rate * (2 ** (semitones / 12.0))) #Calculates the value of the semitone that
        #will be required for shift in pitch, using 12 notes equal temperat
        """As in if the audio has pitch of C4, semintone = 0 will keep to C4, but semitone = -1 will create B3
        and if you use 14 that will create D6"""
        new_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate}) #It creates the modified object
        new_audio.export(output_file, format='wav') #Saves the object into a wav audio file
        print(f"Pitch-changed audio saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

def semitoneMaker(note_name, semitone, path):
    input_wav = "C4.wav"  #File chose for modification
    output_wav = f"{path}/{note_name}.wav" #The path and name for the new wav file
    semitones_to_shift = semitone #Chose the semiton
    change_pitch(input_wav, output_wav, semitones_to_shift)


def pitch_maker():
    folder_name = "my_notes" #path for saving the files
    """The next part is a bool, checks if the files have being created before or already exits. If yes, it moves own and display what is done;
    else it recreates the files. For this instance is very important to have C4.wav file (and next to the pitchmaker.py file) in order
    otherwise the code will. Additional we you cant change the C4.wav file for another wav and have different sounds for the rest of the prohect"""
    existing_files = [f for f in chromatic_scale if os.path.exists(f"{folder_name}/{f}.wav")]
    if len(existing_files) ==  len(chromatic_scale):
        print("Files already exists!") 
    else:
        folder_name = "my_notes"
        os.makedirs(folder_name, exist_ok=True) #Creates the folder were the sounds will be created, if the folder exits, it just overides it
        ind = 0 #this is counter that keeps track of the semitone
        for note in chromatic_scale:
            semitoneMaker(note, ind, folder_name)
            ind += 1
            if ind == 13:
                print("Files created succesfully!")
                #This loop overall creates the chromatic scale by using the initial list and assign it the value to the wave file being created
