from libqtile.config import Key
from libqtile.lazy import lazy

WINDOW_FOCUS_KEYS = [
    Key([], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([], "Up", lazy.layout.up(), desc="Move focus up"),
]

WINDOW_SIZE_KEYS = [
    Key(["shift"], "Left", lazy.layout.shrink(),
        desc="Grow window to the left"),
    Key(["shift"], "Right", lazy.layout.grow(),
        desc="Grow window to the right"),
    Key(["shift"], "Down", lazy.layout.shrink(),
        desc="Grow window down"),
    Key(["shift"], "Up", lazy.layout.grow(), desc="Grow window up"),
    Key([], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    Key(["mod1"], "Return", lazy.window.toggle_maximize(),
        desc="Toggle maximize window"),
]

WINDOW_MOVE_KEYS = [
    Key(["mod1"], "Left", lazy.layout.swap_left(),
        desc="Move window to the left"),
    Key(["mod1"], "Right", lazy.layout.swap_right(),
        desc="Move window to the right"),
    Key(["mod1"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key(["mod1"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(["shift"], "backslash", lazy.layout.flip()),
]

WINDOW_TOGGLE_FLOATING_KEYS = [
    Key(["shift"], "f", lazy.window.toggle_floating(),
        desc="Toggle floating"),
]

WINDOW_KILL_KEYS = [
    Key([], "c", lazy.window.kill(), desc="Kill focused window"),
]

WINDOW_KEYS = [
    *WINDOW_FOCUS_KEYS,
    *WINDOW_KILL_KEYS,
    *WINDOW_MOVE_KEYS,
    *WINDOW_SIZE_KEYS,
    *WINDOW_TOGGLE_FLOATING_KEYS
]