import json
import os

class Config:

  __config_path = ["assets", "config", "config.json"]
  __instance = None

  @staticmethod
  def instance():
    if Config.__instance is None:
      Config()

    return Config.__instance

  def __init__(self):
    if Config.__instance is None:
      Config.__instance = self

      with open(os.path.join(*Config.__config_path)) as file:
        self.data = json.load(file)

    else:
      raise exception("Not allowed multiple instances")