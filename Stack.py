"""

implement:stack
operation:
    push
    pop
    isEmpty
    size
    peek
"""


class Stack:
    def __init__(self):
        self.element = []

    def push(self, data):
        self.element.append(data)

    def pop(self):
        if len(self.element) != 0:
            self.element.pop()
        else:
            None

stack = Stack()
print(stack.element)
