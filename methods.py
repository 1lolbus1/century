import os
import random
import subprocess
import time

from mutagen.mp3 import MP3

from constants import VLC, SOUND_INFO, POWER_HOUR

__author__ = 'Mike'

def run_and_kill(loc, run_time, options=""):
    """
    Logic for killing songs after run_time seconds

    :param loc: where the song is located
    :param run_time: time alive
    :return:
    """
    exit = "--play-and-exit"
    if options:
        process = subprocess.Popen([VLC, exit, options, loc], stdout=subprocess.PIPE,
                                   shell=True)
    else:
        process = subprocess.Popen([VLC, exit, loc], stdout=subprocess.PIPE,
                                   shell=True)
    time.sleep(run_time)
    subprocess.call(['taskkill', '/F', '/T', '/PID', str(process.pid)])


def determine_start_time(music_file):
    music_info = MP3(music_file)
    return random.randint(0, int(music_info.info.length) - SOUND_INFO['music']['lifespan'])