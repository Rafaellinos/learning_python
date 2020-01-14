class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat('Tom',3)
cat2 = Cat('Miau',5)
cat3 = Cat('Jean', 1)

def get_oldest_cat(*args):
    oldest = 0
    for cat in args:
        if cat.age > oldest:
            oldest = cat.age
    return oldest

print(f"the oldest cat is {get_oldest_cat(cat1,cat2,cat3)} years old")

