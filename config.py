                                                               
#   ▄▄█▀▀██▄                               ▀███▀▀▀██▄ ▀███▀▀▀███ 
# ▄██▀    ▀██▄                               ██    ▀██▄ ██    ▀█ 
# ██▀      ▀██ ▄█▀██▄ ▀██▀   ▀██▀███  ▀███   ██     ▀██ ██   █   
# ██        ████   ██   ██   ▄█   ██    ██   ██      ██ ██████   
# ██▄      ▄██ ▄█████    ██ ▄█    ██    ██   ██     ▄██ ██   █  ▄
# ▀██▄    ▄██▀██   ██     ███     ██    ██   ██    ▄██▀ ██     ▄█
#   ▀▀████▀▀  ▀████▀██▄   ▄█      ▀████▀███▄████████▀ ▄██████████
#       ███             ▄█                                       
#        ▀████▀       ██▀                                        

# Qtile config for Jahns Michael's desktop.

# Inpired by Ayu Colorschemes https://github.com/ayu-theme/ayu-colors.

from typing import List  # noqa: F401

from libqtile import hook

from utils import xrandr, get_monitors
from _screens import get_screens
from _keys import get_keys, get_group_keys, get_manage_mode_keys, get_kill_mode_keys, show_keys_key
from _groups import get_groups
from _layouts import get_floating_layout, get_layouts
from _mouse import get_mouse

import os
import subprocess
import colors
import const

mod = const.MOD
terminal = const.TERM


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
    xrandr()


@hook.subscribe.startup
def every_start():
    xrandr()


@hook.subscribe.screen_change
def reset_screen(e):
    screens = get_screens()


groups = get_groups()

keys = get_keys()
keys.extend(get_group_keys(groups))
keys.extend(get_manage_mode_keys(groups))
keys.extend(get_kill_mode_keys())
keys.append(show_keys_key(keys))

layouts = get_layouts()

widget_defaults = dict(
    font='Overpass',
    fontsize=12,
    padding=10,
    background=colors.common['bg']
)
extension_defaults = widget_defaults.copy()

screens = get_screens()

# Drag floating layouts.
mouse = get_mouse()

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = True
floating_layout = get_floating_layout()
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
