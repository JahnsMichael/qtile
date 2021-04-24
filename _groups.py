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
        DropDown("term", "alacritty", on_focus_lost_hide=True, opacity=1.0),
    ]))


def get_groups():
    return groups
