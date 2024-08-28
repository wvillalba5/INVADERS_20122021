import factorial


numbers = [1,2,3]
a = 30

def add(x,y):
  return x + y

class Foo:
  pass

print(f"__name__ = {__name__}")

if __name__ == '__main__':
  print(f"Root Number = {a}")
  print(f"Number List = {numbers}")
  print(f"Adding both = {[add(a, number) for number in numbers]}")
  print(factorial.fact(3))