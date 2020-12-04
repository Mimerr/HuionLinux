""" Handle event processing for the daemon. """
import config
import buttons
import touchstrip

async def process(device):
  """ Process events. """
  async for event in device.async_read_loop():
    if device.name == config.pen_dev_name:
      buttons.handle(event.code, event.value)
    elif device.name == config.pad_dev_name:
      buttons.handle(event.code, event.value)
    elif device.name == config.ts_dev_name:
      touchstrip.handle(event.code, event.value)
