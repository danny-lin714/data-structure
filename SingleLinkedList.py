import unittest

class linked_list_node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,item):
        if not isinstance(item,linked_list_node):
            item=linked_list_node(item)
        if self.head==None:
            self.head=item
        else:
            self.tail.next=item
        self.tail=item

    def length(self):
        current = self.head
        length=0
        while current != None:
            length+=1
            current = current.next
        return length

    def output_list(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next

    def index(self,goal):
        current = self.head
        count=0
        while current!=None:
            if current.data==goal:
                return(count)
            else:
                count+=1
                current=current.next
    def remove(self,index):
        current = self.head
        previous=None
        count = 0
        while current!=None:
            if count==index:
                previous.next=current.next
                break
            else:
                count += 1
                previous=current
                current=current.next

list=LinkedList()
