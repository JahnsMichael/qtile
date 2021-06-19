from libqtile.config import Key
from libqtile.lazy import lazy

CONTROL_KEYS = [
    Key(["control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key(["control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(["control"], "l", lazy.spawn(["betterlockscreen", "-l"]),
        desc="Lock Screen with betterlockscreen"),
    Key(["control"], "s", lazy.spawn(["betterlockscreen", "-s"]),
        desc="Suspend with betterlockscreen"),
]