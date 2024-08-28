from importlib import resources
import os
import pygame

from invaders.fps_stats import FPSStats
from invaders.config import Config
from invaders.hero import Hero

class Game:

  def __init__(self):
    pygame.init()

    self.__window = pygame.display.set_mode(Config.instance().data["screen_size"], 0, 32)
    pygame.display.set_caption(Config.instance().data["game_title"])

    self.__running = False

    with resources.path(Config.instance().data["font_path"], Config.instance().data["font_filename"]) as font_path:
      my_font = pygame.font.Font(font_path, Config.instance().data["font_size"])

    self.__fps_stats = FPSStats(my_font)

    self.__hero = Hero(self.__window)

  def run(self):
    self.__running = True

    fps_clock = pygame.time.Clock()
    while self.__running:
      delta_time = fps_clock.tick(Config.instance().data["fps"])

      self.__process_events()
      self.__update(delta_time)
      self.__render()

    self.__quit()

  def __process_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.__running = False
      if event.type == pygame.KEYDOWN:
        self.__hero.process_events(event.key, True)
      elif event.type == pygame.KEYUP:
        self.__hero.process_events(event.key, False)

  def __update(self, delta_time):
    self.__hero.update(delta_time)
    self.__fps_stats.update(delta_time)

  def __render(self):
    self.__window.fill(Config.instance().data["background_color"])

    self.__hero.render(self.__window)
    self.__fps_stats.render(self.__window)

    pygame.display.update()

  def __quit(self):
    pygame.quit()