""" Controls and calculates actions associated with a touch strip. """
import huion.config.config as config

import huion.events.xdotool as xdotool

class Touchstrip:
  scroll_code = 8
  touch_code = 40
  press_value = 15
  release_value = 0

  is_scrolling = False
  prev_value = -1

  def handle(self, code, value):
    """ Handle a scroll event. """
    if code == self.touch_code:  # Either starting or releasing.
      if value == 15:
        self.is_scrolling = True
      else:
        self.is_scrolling = False
        self.prev_value = -1
    elif code == self.scroll_code:  # Moving up or down.
      if self.is_scrolling:
        if self.prev_value != -1:  # Movement has occurred.
          up = config.input_conf["touchstrip"]["up"]
          down = config.input_conf["touchstrip"]["down"]
          if value > self.prev_value:
            xdotool.execute(xdotool.commands[up["command"]], up["args"])
          elif value < self.prev_value:
            xdotool.execute(xdotool.commands[down["command"]], down["args"])
          else:
            if value == 6:
              xdotool.execute(xdotool.commands[down["command"]], down["args"])
            elif value == 0:
              xdotool.execute(xdotool.commands[up["command"]], up["args"])
        self.prev_value = value
