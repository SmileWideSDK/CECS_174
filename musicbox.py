import pygame
import time
import pygame.midi
import musicbox

notes = [("C", 60), ('D', 62), ('E',64), ('F',65), ('G',67), ('A',69), ('B',71), ('C',72)]
##List of Tuples
class MusicBox:
    def __init__(self, instrument=0):
        """Creates a new MusicBox variable. An optional parameter from 0 to 127 inclusive sets the instrument ID.
        Experiment with different IDs to play different instruments."""
        try:
            pygame.init()
            pygame.midi.init()
            id = pygame.midi.get_default_output_id()
        except e:
            id = 0
            
        if id >= 0:
            self.__player = pygame.midi.Output(id, 1)
            self.__instrument = instrument
            self.__enabled = True
        else:
            self.__enabled = False

    def close(self):
        if self.__enabled:
            self.__player.close()

    def play_note(self, note, duration):
        """Plays a single note for a given duration. The note is in integer notation."""
        print("<MusicBox: play_note({0}, {1})>".format(note, duration))
        if self.__enabled:
            self.__player.set_instrument(self.__instrument, 0)
            self.__player.note_on(note, 127, 0)
            time.sleep(duration / 1000)
            self.__player.note_off(note, 127, 0)

    def pause(self, duration):
        time.sleep(duration / 1000)

    def play_chord(self, chord, duration):
        """Plays a list of notes at the same time, for the given duration."""
        print("<MusicBox: play_chord({0}, {1})>".format(chord, duration))
        if self.__enabled:
            channel = 0
            for note in chord:
                self.__player.set_instrument(self.__instrument, channel)
                self.__player.note_on(note, 127, channel)
                channel += 1
            time.sleep(duration / 1000)
            channel = 0
            for note in chord:
                self.__player.note_off(note, 127, channel)
                channel += 1


def demo():
    # Example of how to use the MusicBox
    m = MusicBox()
    m.play_note(60, 500)
    m.play_note(63, 500)
    m.play_scale([60, 63, 67], 500)
    m.play_chord([60, 63, 67], 1000)

def get_notes():
    user_garbage = str(input("Please input your string of notes: "))

    temp = user_garbage.split()
    temp_value = 0
    note_list = []
    i = 0
    for x in temp:
        temp_value = note_to_int(temp[i])
        note_list.append(temp_value)
        i += 1
    print(note_list)
    return note_list




def note_to_int(note):
    notes_dict = dict(notes)
    temp_str = note.strip('^#b\n1234567890')
    value = 0
    result = note.rfind("^") + 1
    if temp_str in notes_dict:
        value = notes_dict[temp_str]
        value = (result * 12 ) + value
        if 'b' in note:
            value -= 1
        if '#' in note:
            value += 1
        return value
    else:
        return (-1)


def menu_play_notes():
    list = get_notes()
    if not list:
        print("I dont know any of those notes")
    else:
        play_notes(list)


def get_song_files():
    name_of_file = str(input("Please input the name of the file: "))
    return name_of_file

def print_menu():
    print("1. Play notes ")
    print("2. Play Song ")
    print("3. Quit ")

def get_menu_choice():
    choice = -1
    choice = int(input("Please make a selection: "))
    return choice

def menu_play_song():
    song = get_song_files()
    play_song(song)

def play_song(file_name):
    result = []

    first_line = True
    for line in open(file_name):
        if first_line:
            first_line = False
            continue

        split_line = line.split(",")


        result.append(str(split_line[0].strip('"')))
    print(result)
    temp_value = 0
    note_list = []
    duration = []
    for x in result:
        temp_value = note_to_int(result[i])
        note_list.append(temp_value)
        duration_temp = get_duration(result[i])
        duration.append(duration_temp)
        i += 1
    play_song_file(note_list, duration)

def get_duration(ms):
    temp = ms.strip('abcdefghijklmnopqrstuvwyxz^#b')
    return temp

def play_song_file(note, ms):
    m = musicbox.MusicBox()
    for x in note:
        m.play_note(note[x], ms[x])
        m.close()

def main():
    choice = -1
    while choice != 3:
        choice = -1
        print_menu()
        while choice < 1 or choice > 3:
            choice = get_menu_choice()
        if choice == 1:
            menu_play_notes()
        if choice == 2:
            menu_play_song()

def play_notes(notes):
    m = musicbox.MusicBox()
    for x in notes:
        m.play_note(notes[x], 500)
        m.close()


main()