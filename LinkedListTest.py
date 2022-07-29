import LinkedList
import unittest


class LinkedListTest(unittest.TestCase):
    def test_append(self):
        list = LinkedList()
        list.append(1)
        self.assertTrue(list.head.data)
