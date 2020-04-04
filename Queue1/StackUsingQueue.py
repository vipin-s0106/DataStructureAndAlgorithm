
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Q:
    def __init__(self):
        self.end = None

    def enque(self,data):
        new_node = Node(data)
        if (self.end == None):
            self.end = new_node
        else:
            new_node.next = self.end
            self.end = new_node

    def deque(self):
       if self.end == None:
           return
       elif self.end.next == None:
           data = self.end.data
           self.end = None
           return  data

       else:
           prev = self.end
           cur = self.end.next
           while cur.next != None:
               prev = cur
               cur = cur.next
           prev.next = None
           return cur.data



class Stack:

    def __init__(self):
        self.q1 = Q()
        self.q2 = Q()

    def push(self,data):
        if self.q1.end == None:
            self.q1.enque(data)
        else:
            self.q2.enque(data)
            while self.q1.end != None:
                self.q2.enque(self.q1.deque())
            temp = self.q1
            self.q1 = self.q2
            self.q2 = temp

    def pop(self):
        if self.q1.end == None:
            return
        else:
            return self.q1.deque()

    def print_stack(self):
        temp = self.q1.end
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next
        print("")


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.print_stack()
s.pop()
s.pop()
s.print_stack()
s.push(4)
s.print_stack()
