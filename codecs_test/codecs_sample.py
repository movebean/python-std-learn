#-*- coding: utf-8 -*-

import codecs

c = codecs.lookup('gbk')
f = open('sample.txt', 'rb')
if c:
  res, _ = c.encode(u'另外建')
  res, _ = c.decode(res)
  print res

  fp = c.streamreader(f)
  print fp.read()

c = codecs.lookup('gbk')
f = open('sample2.txt', 'wb')
if c:
  fp = c.streamwriter(f)
  fp.write(u'另外建')
  f.close()

  f2 = open("sample2.txt", 'rb')
  fp2 = c.streamreader(f2)
  print fp2.read()
