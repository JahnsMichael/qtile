from libqtile.config import Group, ScratchPad, DropDown

groups = [Group(i) for i in [
    "1:[CODE]",
    "2",
    "3:[WWW]",
    "4",
    "5",
    "6:[PEN]",
    "7:[DOC]",
    "8:[MEET]",
    "9:[SOS]",
    "0:[MUSIC]"
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
    ]))


def get_groups():
    return groups
