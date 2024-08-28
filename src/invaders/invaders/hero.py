from importlib import resources
import pygame

from invaders.config import Config

class Hero:

  def __init__(self, window):
    self.__is_moving_up = False
    self.__is_moving_down = False
    self.__is_moving_right = False
    self.__is_moving_left = False

    self.__hero_position = pygame.math.Vector2(window.get_width() / 2, window.get_height() / 2)

    with resources.path(Config.instance().data["hero_image_path"], Config.instance().data["hero_image_filename"]) as hero_path:
      self.__hero_image = pygame.image.load(hero_path).convert_alpha()

  def process_events(self, key, is_pressed):
    if key == pygame.K_UP:
      self.__is_moving_up = is_pressed
    elif key == pygame.K_DOWN:
      self.__is_moving_down = is_pressed
    elif key == pygame.K_LEFT:
      self.__is_moving_left = is_pressed
    elif key == pygame.K_RIGHT:
      self.__is_moving_right = is_pressed

  def update(self, delta_time):
    movement = pygame.math.Vector2(0.0, 0.0)

    if self.__is_moving_up:
      movement.y -= Config.instance().data["hero_speed"]
    if self.__is_moving_down:
      movement.y += Config.instance().data["hero_speed"]
    if self.__is_moving_left:
      movement.x -= Config.instance().data["hero_speed"]
    if self.__is_moving_right:
      movement.x += Config.instance().data["hero_speed"]

    self.__hero_position += movement * delta_time

  def render(self, surface_dst):
    surface_dst.blit(self.__hero_image, self.__hero_position.xy)

  def release(self):
    pass