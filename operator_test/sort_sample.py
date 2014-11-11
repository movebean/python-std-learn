import operator
import collections

Item = collections.namedtuple("Item", "value")

a = Item(value = 1)
b = Item(value = 4)
c = Item(value = 3)
d = Item(value = 5)
e = Item(value = 2)

items = [a, b, c, d, e]
def cmpa(a, b):
  return 1 if operator.lt(a.value, b.value) else -1

keyFunc = operator.attrgetter("value")

items.sort(cmpa)
print items
items.sort(key=keyFunc)
print items
