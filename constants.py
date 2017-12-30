__author__ = 'Mike'


import os.path

VLC = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
SHOT_TOTAL = 100

POWER_HOUR = {
    'start': 40,
    'dir': "C:\\Users\migleeso\\Desktop\\century\\power\\",
    'sfx dir': 'start.wav',
    'music': 'ladies.mp3',
    'warn': {
        'time': 35,
        'sfx dir': '5minwarn.wav',
    },
}

SOUND_INFO = {
    'fx': {
        'dir': os.path.abspath(os.path.join("C:/", "Users", "migleeso", "Desktop", "century", "sfx")),
        'lifespan': 5
    },
    'music': {
        'dir': "C:\\Users\migleeso\\Desktop\\century\\music\\",
        'lifespan': 55
    },
}