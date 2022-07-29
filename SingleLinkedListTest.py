import random
from SingleLinkedList import LinkedList
import unittest


class LinkedListTest(unittest.TestCase):

    def test_append(self):
        linkedlist = LinkedList()
        linkedlist.append(random.randint(0, 100))
        self.assertTrue(linkedlist.head.data)

    def test_length(self):
        linkedlist = LinkedList()
        for i in range(10):
            linkedlist.append(i)
        self.assertEqual(linkedlist.length(), 10)

    def test_index(self):
        linkedlist = LinkedList()
        for i in range(10):
            linkedlist.append(i)
        self.assertEqual(linkedlist.index(4), 4)

    def test_remove(self):
        linkedlist = LinkedList()
        for i in range(10):
            linkedlist.append(i)
        linkedlist.remove(2)
        self.assertEqual(linkedlist.index(3), 2)
