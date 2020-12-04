""" Configurable values. """
import os

# These are all default values that may be configurable eventually.

# These are values needed to calibrate the position of the tablet.
# To figure these out run the command: xrandr | grep -P '(?<!dis)connected'
# Example: DP-4 connected 1920x1080+2952+2160

# This is the resolution of the tablet itself. The 1920x1080 in the example.
tablet_width = 1920
tablet_height = 1080

# These are the +s after the resolution. The 2952+2160 in the example.
tablet_offset_x = 2952
tablet_offset_y = 2160

# These represent the combined resolution of all monitors.
# With the xrandr output you can find this by adding the width to the x offset
# of each connected monitor and selecting the highest. Then do the same for
# the heights and the y offset.
total_screen_width = 3840 + 1920
total_screen_height = 2160 + 1080

# Id of the pen itself, found with xinput list.
pen_id = "\"HID 256c:006d stylus\""

# Run python list-devices.py to find these values.
pen_dev_name = "HID 256c:006d"
pad_dev_name = "HID 256c:006d Pad"
ts_dev_name  = "HID 256c:006d Touch Strip"

# This is where the error output will be written to a file.
output_path = "{0}/output".format(os.getcwd())
output_finm = "huion-error-output.txt"
