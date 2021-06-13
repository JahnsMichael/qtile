from libqtile import qtile, bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from utils import get_monitors

import colors


def get_sep():
    return widget.Sep(
        foreground=colors.common['bg'],
        linewidth=5
    )


def get_default_screen():
    return Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    rounded=False,
                    highlight_method="line",
                    highlight_color=[colors.common['bg'], colors.brown[2]],
                    this_screen_border=colors.common['accent'],
                    this_current_screen_border=colors.brown[2],
                    other_current_screen_border=colors.common['ui'],
                    other_screen_border=colors.common['ui'],
                    inactive=colors.common['ui'],
                    urgent_border=colors.red[2],
                    padding=5,
                ),
                widget.WindowName(max_chars=30),
                get_sep(),
                widget.Notify(max_chars=30),
                get_sep(),
                widget.CurrentLayout(),
                get_sep(),
                widget.Chord(),
                get_sep(),
                widget.Memory(
                    foreground=colors.blue[0],
                    format='{MemPercent}%{MemUsed: .0f}M/{MemTotal: .0f}M',
                    font='Titillium Web Bold'
                ),
                get_sep(),
                widget.Battery(
                    foreground=colors.brown[5],
                    format='{char} {percent:2.0%}',
                    discharge_char='',
                    low_percentage=0.1,
                    low_foreground=colors.red[0],
                    # notify_below=20,
                    show_sort_text=False,
                    font='Titillium Web Bold'
                ),
                get_sep(),
                widget.Clock(
                    format='%a, %d %b %Y | %H:%M:%S',
                    foreground=colors.green[0],
                    font='Titillium Web Bold'
                ),
                get_sep(),
            ],
            25,
            opacity=0.90
        ),
        bottom=bar.Bar(
            [
                get_sep(),
                widget.Image(
                    filename='~/.config/qtile/assets/manjaro-logo.png',
                    margin=2,
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn(["rofi", "-show", "drun"])
                    }
                ),
                get_sep(),
                widget.TaskList(
                    border=colors.brown[2],
                    rounded=False,
                    highlight_method='block',
                    txt_floating='🗗 ',
                    txt_maximized='🗖 ',
                    txt_minimized='🗕 ',
                    padding=4,
                    margin=0,
                    icon_size=15,
                    max_title_width=200,
                ),
                get_sep(),
                widget.Systray(foreground=colors.brown[5]),
                get_sep(),
                widget.QuickExit(
                    default_text='⏻',
                    foreground=colors.red[0],
                    font='Titillium Web Bold'
                ),
                get_sep(),
            ],
            25,
            opacity=0.90,
        )
    )


def get_screens():
    return [get_default_screen() for i in range(len(get_monitors()))]
