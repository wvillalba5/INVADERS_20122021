from invaders.config import Config

class FPSStats:

  def __init__(self, font):
    self.__font = font
    self.__update_time = 0
    self.__frames = 0
    self.__set_fps_surface()

  def update(self, delta_time):
    self.__update_time += delta_time
    self.__frames += 1

    if self.__update_time >= Config.instance().data["max_update_time"]:
      self.__set_fps_surface()

      self.__update_time -= Config.instance().data["max_update_time"]
      self.__frames = 0

  def render(self, surface_dst):
    surface_dst.blit(self.__fps_image, (0,0))

  def __set_fps_surface(self):
    self.__fps_image = self.__font.render(f"{self.__frames} FPS", True, Config.instance().data["foreground_color"], Config.instance().data["background_color"])