""" The background process to manage setup and event loop. """
import asyncio
import evdev

import calibrate
import config
import eventor
import output

# -----------------------------------------------------------------------------
# Calibrate tablet position and button maps.
# -----------------------------------------------------------------------------
rc = calibrate.position()
if rc.returncode != 0:
  output.append("Calibration Failed.")

rc = calibrate.pen_button_map()
if rc.returncode != 0:
  output.append("Pen Button Mapping Failed.")

# -----------------------------------------------------------------------------
# Set device paths and event handler.
# -----------------------------------------------------------------------------
pen = evdev.InputDevice(config.pen_dev_path)
pad = evdev.InputDevice(config.pad_dev_path)
ts  = evdev.InputDevice(config.ts_dev_path)

pad.grab()
ts.grab()

huion_devices = [pen, pad, ts]

for device in huion_devices:
  asyncio.ensure_future(eventor.process(device))

# -----------------------------------------------------------------------------
# Start the event loop.
# -----------------------------------------------------------------------------
loop = asyncio.get_event_loop()
loop.run_forever()
