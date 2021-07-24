from libqtile.widget.textbox import TextBox
from lib.const import fontawesome, colors
from libqtile.log_utils import logger


class WindowControl(TextBox):

    action_type = None

    def __init__(self, action_type="KILL", **config):
        self.action_type = action_type

        super().__init__(text=self.get_text(), foreground=self.get_color(), **config)

        self.add_callbacks({
            'Button1': self.action
        })

    def action(self):
        current_win = self.bar.screen.group.current_window
        action_map = {
            "KILL": current_win.cmd_kill,
            "MIN": current_win.cmd_toggle_minimize,
            "MAX": current_win.cmd_toggle_maximize,
            "FLOAT": current_win.cmd_toggle_floating,
        }
        action_map[self.action_type]()

    def get_text(self):
        text_map = {
            "KILL": fontawesome.CLOSE,
            "MIN": fontawesome.MINIMIZE,
            "MAX": fontawesome.MAXIMIZE,
            "FLOAT": fontawesome.FLOAT,
        }
        return text_map[self.action_type]

    def get_color(self):
        color_map = {
            "KILL": colors.red[0],
            "MIN": colors.blue[0],
            "MAX": colors.brown[0],
            "FLOAT": colors.green[0],
        }
        return color_map[self.action_type]
