from Stack import Stack
import unittest


class StackTest(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertTrue(bool(stack.element))

    def test_pop(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        stack.pop()
        self.assertTrue(len(stack.element) == 4)

    def test_size(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        self.assertTrue(stack.size() == 5)

    def test_peek(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.peek(), 4)

    def test_empty(self):
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.empty())
