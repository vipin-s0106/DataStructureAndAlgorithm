'''
Design a stack that supports getMin() in O(1) time and O(1) extra space
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.aux_top = None

    def push(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
            self.aux_top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

            #adding the element to aux stack for getmin operation in O(1) operation
            new_node1 = Node(data)
            if new_node1.data < self.aux_top.data:
                new_node1.next = self.aux_top
                self.aux_top = new_node1
            else:
                aux_node = Node(self.aux_top.data)
                aux_node.next = self.aux_top
                self.aux_top = aux_node

    def pop(self):
        if self.top == None:
            return "Stack is Empty"
        temp = self.top
        self.top = temp.next
        aux_node = self.aux_top
        self.aux_top = aux_node.next
        return temp.data


    def getMin(self):
        if self.aux_top == None:
            print("Stack is Empty")
        else:
            return self.aux_top.data

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
s.push(4)
s.push(7)
s.push(3)
s.push(8)
s.push(1)
s.print_stack()
print(s.getMin())
s.pop()
s.print_stack()
print(s.getMin())
s.pop()
s.print_stack()
print(s.getMin())
