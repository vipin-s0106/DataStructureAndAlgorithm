class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularArray:
    def __init__(self):
        self.head = None

    def enque(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            head_node = self.head
            temp = self.head
            while temp.next != head_node:
                temp = temp.next
            new_node.next = head_node
            temp.next = new_node
            self.head = new_node

    def deque(self):
        if self.head == None:
            print("Qeueu is Empty")
        else:
            head_node = self.head
            if head_node.next != head_node:
                temp = self.head.next
                prev = head_node
                while temp.next != head_node:
                    prev = temp
                    temp = temp.next
                prev.next = head_node
                return temp.data
            else:
                self.head = None
                return head_node.data

    def print_queue(self):
        if self.head == None:
            print("Qeueu is Empty")
        else:
            head_node = self.head
            print(head_node.data,end=" ")
            if head_node.next != head_node:
                temp = self.head.next
                while temp != head_node:
                    print(temp.data,end= " ")
                    temp = temp.next
            print("")

q = CircularArray()
q.enque(1)
q.enque(2)
q.enque(3)
q.print_queue()
q.deque()
q.print_queue()
q.deque()
q.print_queue()
q.deque()
q.print_queue()