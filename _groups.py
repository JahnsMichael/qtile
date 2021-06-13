from libqtile.config import Group, ScratchPad, DropDown

groups = [Group(i) for i in [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0"
]]

groups.append(
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
    return groups
