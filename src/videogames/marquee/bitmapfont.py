import os
import pygame
import urllib.request

from config import Config

class BitmapFont:

  def __init__(self):
    urllib.request.urlretrieve(Config.instance().data["font"]["url"], os.path.join(*Config.instance().data["font"]["filename"]))
    self.__image = pygame.image.load(os.path.join(*Config.instance().data["font"]["filename"])).convert_alpha()
    self.__font = dict()
    letter_size = Config.instance().data["font"]["letter_size"]
    letters_x_line = Config.instance().data["font"]["letters_x_line"]

    for i in range(Config.instance().data["font"]["total_letters"]):
      left = letter_size[0] * (i % letters_x_line)
      top = letter_size[1] * int(i / letters_x_line)
      self.__font[self.__translate(i)] = pygame.Rect(left, top, letter_size[0], letter_size[1])

  def render(self, surface_dst, pos, letter):
    surface_dst.blit(self.__image, pos, self.__font[letter.upper()])

  def __translate(self, number):
    if number >=0 and number <=25:
      char = chr(number + 65)
    elif number >=26 and number <= 34:
      char = chr(number + 23)
    else:
      rest = ['0', '-', '.', ':', '?', '!', '(', ')', ' ']
      char = rest[number - 35]

    return char