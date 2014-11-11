import collections

Person = collections.namedtuple('Person', 'name age gender')
print 'Type of Person:', type(Person)

bob = Person(name = 'Bob', age = 30, gender = 'male')
print "Representation:", bob

jane = Person(name = "Jane", age = 29, gender = 'female')
print 'Field by Name:', jane.name

for people in [bob, jane]:
  print '%s is %d years old %s' % people
