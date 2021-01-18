""" Executes commands to xdotool to simulate input. """
import subprocess as sp

xdo = "xdotool {} {}"  # Format ready for command and arguments.

# Command options, for example pass to execute as commands["key"]
commands = {
    "key":       {"command": "key",       "string":  "Key Stroke"},
    "keydown":   {"command": "keydown",   "string":  "Key Press"},
    "keyup":     {"command": "keyup",     "string":  "Key Release"},
    "click":     {"command": "click",     "string":  "Mouse Click"},
    "mousedown": {"command": "mousedown", "string":  "Mouse Press"},
    "mouseup":   {"command": "mouseup",   "string":  "Mouse Release"}
}

def execute(xcmd, args):
  """ Execute an xdotool command with given arguements. """
  cmd = xdo.format(xcmd["command"], args)
  return sp.run(cmd, shell=True)
