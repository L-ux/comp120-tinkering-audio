import math
from audio_constants import *

class waves():
    def perfect_wave(self, sample_number, frequency):
        wave = (math.sin(2.0 * math.pi * frequency *
                         (sample_number / SAMPLE_RATE)) / math.pi) * MAX_VOL
        return wave

    def saw_wave(self, sample_number, frequency):
        wave = 0
        for multiplier in range(1, 6):
            wave += (math.sin(multiplier * 2.0 * math.pi * frequency *
                              (sample_number / SAMPLE_RATE)) /
                     (multiplier * math.pi)) * MAX_VOL
        return wave

    def square_wave(self, sample_number, frequency):
        wave = 0
        for multiplier in range(1, 8, 2):
            wave += (math.sin(multiplier * 2.0 * math.pi * frequency *
                              (sample_number / SAMPLE_RATE)) /
                     (multiplier * math.pi)) * MAX_VOL
        return wave
