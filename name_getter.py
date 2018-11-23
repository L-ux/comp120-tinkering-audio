def get_name(steps):
    """
    Gets a number of steps away from a specific note, and from that calculates
    this notes name.
    :param steps:   number of steps away from A3
    :return:        the name of the note
    """
    note_dictionary = {0: 'A', 1: 'A#', 2: 'B', 3: 'C', 4: 'C#', 5: 'D',
                       6: 'D#', 7: 'E', 8: 'F', 9: 'F#', 10: 'G', 11: 'G#'}
    # dictionary of how many steps correlate to what note

    octave_changes = 0
    while not (0 <= steps <= 11):
        # changes the octaves until its within a specific workable octave
        if steps < 0:
            steps += 12
            octave_changes -= 1
        elif steps > 11:
            steps -= 12
            octave_changes += 1
    if steps == 0 or steps == 1 or steps == 2:  # just here to correct names
        octave_changes -= 1
    name = "{note}{octave}.wav".format(note = note_dictionary[steps],
                                       octave = 4 + octave_changes)
    return name

def frequency_getter(file_name):
    """
    Calculates steps away from A on the same octave, then finds how many steps
    away from A3 a note is, based on a file name/ name of note
    :param file_name:   name of the note
    :return:            the number of steps away from A3
    """
    wave = file_name.split('.')
    wave = wave[0]  # takes off the .wav extension
    if len(wave) == 3:  # trims the note accordingly
        note = wave[:2]
        octave = int(wave[2:])
    else:
        note = wave[:1]
        octave = int(wave[1:])

    step_dict = {"A": 0, "A#": 1, "B": 2, "C": -9, "C#": -8, "D": -7, "D#": -6,
            "E": -5, "F": -4, "F#": -3, "G": -2, "G#": -1}
    # dictionary holding the number of steps away from A
    #  on each octave, dependant on note
    steps = (octave - 3) * 12   # calculates number of octaves away from 3
    steps += step_dict[note]  # calculates the numbers of steps away from A3

    return steps
