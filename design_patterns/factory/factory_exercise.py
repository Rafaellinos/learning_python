class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    index = -1

    def create_person(self, name):
        self.index += 1
        return Person(self.index, name)


if __name__ == '__main__':
    pf = PersonFactory()
    p = pf.create_person('Rafael')
    print(p.id)
    p1 = pf.create_person('João')
    print(p1.id)
    p2 = pf.create_person('Maria')
    print(p2.id)
