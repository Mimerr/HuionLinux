""" Controls and calculates actions associated with buttons. """
import huion.config.config as config

import huion.events.xdotool as xdotool

class Buttons:
  # Codes for pad buttons top to bottom and pen buttons top to bottom.
  codes = [256, 257, 258, 259, 260, 261, 262, 331, 332]
  gui_toggle_code = 262  # The hardware settings button toggles gui.

  def __init__(self, gui):
    self.gui = gui

  def handle(self, code, value):
    """ Handle a button event. """
    if code not in self.codes:
      return
    if code == self.gui_toggle_code:
      if value == 0:
        self.gui.toggle()
      return

    button = config.input_conf["buttons"][str(code)]

    is_up = value == 0
    is_up_cmd = button["command"] in ["key", "keyup", "click", "mouseup"]

    if button["command"] is None or button["command"] == "none":
      return

    if (is_up_cmd and is_up):
      xdotool.execute(xdotool.commands[button["command"]], button["args"])
    elif button["command"] == "keydown" and is_up:
      xdotool.execute(xdotool.commands["keyup"], button["args"])
    elif button["command"] == "mousedown" and is_up:
      xdotool.execute(xdotool.commands["mouseup"], button["args"])
