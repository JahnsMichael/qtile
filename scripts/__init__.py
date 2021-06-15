from libqtile.lazy import lazy

import os
import subprocess

HOME = os.path.expanduser('~')
SCRIPTS_DIR = f'{HOME}/.config/qtile/scripts/'

def autostart():
    script = SCRIPTS_DIR + 'autostart'
    subprocess.call([script])

def screenshot(lazy=True):
    script = SCRIPTS_DIR + 'screenshot'
    if lazy:
        lazy.spawn(script)
    else:
        subprocess.call([script])
