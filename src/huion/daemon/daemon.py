""" The background process to manage setup and event loop. """
import asyncio
import evdev

import huion.config.config as config
import huion.daemon.calibrate as calibrate

def get_or_create_eventloop():
  try:
    return asyncio.get_event_loop()
  except RuntimeError as ex:
    if "There is no current event loop in thread" in str(ex):
      loop = asyncio.new_event_loop()
      asyncio.set_event_loop(loop)
      return asyncio.get_event_loop()

class HuionDaemon:
  def __init__(self, buttons, touchstrip):
    self.buttons = buttons
    self.touchstrip = touchstrip
    calibrate.position()
    calibrate.pen_button_map()

  def start(self):
    loop = get_or_create_eventloop()
    huion_devices = []
    config_devices = [config.pen_dev, config.pad_dev, config.ts_dev]
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
      if device.name in config_devices:
        dev = evdev.InputDevice(device.path)
        huion_devices.append(dev)
        if device.name != config.pen_dev:
          dev.grab()

    for device in huion_devices:
      asyncio.ensure_future(self.process(device))

    loop.run_forever()

  async def process(self, device):
    async for event in device.async_read_loop():
      if device.name == config.pen_dev:
        self.buttons.handle(event.code, event.value)
      elif device.name == config.pad_dev:
        self.buttons.handle(event.code, event.value)
      elif device.name == config.ts_dev:
        self.touchstrip.handle(event.code, event.value)
