import random
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0 , item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class RandomQueue:

    def __init__(self, names_list):
        self.queue = Queue()
        for item in names_list:
            self.queue.enqueue(item)

    def randomize(self):
        if self.queue:
            return random.randint(0, (self.queue.size() - 1))

names_list = ['RZA', 'GZA', 'ODB','BK']
random_queue = RandomQueue(names_list)

while len(random_queue.queue.items) > 1:
        for i in range(random_queue.randomize()):
            random_queue.queue.enqueue(random_queue.queue.dequeue())
        random_queue.queue.dequeue()

print random_queue.queue.items

