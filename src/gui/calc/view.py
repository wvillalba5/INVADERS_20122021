from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt

class View(QMainWindow):

  def __init__(self):
    super().__init__()

    self.setWindowTitle('MyCalc')
    '''With rezise is not change the size'''
    self.setFixedSize(235, 235)
    '''El Qwidget class is the base class of all user interface objects'''
    self.__central_widget = QWidget(self)
    self.setCentralWidget(self.__central_widget)

    '''Creating a Layaout'''
    self.main_layout = QVBoxLayout()
    self.__central_widget.setLayout(self.main_layout)
    '''Calling to the functions'''
    self.__create_display()
    self.__create_buttons()

  def __create_display(self):
    '''Create a display with a size of 35'''
    self.display = QLineEdit()
    '''set the hight display'''
    self.display.setFixedHeight(35)
    '''Set the read only to the display'''
    # self.display.setReadOnly(True)
    '''Text  alingment to right'''
    self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
    '''It is so important to enter the displas inside the main layaout'''
    self.main_layout.addWidget(self.display)




  def __create_buttons(self):
    buttons_layout = QGridLayout()

    buttons = {'7' : (0,0), '8' : (0,1), '9' : (0,2), '/' : (0,3), 'C' : (0,4),
               '4' : (1,0), '5' : (1,1), '6' : (1,2), '*' : (1,3), '(' : (1,4),
               '1' : (2,0), '2' : (2,1), '3' : (2,2), '-' : (2,3), ')' : (2,4),
               '0' : (3,0), '00' : (3,1), '.' : (3,2), '+' : (3,3), '=' : (3,4)}

    self.buttons = dict()
    '''read the dictionary buttons'''
    for text, position in buttons.items():
      '''Create a dictionary of button inside a public reference '''
      self.buttons[text] = QPushButton(text)
      '''Size of the button'''
      self.buttons[text].setFixedSize(35,35)
      ''' clave = Text  and Value  == position, then with position get the tupla '''
      buttons_layout.addWidget(self.buttons[text], position[0], position[1])
    '''It is so important to enter the buttons inside the main layaout'''
    self.main_layout.addLayout(buttons_layout)



  def clear_display(self):
    '''Clear the text in display'''
    self.set_display_text('')



  def get_display_text(self):
    '''Get the text in display'''
    return self.display.text()

    

  def set_display_text(self, text):
    self.display.setText(text)
    self.display.setFocus()