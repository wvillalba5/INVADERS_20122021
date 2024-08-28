import pygame

from config import Config
from bitmapfont import BitmapFont

class Scroll:

  def __init__(self):
    self.__text = list(Config.instance().data["scroll"]["text"])
    self.__pos = pygame.math.Vector2(Config.instance().data["screen_size"][0], Config.instance().data["screen_size"][1]/2)
    self.__current_letter_index = 0

    self.__font = BitmapFont()

  def update(self, delta_time):
    self.__pos.x -= Config.instance().data["scroll"]["speed"] * delta_time
    if self.__pos.x <= -Config.instance().data["font"]["letter_size"][0]:
      self.__pos.x = 0
      self.__current_letter_index += 1

  def render(self, surface_dst):
    letters_in_screen = int((Config.instance().data["screen_size"][0] - self.__pos.x) / Config.instance().data["font"]["letter_size"][0]) + 1
    print(letters_in_screen)
    for i in range(letters_in_screen):
      index = (self.__current_letter_index + i) % len(self.__text)
      pos = (self.__pos.x + (Config.instance().data["font"]["letter_size"][0] * i), self.__pos.y)
      letter = self.__text[index]
      self.__font.render(surface_dst, pos, letter)