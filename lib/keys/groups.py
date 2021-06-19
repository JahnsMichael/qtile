from libqtile.config import Key
from libqtile.lazy import lazy
from lib.groups import get_groups

SCRATCHPAD_KEYS = [
    Key([], "Return", lazy.group["scratchpad"].dropdown_toggle('term'),
        desc="Launch terminal"),
    Key([], "backslash", lazy.group["scratchpad"].dropdown_toggle('mocp'),
        desc="Launch mocp"),
]

GROUP_CYCLE_KEYS = [
    Key([], "period", lazy.screen.next_group(),
            desc="Move to the group on the right"),
    Key([], "comma", lazy.screen.prev_group(),
        desc="Move to the group on the left"),
]

GROUP_KEYS = [*SCRATCHPAD_KEYS, *GROUP_CYCLE_KEYS]

for group in get_groups():

    if (group.name == "scratchpad"):
        continue

    GROUP_KEYS.extend([
        Key([], group.name[0], lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),
        Key(["shift"], group.name[0], lazy.window.togroup(group.name),
            desc="move focused window to group {}".format(group.name)),
        Key(["mod1"], group.name[0], lazy.window.togroup(group.name),
            desc="move focused window to group {}".format(group.name)),
    ])
