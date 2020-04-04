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
           print("Queue is Empty")
       elif self.end.next == None:
           return  self.end.data
           self.end = None
       else:
           prev = self.end
           cur = self.end.next
           while cur.next != None:
               prev = cur
               cur = cur.next
           prev.next = None
           return cur.data


    def print_queue(self):
        temp = self.end
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next
        print("")


q = Q()
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)
q.print_queue()
q.deque()
q.print_queue()
q.enque(6)
q.print_queue()
q.deque()
q.print_queue()