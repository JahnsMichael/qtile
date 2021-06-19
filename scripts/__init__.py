from libqtile.lazy import lazy

import os
import subprocess
import datetime

HOME = os.path.expanduser('~')
SCRIPTS_DIR = f'{HOME}/.config/qtile/scripts/'

def screenshot(qtile):
    date = datetime.datetime.now().strftime("%m%d%Y-%H%M%S")
    filename = os.path.expanduser(f'~/Pictures/Screenshots/{date}.png')
    qtile.cmd_spawn(f'maim -s {filename}')
    
