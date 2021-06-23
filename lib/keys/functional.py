from libqtile.config import Key
from libqtile.lazy import lazy
from lib.scripts import screenshot

UTIL_KEYS = [
    Key([], "XF86MonBrightnessDown", lazy.spawn(["xbacklight", "-dec", "5"]),
            desc="Set brightness down"),
    Key([], "XF86MonBrightnessUp", lazy.spawn(["xbacklight", "-inc", "5"]),
        desc="Set brightness up"),
    Key([], "Print", lazy.function(screenshot),
            desc="Take a screenshot, select region"),
]

ROFI_KEYS = [
    Key([], "space", lazy.spawn(["rofi", "-show", "drun"]),
            desc="rofi -show drun"),
    Key(['mod1'], "space", lazy.spawn(["rofi", "-show", "file-browser-extended"]),
            desc="rofi -show file-browser-extended"),
    Key([], "b", lazy.spawn(["rofi-bluetooth"]),
        desc="rofi-bluetooth"),
]

# def show_keys_key(keys):
#     return Key(
#         [mod, "shift"], "slash",
#         lazy.spawn(
#             "sh -c 'echo \"" +
#             show_keys(keys) +
#             "\" | rofi -columns 1 -width 45 -dmenu -i -mesg \"Keyboard shortcuts\"'"
#         ),
#         desc="Print keyboard bindings"
#     )