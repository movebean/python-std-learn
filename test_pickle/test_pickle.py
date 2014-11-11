import pickle
import gevent
from ftplib import FTP

class TestCls(object):
  def __init__(self, a):
    self.a = a

ftp = FTP()
f = open('output.txt', 'wb')
pickle.dump(ftp, f)

a = TestCls(2)
pickle.dump(a, f)

f.close()
