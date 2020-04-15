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


'''
Algorithm - Postfix to Infix
1)Iterate from starting 
2)If opearend find push to stack
3)If operator find then pop two elements from stack and place operator in beteween operand
   operand1 = s.pop
   operand2 = s.pop
   result = operand2 + operator + operand1
4) push the resulted string to stack
5)return the last string which push back to stack
'''

def convert_postfix_to_infix(postfix_expression):
    s = Stack()
    operator = ['(', ')', '+', '*', '-', '/', '^']
    infix_expression = ""
    for char in postfix_expression:
        if char not in operator:
            s.push(char)
        else:
            operand1 = s.pop()
            operand2 = s.pop()
            infix_expression = str(operand2)+str(char)+str(operand1)
            s.push(infix_expression)
    return s.pop()

print(convert_postfix_to_infix("ABC/D*-E+"))


'''
Algorithm - Prefix to Infix
1)Iterate from Last
2)If opearend find push to stack
3)If operator find then pop two elements from stack and place operator in beteween operand
   operand1 = s.pop
   operand2 = s.pop
   result = operand1 + operator + operand2
4) push the resulted string to stack
5)return the last string which push back to stack
'''



def convert_prefix_to_infix(prefix_expression):
    s = Stack()
    operator = ['(', ')', '+', '*', '-', '/', '^']
    infix_expression = ""
    for char in prefix_expression[::-1]:
        if char not in operator:
            s.push(char)
        else:
            operand1 = s.pop()
            operand2 = s.pop()
            infix_expression = str(operand1)+str(char)+str(operand2)
            s.push(infix_expression)
    return s.pop()

print(convert_prefix_to_infix("+-A*/BCDE"))