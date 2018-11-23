import random
import re


def letter_checker(chosen_sample, search_start, search_end):
    """ Checks letters to see if they are part of the same note"""
    regex_strings = "[a-zA-Z]{1}"
    count = search_start + 1
    while count <= search_end:
        if re.match(regex_strings, chosen_sample[count]) is not None:
            return False  # returns false if it finds a letter
        count += 1
    return True # returns true if scanned characters are part of the same note


def note_name_getter(notes):
    """
    Takes in a a set of notes and creates the appropriate filename for it.
    :param notes:
    :return:
    """
    lengths = []  # stores the length of each note string.
    for a_note in range(len(notes)):
        lengths.append(len(notes[a_note]))
    lengths[len(lengths) - 1] -= 1  # removes a simole error that occurs when
                                    # reading from txt files in this way
    file_name_dur_list = []  # file name and duration list
    for i in range(len(lengths)):   # splits the name and duration accordingly
        if lengths[i] == 3:
            note_name = "{}{}4.wav".format(notes[i][0], notes[i][1])
            note_len = int(notes[i][2])
        elif lengths[i] == 2:
            if notes[i][1] == "#":
                note_name = "{}{}4.wav".format(notes[i][0], notes[i][1])
                note_len = 1
            else:
                note_name = notes[i][0]+"4.wav"
                note_len = int(notes[i][1])
        else:
            note_name = notes[i][0]+"4.wav"
            note_len = 1
        notes_tuple = (note_name, note_len)  # stores name and length together
        file_name_dur_list.append(notes_tuple)  # adds notes_tuple to list
    return file_name_dur_list  # returns the list full of names and durations


def random_melody_getter():
    """
    Chooses a random melody from a .txt file and processes it for use.
    :return:   returns filenames and note durations of each note for the melody
    """
    with open("melodies.txt") as file:  # the text file used to store melodies
        sample_list = []
        for a_sample in file:  # adds every line of file to sample_list
            sample_list.append(a_sample)

    the_sample = random.choice(sample_list)  # choose a random melody
    notes = []
    marker = 0
    while marker < len(the_sample):
        # split the block melody into a list of individual notes
        finished = False  # a boolean to store whether a note has been done yet
        if marker + 2 < len(the_sample):  # if marker+2 isn't out of range
            finished = letter_checker(the_sample, marker, marker + 2)
            if finished:
                value = ("{}{}{}".format(the_sample[marker],
                                         the_sample[marker + 1],
                                         the_sample[marker + 2]))
                notes.append(value)
                marker += 3

        if marker + 1 < len(the_sample) and not finished:
            finished = letter_checker(the_sample, marker, marker + 1)
            if finished:
                value = ("{}{}".format(the_sample[marker],
                                       the_sample[marker + 1]))
                notes.append(value)
                marker += 2

        if not finished:
            value = (the_sample[marker])
            notes.append(value)
            marker += 1

    file_name_dur_list = note_name_getter(notes)
    # sends the list of individual notes to another function,
    # where they are split into specific filenames and durations
    return file_name_dur_list
