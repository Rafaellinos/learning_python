from collections import namedtuple


Person = namedtuple('Person', 'first_name last_name zip_code')

p1 = Person('Joe', 'Schmoe', '93002')

Car = namedtuple('Car', ['color', 'year'])


car1 = Car('blue', 'year')

print(car1.color)