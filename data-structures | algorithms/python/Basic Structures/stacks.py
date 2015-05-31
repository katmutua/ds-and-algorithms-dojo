class Stacks:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        return True if len(self.items) > 0 else False

    def peek(self):
        return self.items(len(self.items) - 1)

    def size(self):
        return len(self.items)