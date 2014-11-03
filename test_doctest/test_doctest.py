import doctest

def Div2(x):
  '''
  >>> Div2(6)
  3.0
  >>> Div2(3)
  1.5
  '''
  return x * 1.0 / 2

if __name__ == '__main__':
  doctest.testmod()
