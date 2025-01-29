import os
import threading as thr
import time
import webview

import huion.config.config as config

class Api:
  profiles = set()

  def get_profiles(self):
    self.profiles.clear()
    ls = os.listdir("{}/config/profiles".format(config.root_dir))
    for f in ls:
      if f.endswith(".json"):
        self.profiles.add(f.split(".")[0])
    config.load_profile(config.app_conf["last_profile"])
    return sorted(self.profiles)

  def set_profile(self, name):
    config.load_profile(name)

  def get_active_profile(self):
    return config.app_conf["last_profile"]


class Gui:
  main_window_is_shown = False
  stop_config_poll = False

  def create(self):
    self.api = Api()
    self.main_window = webview.create_window( "Huion GUI",
                                              config.gui_index,
                                              js_api=self.api,
                                              transparent=True,
                                              frameless=True,
                                              on_top=True,
                                              hidden=True,
                                              confirm_close=True,
                                              min_size=(80, 84),
                                              width=320,
                                              height=config.tablet_height,
                                              x=config.app_conf["last_x"],
                                              y=config.app_conf["last_y"])
    self.main_window.closed += self.on_close
    thr.Thread(target=self.polling, name="Huion Config Poll").start()
    webview.start()

  def on_close(self):
    self.stop_config_poll = True

  def toggle(self):
    try:
      if (self.main_window_is_shown):
        self.main_window.hide()
        self.main_window_is_shown = False
      else:
        self.main_window.show()
        self.main_window_is_shown = True
    except KeyError:
      return  # TODO Need to find a way to just recreate the main window.

  def config_update(self):
    has_changes = False
    if (config.app_conf["last_x"] != self.main_window.x):
      config.app_conf["last_x"] = self.main_window.x
      has_changes = True
    if (config.app_conf["last_y"] != self.main_window.y):
      config.app_conf["last_y"] = self.main_window.y
      has_changes = True
    if (has_changes):
      config.save_app_config()

  def polling(self):
    while not self.stop_config_poll:
      self.config_update()
      time.sleep(1)
