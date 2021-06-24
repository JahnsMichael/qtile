from libqtile.config import (
    Group,
    Match,
    ScratchPad,
    DropDown
)

GROUPS = [
    Group("1", matches=[
        Match(wm_class="vscodium"),  # vscodium
    ]),
    Group("2"),
    Group("3", matches=[
        Match(role="browser"),  # browser
    ]),
    Group("4"),
    Group("5"),
    Group("6", matches=[
        Match(wm_class="pcmanfm"),  # pcmanfm file browser
    ]),
    Group("7"),
    Group("8"),
    Group("9", matches=[
        Match(wm_class="web.whatsapp.com"),  # Whatsapp Web
        # LINE Browser Extension
        Match(wm_class="ophjlpahpchlmihnnnihgmmeilfjmjjc__index.html"),
    ]),
    Group("0")
]

GROUPS.append(
    ScratchPad("scratchpad", [
        DropDown(
            "term",
            ["alacritty", "-o", "background_opacity=0.8"],
            opacity=1.0,
            x=0, y=-0.032,
            width=0.995, height=1.025
        ),
        DropDown(
            "mocp",
            ["alacritty", "-o", "background_opacity=0.8", "-e", "mocp"],
            opacity=1.0,
            x=0.3, y=0.15,
            width=0.412, height=0.65
        ),
    ]))


def get_groups():
    return GROUPS
