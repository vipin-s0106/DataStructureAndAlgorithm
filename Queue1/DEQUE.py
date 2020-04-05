#Double Ended Queue
'''
Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends.
Operations on Deque:
Mainly the following four basic operations are performed on queue:

insertFront(): Adds an item at the front of Deque.
insertLast(): Adds an item at the rear of Deque.
deleteFront(): Deletes an item from front of Deque.
deleteLast(): Deletes an item from rear of Deque.

It can be used as Stack or Queue -
Stack - insertFront,DeleteFront
Queue - insertFront,deleteLast
'''

#Implementation Using Doubly Linkedlist

class Node:
    def __init__(self,data):
        self.data = data
        self.left_next = None
        self.right_next = None

class Deque:

    def __init__(self):
        self.last_head = None
        self.front_head = None

    def insertFront(self,data):
        new_node = Node(data)
        if self.front_head == None:
            self.front_head = new_node
            self.last_head = new_node
        else:
            new_node.right_next = self.front_head
            self.front_head.left_next = new_node
            self.front_head = new_node

    def insertLast(self,data):
        new_node = Node(data)
        if self.last_head == None:
            self.front_head = new_node
            self.last_head = new_node
        else:
            new_node.left_next = self.last_head
            self.last_head.right_next = new_node
            self.last_head = new_node

    def deleteFront(self):
        if self.front_head == None:
            print("Dqueue is Empty")
        else:
            temp = self.front_head
            self.front_head = self.front_head.right_next
            self.front_head.left_next = None
            return temp.data

    def deleteLast(self):
        if self.last_head == None:
            print("Dqueue is Empty")
        else:
            temp = self.last_head
            self.last_head = self.last_head.left_next
            self.last_head.right_next = None
            return temp.data

    def print_deque_from_front(self):
        temp = self.front_head
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.right_next
        print("")


    def print_deque_from_last(self):
        temp = self.last_head
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.left_next
        print("")


d = Deque()
d.insertFront(1)
d.insertLast(2)
d.insertFront(3)
d.insertLast(4)
d.insertFront(5)
d.insertLast(6)
d.print_deque_from_front()
d.deleteFront()
d.print_deque_from_front()
d.deleteLast()
d.print_deque_from_front()
print("Print from last")
d.print_deque_from_last()

