from libqtile import qtile, widget
from lib.const import colors, fontawesome, fonts

SEP_S = widget.Sep(
    foreground=colors.common['bg'],
    linewidth=5
)
SEP_M = widget.Sep(
    foreground=colors.common['bg'],
    linewidth=10
)
SEP_L = widget.Sep(
    foreground=colors.common['bg'],
    linewidth=20
)


def get_top_widgets():

    group_box_attr = {
        "rounded": False,
        "highlight_method": "line",
        "other_current_screen_border": colors.common['ui'],
        "other_screen_border": colors.common['ui'],
        "inactive": colors.common['ui'],
        "urgent_border": colors.red[2],
        "padding": 5,
    }

    def get_groupbox(text, scheme, groups):
        return [widget.TextBox(
            text=text,
            font=fonts.ICON,
            foreground=scheme[0],
        ),
            widget.GroupBox(
            **group_box_attr,
            highlight_color=[colors.common['bg'], scheme[0]],
            this_screen_border=scheme[0],
            this_current_screen_border=scheme[1],
            visible_groups=groups
        )]

    CODE_GROUPBOX = get_groupbox(
        fontawesome.CODE, [colors.brown[0], colors.brown[2]], ["1", "2"])
    WEB_GROUPBOX = get_groupbox(
        fontawesome.WEB, [colors.blue[0], colors.blue[1]], ["3", "4", "5"])
    DOCS_GROUPBOX = get_groupbox(
        fontawesome.FOLDER, [colors.green[0], colors.green[1]], ["6", "7"])
    MEET_GROUPBOX = get_groupbox(
        fontawesome.CAMERA, [colors.red[0], colors.red[1]], ["8", "9", "0"])
    GROUPBOXES = [
        *CODE_GROUPBOX,
        SEP_M,
        *WEB_GROUPBOX,
        SEP_M,
        *DOCS_GROUPBOX,
        SEP_M,
        *MEET_GROUPBOX
    ]

    MEMORY = [
        widget.TextBox(
            text=fontawesome.MEMORY,
            font=fonts.ICON,
            foreground=colors.blue[0],
        ),
        widget.Memory(
            foreground=colors.blue[0],
            format='{MemPercent}%{MemUsed: .0f}M/{MemTotal: .0f}M',
            font=fonts.MAIN
        ),
    ]

    BATTERY = [
        widget.TextBox(
            text=fontawesome.BATTERY,
            font=fonts.ICON,
            foreground=colors.brown[5],
        ),
        # widget.BatteryIcon(
        #     theme_path="/home/jahnsmichael/.config/qtile/assets/battery",
        #     padding=8,
        # ),
        widget.Battery(
            foreground=colors.brown[5],
            format='{char} {percent:2.0%}',
            discharge_char='',
            low_percentage=0.1,
            low_foreground=colors.red[0],
            notify_below=20,
            show_sort_text=False,
            font=fonts.MAIN
        )
    ]
    CLOCK = [
        widget.TextBox(
            text=fontawesome.CLOCK,
            font=fonts.ICON,
            foreground=colors.green[0],
        ),
        widget.Clock(
            format='%a, %d %b %Y | %H:%M:%S',
            foreground=colors.green[0],
            font=fonts.MAIN
        ),
    ]

    TOP_WIDGETS = [
        *GROUPBOXES, SEP_M,
        widget.WindowName(max_chars=30), SEP_S,
        widget.Chord(), SEP_S,
        *MEMORY, SEP_S,
        *BATTERY, SEP_S,
        *CLOCK, SEP_L
    ]

    return TOP_WIDGETS


def get_bottom_widgets():
    def get_app_btn(text, color, cmd):
        return widget.TextBox(
            text=text,
            font=fonts.ICON,
            foreground=color,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(cmd)
            }
        )

    APP_BTN = [
        get_app_btn(fontawesome.SEARCH, colors.red[0], "rofi -show drun"),
        get_app_btn(fontawesome.CODE, colors.brown[0], "/usr/bin/codium -n"),
        get_app_btn(fontawesome.WEB, colors.blue[0], "/usr/bin/brave"),
        get_app_btn(fontawesome.FOLDER, colors.green[0], "/usr/bin/pcmanfm"),
    ]

    APP_LIST = widget.TaskList(
        border=colors.brown[2],
        rounded=False,
        highlight_method='block',
        txt_floating='🗗 ',
        txt_maximized='🗖 ',
        txt_minimized='🗕 ',
        padding=4,
        margin=0,
        icon_size=15,
        max_title_width=200
    )

    SYSTRAY = widget.Systray(foreground=colors.brown[5])
    POWER = widget.QuickExit(
        default_text=fontawesome.POWER,
        foreground=colors.red[0],
        font=fonts.ICON
    )

    BOTTOM_WIDGETS = [
        SEP_S,
        *APP_BTN,
        SEP_L,
        APP_LIST,
        SEP_S,
        SYSTRAY,
        SEP_L,
        POWER,
        SEP_L
    ]

    return BOTTOM_WIDGETS