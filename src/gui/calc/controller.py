from functools import partial
'''functools.partial(func, /, *args, **keywords)'''
from model import ERROR_MSG

class Controller:
  ''''The CONTROLLER is the connector between  the VIEW and MODEL  '''

  def __init__(self, view, model):
    '''Recibe the VIEW and MODEL'''
    self.__view = view
    self.__model = model
    ''' Function to connect all signals'''
    self.__connect_signals()

  def __connect_signals(self):
    '''Recorre all buttons and connect the clicked with slots'''
    '''The C button is connected to slot that clear the display'''
    self.__view.buttons['C'].clicked.connect(self.__view.clear_display)
    
    '''The = key is connected with privated function __calc_result '''
    self.__view.buttons['='].clicked.connect(self.__calc_result)

    '''The for Recorre the buttons dictionary placed in VIEW'''
    for text, button in self.__view.buttons.items():
      if text not in{'=', 'C'}:
        '''With a click connect the text expresion of button with private function __built_expr'''
        '''functools.partial(func, /, *args, **keywords)'''
        button.clicked.connect(partial(self.__build_expr, text))

    ''''This signal is emitted when the Return or Enter key is pressed and calculate the result.'''
    self.__view.display.returnPressed.connect(self.__calc_result)
    

  def __calc_result(self):
    # print('Inside __calc')
    '''Call to MODEL and its fuction "eval_expression" and recibe the expresion of display'''
    result = self.__model.eval_expression(self.__view.get_display_text())
    self.__view.set_display_text(result)

  def __build_expr(self, text):
    #  print(f'inside __build_exp = {text}')
    
    if self.__view.get_display_text() == ERROR_MSG:
      '''if there is any mistake, first Clear the screen'''
      self.__view.clear_display()
    '''Build the expresion create by clicked buttons and show in display'''
    self.__view.set_display_text(self.__view.get_display_text() + text)
    