import wave
import struct
from audio_constants import *
from wave_class import *
import os


def generate_note(steps_duration, name, wave_type):
    """
    Calculates and resolves everything needed to create any wave(s).
    :param steps_duration:  list of tuples, hold steps and durations of note(s)
    :param name:            string, the name the saved wave will be called
    :param wave_type:       string, determines the type of wave
    :return:                nil
    """
    total_duration = 0
    for i in range(len(steps_duration)):
        total_duration += steps_duration[i][1]
        # find the total duration of all notes being recorded in this sample
    total_duration = int(total_duration/4)
    # reduces the total duration by factor 4, to speed up the melody.
    sample_length = total_duration * SAMPLE_RATE

    with wave.open(name, mode='w') as note:
        note.setparams((CHANNELS, BYTE_PER_SAMPLE, SAMPLE_RATE, sample_length,
                        "NONE", "not compressed"))
        current_index = 0  # to keep track of where it is when changing freq's
        length = 0  # to keep track of how many samples to do on this freq
        samples = []  # to hold the samples for packing later
        for i in range(len(steps_duration)):  # for every note in this sample
            tally = (steps_duration[i][1] * SAMPLE_RATE)
            tally = int(tally/4)  # tally stores what is being added to length
            length += tally
            while current_index < length:  # for every value in this note
                steps = steps_duration[i][0]
                frequency = A3 * (SINGLE_STEP ** steps)
                if wave_type == "perfect":
                    to_pack = Waves.perfect_wave(current_index, frequency)
                elif wave_type == "square":
                    to_pack = Waves.square_wave(current_index, frequency)
                elif wave_type == "saw":
                    to_pack = Waves.saw_wave(current_index, frequency)
                samples.append(pack_value(to_pack))  # adds packed value
                current_index += 1
        note.writeframes(b''.join(samples))


def pack_value(to_pack):
    """
    Uses struct to pack the wave.
    :param to_pack:     int?, the value to be packed
    :return:            ???, the value after it has been packed
    """
    packed_value = struct.pack('h', int(to_pack))
    return packed_value
