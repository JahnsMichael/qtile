from libqtile import qtile, bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from lib.scripts import get_monitors

from lib.const import colors
from lib.screens.widgets import (
    TOP_WIDGETS,
    BOTTOM_WIDGETS
)


def get_default_screen():
    attrs = {"size": 25, "opacity": 0.9}
    return Screen(
        top=bar.Bar(TOP_WIDGETS, **attrs),
        bottom=bar.Bar(BOTTOM_WIDGETS, **attrs)
    )


def get_screens():
    return [get_default_screen() for i in range(len(get_monitors()))]
