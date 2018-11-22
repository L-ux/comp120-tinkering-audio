import wave
import struct
from audio_constants import *
from wave_class import *
import os

def generate_note(steps, duration, name, wave_type):
    # save_as = os.path.join(PATH, name)
    # with wave.open(save_as, mode = 'w') as note:
    with wave.open(name, mode = 'w') as note:
        sample_length = duration * SAMPLE_RATE
        frequency = A3 * (SINGLE_STEP ** steps)
        note.setparams((CHANNELS, BYTE_PER_SAMPLE, SAMPLE_RATE, sample_length,
                        "NONE", "not compressed"))
        samples = []
        class_holder = waves()
        if wave_type == "perfect":
            for sample in range(sample_length):
                to_pack = class_holder.perfect_wave(sample, frequency)
                samples.append(pack_value(to_pack))
        elif wave_type == "square":
            for sample in range(sample_length):
                to_pack = class_holder.square_wave(sample, frequency)
                samples.append(pack_value(to_pack))
        elif wave_type == "saw":
            for sample in range(sample_length):
                to_pack = class_holder.saw_wave(sample, frequency)
                samples.append(pack_value(to_pack))
        note.writeframes(b''.join(samples))
        return note, frequency

def pack_value(to_pack):
    packed_value = struct.pack('h', int(to_pack))
    return packed_value
