""" Controls and calculates actions associated with a touch strip. """
import config
import xdotool

scroll_code = 8
touch_code = 40
press_value = 15
release_value = 0

is_scrolling = False
prev_value = -1

up   = {"command": "key", "args": "plus"}
down = {"command": "key", "args": "minus"}

def handle(code, value):
  """ Handle a scroll event. """
  global is_scrolling
  global prev_value
  if code == touch_code:  # Either starting or releasing.
    if value == 15:
      is_scrolling = True
    else:
      is_scrolling = False
      prev_value = -1
  elif code == scroll_code:  # Moving up or down.
    if is_scrolling:
      if prev_value != -1:  # Movement has occurred.
        if value > prev_value:
          xdotool.execute(xdotool.commands[up["command"]], up["args"])
        elif value < prev_value:
          xdotool.execute(xdotool.commands[down["command"]], down["args"])
        else:
          if value == 6:
            xdotool.execute(xdotool.commands[down["command"]], down["args"])
          elif value == 0:
            xdotool.execute(xdotool.commands[up["command"]], up["args"])
      prev_value = value
