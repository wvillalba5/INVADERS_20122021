from setuptools import setup

setup(
  name = "invaders",
  version = "0.0.1",
  packages = ["invaders"],
  entry_points = {"console_scripts":["invaders = invaders.__main__:main"]},
  install_requires = ["pygame"]
)