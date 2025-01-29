import threading as thr

import huion.daemon.daemon as daemon
import huion.events.buttons as buttons
import huion.events.touchstrip as touchstrip
import huion.gui.gui as gui
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

class Main:
  def __init__(self):
    self.gui = gui.Gui()
    self.buttons = buttons.Buttons(self.gui)
    self.touchstrip = touchstrip.Touchstrip()
    self.daemon = daemon.HuionDaemon(self.buttons, self.touchstrip)

main = Main()
thr.Thread(target=main.daemon.start, name="Huion Daemon").start()
main.gui.create()
