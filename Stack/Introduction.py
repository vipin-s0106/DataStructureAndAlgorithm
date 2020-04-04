# implementation of Stack using Linkedlist

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


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.print_stack()
s.pop()
s.pop()
s.print_stack()
