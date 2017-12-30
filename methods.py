""" repeatable production logic goes here
"""
import random
import subprocess
import time

from mutagen.mp3 import MP3

from constants import VLC, SOUND_INFO


def run_and_kill(loc, run_time, options=""):
    """
    Logic for killing songs after run_time seconds

    :param loc: where the song is located
    :param run_time: time alive
    :param options: special option flags for vlc run
    :return:
    """
    ext = "--play-and-ext"
    if options:
        process = subprocess.Popen([VLC, ext, options, loc], stdout=subprocess.PIPE,
                                   shell=True)
    else:
        process = subprocess.Popen([VLC, ext, loc], stdout=subprocess.PIPE,
                                   shell=True)
    time.sleep(run_time)
    # windows only. make some linux detection for linux use
    subprocess.call(['taskkill', '/F', '/T', '/PID', str(process.pid)])


def determine_start_time(music_file):
    """
    find a random start time for a song

    :param music_file: mp3 music file
    :return: a valid start time within SOUND_INFO['music'][lifespan] (55) seconds of the end
    """
    music_info = MP3(music_file)
    return random.randint(0, int(music_info.info.length) - SOUND_INFO['music']['lifespan'])
