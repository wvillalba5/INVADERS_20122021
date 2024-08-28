ERROR_MSG = 'ERR'

class Model:

  def __init__(self):
    pass

  def eval_expression(self, expression):
    "Get the math expresion of the display and eval it"
    try:
      '''Control of errors for example if there is /0 or other mistake'''
      result = str(eval(expression, {}, {}))

      '''eval(expression, {globals}, {locals}) ==> Take care with EVAL since any text expresion with malware or virus or any expresion of internet
      could be evaluated with this.'''
    except Exception:
      result = ERROR_MSG

    return result