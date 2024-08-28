import sys

from PyQt6.QtWidgets import QApplication

from view import View
from model import Model
from controller import Controller

def main():
  '''calc el punto de acceso es el main'''
  calc = QApplication(sys.argv)

  view = View()
  view.show()

  model = Model()
  controller = Controller(view, model)

  sys.exit(calc.exec())

if __name__ == '__main__':
  main()