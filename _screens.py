from libqtile import bar, widget
from libqtile.config import Screen
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
                    highlight_color= [colors.common['bg'], colors.brown[2]],
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
                    foreground=colors.blue[1],
                    format='{MemPercent}%{MemUsed: .0f}M/{MemTotal: .0f}M'
                ),
                get_sep(),
                widget.Systray(foreground=colors.brown[5]),
                get_sep(),
                widget.Clock(
                    format='%a, %d %b %Y | %H:%M',
                    foreground=colors.green[1],
                ),
                get_sep(),
                widget.QuickExit(
                    default_text='⏻',
                    foreground=colors.red[2],
                ),
                get_sep(),
            ],
            24,
        )
    )

def get_screens():
    return [get_default_screen() for i in range(len(get_monitors()))]
