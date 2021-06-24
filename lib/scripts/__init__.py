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
    
def xrandr():
    monitors = get_monitors()
    if (len(monitors) > 1):
        cmd = "xrandr "
        for i in range(1, len(monitors)):
            cmd += f"--output {monitors[i]} --auto --right-of {monitors[i-1]} "
        subprocess.call(cmd, shell=True)

def get_monitors(all=False):
    if (all):
        cmd = "xrandr | grep 'connected ' | awk '{ print$1 }'"
    else:
        cmd = "xrandr | grep ' connected ' | awk '{ print$1 }'"
    monitors = subprocess.check_output(
        cmd, shell=True).decode("utf8").splitlines()
    return monitors