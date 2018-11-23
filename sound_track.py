import sys
from sound_generator import *
from name_getter import get_name
import pygame
from pygame import mixer
from pygame.locals import *
from notation_worker import *
from name_getter import frequency_getter

mixer.pre_init()
pygame.init()

display = pygame.display.set_mode((150,50))
clock = pygame.time.Clock()

# just some notes i used along the way
''' 
 a3 is 0 steps as we are using this as our baseline, we want to go down to 
        c2 and up to c5
 c2 = -21, c3 = -9 steps c4(m) = +3 steps, c5 = + 15 steps

so to figure out the filename, keep adding 12 or taking until
0 <= x <= 11 and then the number remaining determines the note.

is 0 = A, 1 = A#/Bb, 2 = B, 3 = C, 4 = C#/Db, 5 = D, 6 = D#/Eb, 7 = E,
   8 = F, 9 = F#/Gb, 10 = G, 11 = G#/Ab......

get the number of times needed to get into the 0,11 range, and that will
 be used to determine the octave
'''

satisfied = False
while not satisfied:  # asks for input to determine what wave type to make
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_1:  # number 1 pressed
            wave_type = "perfect"
            satisfied = True
        elif event.type == KEYDOWN and event.key == K_2:  # number 2 pressed
            wave_type = "square"
            satisfied = True
        elif event.type == KEYDOWN and event.key == K_3:  # number 3 pressed
            wave_type = "saw"
            satisfied = True

'''duration = 1
for steps in range(-21, 16):  # generates and saves all notes from c2 to c5
    name = get_name(steps)
    lsit = [(steps, duration)]
    generate_note(lsit, name, wave_type)'''

# Plays a chosen random melody a few times
all_notes = []
for i in range(14):
    melody = random_melody_getter()
    for i in range(len(melody)):
        all_notes.append(melody[i])
        # uncommenting this chunk will play the melody before saving it
        '''plays_number = melody[i][1]
        while plays_number > 0:
            mixer.music.load(melody[i][0])
            mixer.music.play()
            clock.tick(5)
            plays_number -= 1'''

# The code from here saves the melody to a single .wav file, because I never
#  found out how to use .ogg files
list_for_notes = []
for i in range(len(all_notes)):
    steps = frequency_getter(all_notes[i][0])
    list_for_notes.append((steps, all_notes[i][1]))

generate_note(list_for_notes, "Melody.wav", wave_type)
