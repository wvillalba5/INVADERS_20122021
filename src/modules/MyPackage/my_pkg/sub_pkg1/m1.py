from importlib import resources
import my_pkg as p

def foo():
    print("from mod_1, you called foo()")
    print(p.init_data)

def print_lista():
    with resources.open_text('my_pkg.assets','lista.txt') as lista:
        print(lista.readlines())

class Foo:
    pass