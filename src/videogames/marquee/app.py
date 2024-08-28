import pygame

from config import Config
from scroll import Scroll

class App:

  def __init__(self):
    pygame.init()
    self.__window = pygame.display.set_mode(Config.instance().data["screen_size"])

    self.__scroll = Scroll()
    self.__fps_clock = pygame.time.Clock()

  def run(self):
    self.__running = True
    while self.__running:
      delta_time = self.__fps_clock.tick(Config.instance().data["fps"])
      self.__process_events()
      self.__update(delta_time)
      self.__render()
    self.__quit()

  def __process_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.__running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.__running = False

  def __update(self, delta_time):
    self.__scroll.update(delta_time)

  def __render(self):
    self.__window.fill(Config.instance().data["background_color"])
    self.__scroll.render(self.__window)
    pygame.display.update()

  def __quit(self):
    pygame.quit()
