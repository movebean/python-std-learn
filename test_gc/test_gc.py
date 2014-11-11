import gc
import inspect

gc.set_debug(gc.DEBUG_LEAK)

class T(object):

  def set(self, b):
    self.t = b

def Test():
  a = T()
  b = T()
  c = T()
  b = [c]
  a.set(b)
  c.set(a)
  print a
  print b
  print c

Test()
gc.disable()
gc.collect()
TIMES = 2

def getCircle(tar):
  def _inner(tar, gar = None, index = 0):
    if gar == tar:
      return [('end', 'find')]
    if index > TIMES:
      return
    if gar:
      res = [gar]
    else:
      res = [tar]

    for obj in res:
      subres = []
      if hasattr(obj, '__dict__'):
        subres.extend(obj.__dict__.items())
      for attr in gc.get_referents(obj):
        item = ('mem', attr)
        subres.append(item)

      for key, y in subres:
        if inspect.isbuiltin(y):
          continue
        tmp = _inner(tar, y, index + 1)
        if tmp:
          tmp.append((key, y))
          return tmp
    return []
  res = _inner(tar)
  res.reverse()
  return res

for obj in gc.garbage:
  if isinstance(obj, T):
    print 'origin', obj
    print 'result', getCircle(obj)
