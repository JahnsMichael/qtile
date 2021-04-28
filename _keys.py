from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
from utils import show_keys
import const

mod = const.MOD


NAV_KEY_CHORDS = [
    Key([], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([], "Up", lazy.layout.up(), desc="Move focus up")
]


def get_keys():
    return [
        # Switch between windows
        Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "Tab", lazy.layout.next(),
            desc="Move window focus to other window"),

        # Move windows between left/right columns or move up/down in current stack.
        Key([mod, "mod1"], "Left", lazy.layout.swap_left(),
            desc="Move window to the left"),
        Key([mod, "mod1"], "Right", lazy.layout.swap_right(),
            desc="Move window to the right"),
        Key([mod, "mod1"], "Down", lazy.layout.shuffle_down(),
            desc="Move window down"),
        Key([mod, "mod1"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod, "shift"], "Left", lazy.layout.shrink(),
            desc="Grow window to the left"),
        Key([mod, "shift"], "Right", lazy.layout.grow(),
            desc="Grow window to the right"),
        Key([mod, "shift"], "Down", lazy.layout.shrink(),
            desc="Grow window down"),
        Key([mod, "shift"], "Up", lazy.layout.grow(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(),
            desc="Reset all window sizes"),
        Key([mod, "shift"], "backslash", lazy.layout.flip()),

        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack"),
        Key([mod], "Return", lazy.group["scratchpad"].dropdown_toggle('term'),
            desc="Launch terminal"),

        # Toggle between different layouts as defined below
        Key([mod, "shift"], "Tab", lazy.next_layout(),
            desc="Toggle between layouts"),
        Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),

        # Move window focus to next screen
        Key([mod, "control"], "Left", lazy.next_screen(),
            desc="Move Focus to next screen"),
        Key([mod, "control"], "Right", lazy.prev_screen(),
            desc="Move Focus to next screen"),

        # Move to next group
        Key([mod], "period", lazy.screen.next_group(),
            desc="Move to the group on the right"),
        Key([mod], "comma", lazy.screen.prev_group(),
            desc="Move to the group on the left"),

        Key([mod], "a", lazy.to_layout_index(2),
            desc="Set current layout to matrix"),
        Key([mod], "s", lazy.to_layout_index(0),
            desc="Set current layout to monadtall"),

        Key([mod, "mod1"], "Return", lazy.window.toggle_maximize(),
            desc="Toggle maximize window"),


        Key([], "XF86MonBrightnessDown", lazy.spawn(["xbacklight", "-dec", "5"]),
            desc="Set brightness down"),

        Key([], "XF86MonBrightnessUp", lazy.spawn(["xbacklight", "-inc", "5"]),
            desc="Set brightness up"),

        Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([mod, "control"], "l", lazy.spawn(["betterlockscreen", "-l"]),
            desc="Lock Screen with betterlockscreen"),
        Key([mod, "control"], "s", lazy.spawn(["betterlockscreen", "-s"]),
            desc="Suspend with betterlockscreen"),
        Key([mod], "r", lazy.spawncmd(),
            desc="Spawn a command using a prompt widget"),
        Key([mod], "space", lazy.spawn(["rofi", "-show", "drun"]),
            desc="Spawn a command using a prompt widget"),
    ]


def get_group_keys(groups):
    keys = []

    for group in groups:

        if (group.name == "scratchpad"):
            continue

        keys.extend([
            Key([mod], group.name[0], lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name)),

            Key([mod, "shift"], group.name[0], lazy.window.togroup(group.name),
                desc="move focused window to group {}".format(group.name)),
        ])

    return keys


def get_manage_mode_keys(groups):
    keys = []
    keychords = NAV_KEY_CHORDS

    for group in groups:
        keychords.append(Key([], group.name[0], lazy.window.togroup(
            group.name), desc="move focused window to group {}".format(group.name)))

    keys.append(KeyChord([mod], "m", keychords))
    keys.append(KeyChord([mod, "shift"], "m", keychords, mode="manage"))

    return keys


def get_kill_mode_keys():
    keys = []
    keychords = NAV_KEY_CHORDS
    keychords.append(
        Key([], "Return", lazy.window.kill(), desc="Kill focused window"),
    )

    keys.append(KeyChord([mod, "shift"], "c", keychords, mode="kill"))

    return keys


def show_keys_key(keys):
    return Key([mod, "shift"], "slash", lazy.spawn("sh -c 'echo \"" + show_keys(keys) +
        "\" | rofi -columns 1 -width 45 -dmenu -i -mesg \"Keyboard shortcuts\"'"), desc="Print keyboard bindings")
