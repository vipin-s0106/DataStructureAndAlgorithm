
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top == None:
            return "Stack is Empty"
        temp = self.top
        self.top = temp.next
        return temp.data

    def print_stack(self):
        if self.top == None:
            print("Stack is Empty")
        else:
            temp = self.top
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
            print("")


'''
Algorithm 
Maintain the Enque operation costly
and dequeue opearation O(1)

1) Maintain two stack to perform the Queue operation
2) during enque operation - 
pop element from stack1 and push to stack2
then push the new data to stack1
then pop element from stack2 ad push to stack1
so that the new data always be at last during poping from stack1
3) during deque operation - 
directly pop the element from stack1
'''

class Q:

     def __init__(self):
         self.stack1 = Stack()
         self.stack2 = Stack()

     # time complexity n+n but here highest order of n is 1 so O(n)
     def enque(self,data):
         if self.stack1.top == None:
             self.stack1.push(data)
         else:
             temp = self.stack1.top
             while temp != None:
                 self.stack2.push(self.stack1.pop())
                 temp = temp.next

             self.stack1.push(data)

             temp = self.stack2.top
             while temp != None:
                 self.stack1.push(self.stack2.pop())
                 temp = temp.next

     #time complexity is O(1)
     def deque(self):
         if self.stack1.top == None:
             print("Queue is Empty")
         else:
             return self.stack1.pop()


     def print_queue(self):
         temp = self.stack1.top
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
q.deque()
q.print_queue()
