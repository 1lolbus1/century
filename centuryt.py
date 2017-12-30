import os
import random
import time
import subprocess
import signal

from constants import SOUND_INFO, VLC, SHOT_TOTAL, POWER_HOUR
from methods import run_and_kill, determine_start_time

__author__ = 'Mike'

# debug
print(VLC)
count = 1
sounds = os.listdir(SOUND_INFO['fx']['dir'])
music = os.listdir(SOUND_INFO['music']['dir'])
print(sounds)
random.shuffle(sounds)
random.shuffle(music)
print("Shuffled sounds:", sounds)
print("Shuffled music:", music)
while count <= SHOT_TOTAL:
    sound_file = sounds[0]
    music_file = music[0]
    print('sound effect file: ', sound_file, 'count: ', count)
    fx_loc = os.path.abspath(os.path.join(SOUND_INFO['fx']['dir'], sound_file))
    print(fx_loc)
    music_loc = SOUND_INFO['music']['dir'] + music_file

    # power hour special case
    if count == POWER_HOUR['warn']['time']:
        fx_loc = POWER_HOUR['dir'] + POWER_HOUR['warn']['sfx dir']
    elif count == POWER_HOUR['start']:
        fx_loc = POWER_HOUR['dir'] + POWER_HOUR['sfx dir']
        music_loc = POWER_HOUR['dir'] + POWER_HOUR['music']

    op = "--start-time={start}".format(start=determine_start_time(music_loc))
    run_and_kill(fx_loc, SOUND_INFO['fx']['lifespan'])
    run_and_kill(music_loc, SOUND_INFO['music']['lifespan'], op)
    count += 1
    if len(sounds) > 1:
        del sounds[0]
    if len(music) > 1:
        del music[0]

print("done!")

