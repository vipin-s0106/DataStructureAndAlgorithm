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
            return
        temp = self.top
        self.top = temp.next
        return temp.data

'''
Algorithm - 
1) Iterate the Expression char one by one
2) if operand find push into the stack
3) if operator find pop two element from stack evalate based on the operand and push the result to stack
'''

def evalaute_postfix_expression(postfix_expression):
    s = Stack()
    operator = ['(',')','+','-','*','/','^']
    for char in postfix_expression:
        if char not in operator:
            s.push(char)
        else:
            operand1 = s.pop()
            operand2 = s.pop()
            result = eval(str(operand2)+str(char)+str(operand1))
            s.push(result)
    return s.pop()

print(evalaute_postfix_expression("231*+9-"))


'''
Algorithm
1) iteratate the expression from last element
2) if operand find push into the stack
3) if operator find pop two element from stack evalate based on the operand and push the result to stack
'''


def evalaute_prefix_expression(prefix_expression):
    s = Stack()
    operator = ['(',')','+','-','*','/','^']
    prefix_expression = prefix_expression.split(' ')
    for index in range(len(prefix_expression)-1,-1,-1):
        char = prefix_expression[index]
        if char not in operator:
            s.push(char)
        else:
            operand1 = s.pop()
            operand2 = s.pop()
            if char == "^":
                char = "**"
            result = eval(str(operand1)+str(char)+str(operand2))
            s.push(result)
    return round(s.pop())

print(evalaute_prefix_expression("- + 2 * 3 4 / 16 ^ 2 3"))