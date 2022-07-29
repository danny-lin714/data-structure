

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        if not isinstance(item, LinkedListNode):
            item = LinkedListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def length(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

    def output_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def index(self, goal):
        current = self.head
        count = 0

        while current is not None:
            if current.data == goal:
                return count
            else:
                count += 1
                current = current.next

    def remove(self, index):
        current = self.head
        previous = None
        count = 0
        while current is not None:
            if count == index:
                previous.next = current.next
                break
            else:
                count += 1
                previous = current
                current = current.next


List = LinkedList()
