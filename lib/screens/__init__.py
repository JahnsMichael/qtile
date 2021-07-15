from libqtile import qtile, bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from lib.scripts import get_monitors, xrandr

from lib.const import colors
from lib.screens.widgets import (
    get_top_widgets,
    get_bottom_widgets
)


def get_default_screen():
    attrs = {"size": 25, "opacity": 0.9}
    return Screen(
        top=bar.Bar(get_top_widgets(), **attrs),
        bottom=bar.Bar(get_bottom_widgets(), **attrs)
    )


def get_screens():
    xrandr()
    return [get_default_screen() for i in range(len(get_monitors()))]
