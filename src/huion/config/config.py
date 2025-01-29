""" Configurable values. """
import json
import sys

# These are all default values that may be configurable eventually.

# These are values needed to calibrate the position of the tablet.
# To figure these out run the command: xrandr | grep -P '(?<!dis)connected'
# Example: DP-4 connected 1920x1080+2952+2160

# This is the resolution of the tablet itself. The 1920x1080 in the example.
tablet_width = 1920
tablet_height = 1080

# These are the +s after the resolution. The 2952+2160 in the example.
tablet_offset_x = 1600
tablet_offset_y = 1440

# These represent the combined resolution of all monitors.
# With the xrandr output you can find this by adding the width to the x offset
# of each connected monitor and selecting the highest. Then do the same for
# the heights and the y offset.
total_screen_width = 5120 + 1080
total_screen_height = 1440 + 1080

# Id of the pen itself, found with xinput list.
pen_id = "\"HID 256c:006d Pen stylus\""

# Run python aide/list-devices.py to find these values.
pen_dev = "HID 256c:006d"
pad_dev = "HID 256c:006d Pad"
ts_dev  = "HID 256c:006d Touch Strip"

# Root directory of the application.
root_dir = "{}/..".format(sys.path[0])  # Relative to main.py.
gui_index = "{}/gui/index.html".format(root_dir)

# App configuration loader.
app_conf = []
with open("{}/config/config.json".format(root_dir)) as json_file:
  app_conf = json.load(json_file)

def save_app_config():
  with open("{}/config/config.json".format(root_dir), "w") as json_file:
    json.dump(app_conf, json_file, indent=2)

# Profile configurations.
default_input_conf = {
  "buttons": {
    "256": {"command": "key",     "args": "Up"},
    "257": {"command": "key",     "args": "Down"},
    "258": {"command": "keydown", "args": "super"},
    "259": {"command": "keydown", "args": "ctrl"},
    "260": {"command": "keydown", "args": "shift"},
    "261": {"command": "keydown", "args": "alt"},
    "332": {"command": "click",   "args": "3"},
    "331": {"command": "click",   "args": "2"}
  },
  "touchstrip": {
    "up":   {"command": "click", "args": "4"},
    "down": {"command": "click", "args": "5"}
  }
}

input_conf = []
def load_profile(name):
  try:
    with open("{}/config/profiles/{}.json".format(root_dir, name)) as j_file:
      global input_conf
      input_conf = json.load(j_file)
  except FileNotFoundError:
    # If the given profile doesn't exist use a default setup.
    input_conf = default_input_conf
  app_conf["last_profile"] = name
  save_app_config()

load_profile(app_conf["last_profile"])
