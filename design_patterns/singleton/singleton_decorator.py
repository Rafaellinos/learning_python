"""
    singleton decorator em classes para
    garantir que haja sempre uma única instância daquela classe
"""


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:

    def __init__(self):
        print('loading database')


if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 == db2)
    print(id(db1))
    print(id(db2))
