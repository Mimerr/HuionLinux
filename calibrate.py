""" Calibrate the tablet. """
import subprocess as sp

import config

# Calculations for the xinput values to set the tablet's location.
C0 = config.tablet_width / config.total_screen_width
C1 = config.tablet_offset_x / config.total_screen_width
C2 = config.tablet_height / config.total_screen_height
C3 = config.tablet_offset_y / config.total_screen_height

def position():
  """ Run the xinput command to calibrate position of the tablet. """
  xinput = "xinput set-prop {} --type=float \"{}\" {} 0 {} 0 {} {} 0 0 1"
  xprop = "Coordinate Transformation Matrix"
  cmd = xinput.format(config.pen_id, xprop, C0, C1, C2, C3)
  return sp.run(cmd, shell=True)

def pen_button_map():
  """ Run the xinput command to clear pen side button functionality. """
  xinput = "xinput set-button-map {} 1 0 0 4 5 6 7"
  cmd = xinput.format(config.pen_id)
  return sp.run(cmd, shell=True)
