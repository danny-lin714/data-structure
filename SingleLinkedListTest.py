import random

from SingleLinkedList import LinkedList
import unittest


class LinkedListTest(unittest.TestCase):
    def test_append(self):
        list = LinkedList()
        list.append(random.randint(0,100))
        self.assertTrue(list.head.data)
    def test_length(self):
        list=LinkedList()
        for i in range(10):
            list.append(i)
        self.assertEqual(list.length(),10)
    def test_index(self):
        list=LinkedList()
        for i in range(10):
            list.append(i)
        self.assertEqual(list.index(4),4)
    def test_remove(self):
        list=LinkedList()
        for i in range(10):
            list.append(i)
        list.remove(2)
        self.assertEqual(list.index(3),2)

