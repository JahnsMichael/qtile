from libqtile import qtile, bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from lib.scripts import get_monitors

from lib.const import colors


def get_sep(width=5):
    return widget.Sep(
        foreground=colors.common['bg'],
        linewidth=width
    )


def get_default_screen():
    group_box_attr = {
        "rounded" : False,
        "highlight_method" : "line",
        "other_current_screen_border" : colors.common['ui'],
        "other_screen_border" : colors.common['ui'],
        "inactive" : colors.common['ui'],
        "urgent_border" : colors.red[2],
        "padding" : 5,
    }
    return Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors.brown[0],
                ),
                widget.GroupBox(
                    **group_box_attr,
                    highlight_color=[colors.common['bg'], colors.brown[2]],
                    this_screen_border=colors.common['accent'],
                    this_current_screen_border=colors.brown[2],
                    visible_groups=["1", "2"]
                ),
                get_sep(10),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors.blue[0]
                ),
                widget.GroupBox(
                    **group_box_attr,
                    highlight_color=[colors.common['bg'], colors.blue[0]],
                    this_screen_border=colors.blue[0],
                    this_current_screen_border=colors.blue[1],
                    visible_groups=["3", "4", "5"]
                ),
                get_sep(10),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors.green[0],
                ),
                widget.GroupBox(
                    **group_box_attr,
                    highlight_color=[colors.common['bg'], colors.green[0]],
                    this_screen_border=colors.green[0],
                    this_current_screen_border=colors.green[1],
                    visible_groups=["6", "7"]
                ),
                get_sep(10),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors.red[0],
                ),
                widget.GroupBox(
                    **group_box_attr,
                    highlight_color=[colors.common['bg'], colors.red[0]],
                    this_screen_border=colors.red[0],
                    this_current_screen_border=colors.red[1],
                    visible_groups=["8", "9", "0"]
                ),
                get_sep(10),
                widget.WindowName(max_chars=30),
                get_sep(),
                widget.Chord(),
                get_sep(),
                widget.Memory(
                    foreground=colors.blue[0],
                    format='RAM {MemPercent}%{MemUsed: .0f}M/{MemTotal: .0f}M',
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
                get_sep(20),
            ],
            25,
            opacity=0.90
        ),
        bottom=bar.Bar(
            [
                get_sep(),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors.green[0],
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn(["rofi", "-show", "drun"])
                    }
                ),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors.brown[1],
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn(["pcmanfm"])
                    }
                ),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors.red[0],
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn(["alacritty"])
                    }
                ),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free Solid",
                    foreground=colors.blue[0],
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn(["brave"])
                    }
                ),
                get_sep(20),
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
                get_sep(20),
                widget.QuickExit(
                    default_text='',
                    foreground=colors.red[0],
                    font='Font Awesome 5 Free Solid'
                ),
                get_sep(20),
            ],
            25,
            opacity=0.90,
        )
    )


def get_screens():
    return [get_default_screen() for i in range(len(get_monitors()))]
