def get_name(steps):
    """

    :param steps:
    :return:
    """
    note_dictionary = {0: 'A', 1: 'A#', 2: 'B', 3: 'C', 4: 'C#', 5: 'D',
                       6: 'D#', 7: 'E', 8: 'F', 9: 'F#', 10: 'G', 11: 'G#'}
    octave_changes = 0
    while not (0 <= steps <= 11):
        if steps < 0:
            steps += 12
            octave_changes -= 1
        elif steps > 11:
            steps -= 12
            octave_changes += 1
    if steps == 0 or steps == 1 or steps == 2:
        octave_changes -= 1
    name = "{note}{octave}.wav".format(note = note_dictionary[steps],
                                       octave = 4 + octave_changes)
    return name
