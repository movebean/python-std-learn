import pickle

class TestCls(object):
  def __init__(self, a):
    self.a = a

f = open("output.txt", "rb")
ftp = pickle.load(f)
a = pickle.load(f)

print ftp
print a
