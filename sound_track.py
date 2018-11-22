import sys
import pygame
from sound_generator import generate_note
from name_getter import get_name
from pygame import *

mixer.pre_init()
pygame.init()

display = pygame.display.set_mode((150,50))
clock = pygame.time.Clock()

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
while not satisfied:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_1:
            wave_type = "perfect"
            satisfied = True
        elif event.type == KEYDOWN and event.key == K_2:
            wave_type = "square"
            satisfied = True
        elif event.type == KEYDOWN and event.key == K_3:
            wave_type = "saw"
            satisfied = True


notes_set = set()
duration = 1


for steps in range(-21, 16):  # generates and saves all notes from c2 to c5
    name = get_name(steps)
    new_note, freq = generate_note(steps, duration, name, wave_type)
    notes_set.add(name)
    print(name,freq)




'''
note_list = []
note_list.append("C4.wav")
note_list.append("C5.wav")
note_list.append("C2.wav")
for i in range(len(note_list)):
    clock.tick(5)
    mixer.music.load(note_list[i])
    mixer.music.play()
    clock.tick(5)
'''

''' # this stuff just has play/pause functions... 
game_state_list = {"IDLE": 0, "PLAYING": 1, "PAUSED": 2}

game_state = game_state_list["IDLE"]


mixer.music.load("1117.wav")

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if game_state == game_state_list["IDLE"]:
                    mixer.music.play(-1)
                    game_state  = game_state_list["PLAYING"]
                elif game_state == game_state_list["PLAYING"]:
                    mixer.music.pause()
                    game_state = game_state_list["PAUSED"]
                elif game_state == game_state_list["PAUSED"]:
                    mixer.music.unpause()
                    game_state = game_state_list["PLAYING"]
            elif event.key == K_BACKSPACE:
                game_state = game_state_list["IDLE"]
                mixer.music.stop()
            elif event.key == K_ESCAPE:
                quit()
                sys.exit()
    pygame.display.flip()
    clock.tick(30)'''
