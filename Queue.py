"""
implement:queue
operation:
    add
    delete
    front
    empty
    size
    peek
    clear
"""


class Queue:

    def __init__(self):
        self.element = []

    def add(self, data):
        self.element.insert(0, data)

    def delete(self):
        if len(self.element) >= 1:
            self.element.pop()
        else:
            return "You don't have any data!!!"

    def front(self):
        if len(self.element) >= 1:
            return self.element[-1]
        else:
            return "You don't have any data!!!"

    def size(self):
        return len(self.element)

    def empty(self):
        return not bool(len(self.element))

    def clear(self):
        self.element = []


queue=Queue()
print(queue.size())
