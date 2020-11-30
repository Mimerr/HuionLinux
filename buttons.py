""" Controls and calculates actions associated with buttons. """
import xdotool

buttons = {
    256: {"command": "key", "args": "p"},         # Top Pad
    257: {"command": "key", "args": "r"},
    258: {"command": "key", "args": "shift+e"},
    259: {"command": "key", "args": "ctrl+z"},
    260: {"command": "key", "args": "ctrl+y"},
    261: {"command": "keydown", "args": "ctrl"},
    262: {"command": "keydown", "args": "ctrl"},  # Bottom Pad
    332: {"command": "click", "args": "3"},       # Top Pen
    331: {"command": "keydown", "args": "alt"}    # Bottom Pen
}

codes = [256, 257, 258, 259, 260, 261, 262, 331, 332]

def handle(code, value):
  """ Handle a scroll event. """
  if code not in codes:
    return
  button = buttons[code]

  is_up = value == 0
  is_up_cmd = button["command"] in ["key", "keyup", "click", "mouseup"]

  if button["command"] is None or button["command"] == "none":
    return

  if (is_up_cmd and is_up) or (not is_up_cmd and not is_up):
    xdotool.execute(xdotool.commands[button["command"]], button["args"])
  elif button["command"] == "keydown" and is_up:
    xdotool.execute(xdotool.commands["keyup"], button["args"])
  elif button["command"] == "mousedown" and is_up:
    xdotool.execute(xdotool.commands["mouseup"], button["args"])
