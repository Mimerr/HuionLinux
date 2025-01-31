import evdev

# Find your pen device
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
pen = None

for device in devices:
    print(f"Found device: {device.name} at {device.path}")
    if "pen" in device.name.lower():  # Adjust this to match your device name
        pen = device
        break

if not pen:
    print("Pen device not found!")
    exit(1)

print(f"Listening for events from: {pen.path}")

# Listen for events
for event in pen.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(f"Button {event.code} {'pressed' if event.value else 'released'}")
