from collections import deque


def contador(stop):
    cont = 1
    while cont <= stop:
        yield cont
        cont += 1


def contador_regressivo(start):
    while start >= 1:
        yield start
        start -= 1


class Scheduler:
    def __init__(self):
        self.queue = deque()

    def add_new(self, coro):
        self.queue.append(coro)

    def run(self):
        while self.queue:
            print(self.queue)

            task = self.queue.popleft() # remove o generator a esquerda
            try:
                result = next(task) # pega o next do generator da esquerda
                print(f'{task}: {result}')

                # self.queue.append(task) # joga o generator pra direta
            except StopIteration:
                ...


s = Scheduler()
s.add_new(contador(10))
s.add_new(contador_regressivo(15))
s.run()


