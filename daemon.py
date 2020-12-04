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
huion_devices = []
config_devices = [config.pen_dev_name, config.pad_dev_name, config.ts_dev_name]
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
  if device.name in config_devices:
    dev = evdev.InputDevice(device.path)
    huion_devices.append(dev)
    if device.name != config.pen_dev_name:
      dev.grab()

for device in huion_devices:
  asyncio.ensure_future(eventor.process(device))

# -----------------------------------------------------------------------------
# Start the event loop.
# -----------------------------------------------------------------------------
loop = asyncio.get_event_loop()
loop.run_forever()
