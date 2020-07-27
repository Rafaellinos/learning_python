"""
Single Reponsibility Principle:
SRP - SOC

Class must have a single responsible only.
"""
"""
Anti - Patter 

GOD Object:
    all the things in the same obj
"""

class Journal:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]
        self.count -= 1

    def __str__(self):
        return '\n'.join(self.entries)

    # Bad pratice below. You are adding
    # the responsability to save and load the journal
    # def save(self, filename):
    #     with open(filename, 'w') as f:
    #         f.write(str(self))
    #
    # def load(self, filename):
    #     pass
    #
    # def low_from_web(self, uri):
    #     pass


class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as f:
            f.write(str(journal))


j = Journal()
j.add_entry('I cried')
j.add_entry('I ate a bug')

print(j)

file = '/tmp/journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file, 'r') as f:
    print(f.read())
