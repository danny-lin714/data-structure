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

    def push(self, data) -> None:
        self.element.append(data)

    def pop(self) -> None:
        if len(self.element) != 0:
            self.element.pop()

    def size(self) -> int:
        return len(self.element)

    def peek(self) -> (int, str, bool, float, list, set, dict, tuple):
        return self.element[-1]

    def empty(self) -> bool:
        return not bool(self.element)


stack = Stack()
