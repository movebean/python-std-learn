import inspect
import gevent

def TestFunc(a, b, c=1, *args, **kargs):
  print inspect.getargvalues(inspect.currentframe())
  pass

print inspect.getargspec(TestFunc)

TestFunc(1, 2)
print inspect.getfile(gevent)
print inspect.getmembers(TestFunc)
print inspect.getmodule(TestFunc)
print inspect.getmoduleinfo(inspect.getfile(gevent))
print inspect.getmodulename(inspect.getfile(gevent))
print inspect.getmro(TestFunc.__class__)
print inspect.getsourcefile(gevent.spawn)
print inspect.getsourcelines(gevent.spawn)
print ''.join([str(line) for line in inspect.getsourcelines(gevent.spawn)[0]])
print inspect.getsource(gevent.spawn)
