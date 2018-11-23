import math
from audio_constants import *


class Waves:
    """Exists to hold all the different wave functions."""
    @staticmethod
    def multiplied_wave(sample_number, frequency, multiplier):
        wave = (math.sin(multiplier * 2.0 * math.pi * frequency *
                         (sample_number / SAMPLE_RATE)) /
                (multiplier * math.pi)) * MAX_VOL
        return wave

    @staticmethod
    def perfect_wave(sample_number, frequency):
        wave = Waves.multiplied_wave(sample_number, frequency, 1)
        return wave

    @staticmethod
    def saw_wave(sample_number, frequency):
        wave = 0
        for multiplier in range(1, 6):
            wave += Waves.multiplied_wave(sample_number, frequency, multiplier)
        return wave

    @staticmethod
    def square_wave(sample_number, frequency):
        wave = 0
        for multiplier in range(1, 8, 2):
            wave += Waves.multiplied_wave(sample_number, frequency, multiplier)
        return wave
