class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat('Tom',3)
cat2 = Cat('Miau',5)
cat3 = Cat('Jean', 1)

def get_oldest_cat(*args):
    cat_old = args[0]
    for i,cat in enumerate(args):
        if cat.age > cat_old.age:
            cat_old = args[i]

    return cat_old.age, cat_old.name

old_age, old_name = get_oldest_cat(cat1,cat2,cat3)
print(f"the oldest cat name is {old_name} and has {old_age} years old")

