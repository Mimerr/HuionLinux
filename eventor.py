""" Handle event processing for the daemon. """
import config
import buttons
import touchstrip

async def process(device):
  """ Process events. """
  async for event in device.async_read_loop():
    if device.path == config.pen_dev_path:
      buttons.handle(event.code, event.value)
    elif device.path == config.pad_dev_path:
      buttons.handle(event.code, event.value)
    elif device.path == config.ts_dev_path:
      touchstrip.handle(event.code, event.value)
