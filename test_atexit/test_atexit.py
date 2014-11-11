import atexit

def Raise2(i):
  raise RuntimeError(i)

def Raise1(i):
  raise RuntimeError(i)

atexit.register(Raise1, 1)
atexit.register(Raise2, 2)
