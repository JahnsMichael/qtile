from libqtile import layout
from libqtile.config import Match
from lib.const import colors

layout_theme = {
    "border_width": 3,
    "fullscreen_border_width": 1,
    "font": "Overpass",
    "margin": 5,
    "border_focus": colors.brown[2],
    "border_normal": colors.common['bg']
}


def get_layouts():
    return [
        layout.MonadTall(**layout_theme),
        layout.Tile(**layout_theme),
        # layout.Columns(**layout_theme),
        # layout.Max(**layout_theme),
        # layout.Matrix(**layout_theme),
        # layout.TreeTab(
        #     bg_color=colors.common['bg'],
        #     active_bg=colors.common['accent'],
        #     inactive_bg=colors.common['fg'],
        #     urgent_bg=colors.red[0],
        #     panel_width=100,
        #     rounded=False,
        #     **layout_theme
        # ),
        # Try more layouts by unleashing below layouts.
        # layout.Bsp(**layout_theme),
        # layout.Stack(num_stacks=2),
        # layout.MonadWide(**layout_theme),
        # layout.RatioTile(**layout_theme),
        # layout.VerticalTile(**layout_theme),
        # layout.Zoomy(**layout_theme),
    ]


def get_floating_layout():
    return layout.Floating(float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry

        # Match(wm_class='pavucontrol'),
        # Match(wm_class='pamac-manager'),
        Match(wm_class='Conky'),
        Match(wm_class='pentablet'),
    ], **layout_theme)
