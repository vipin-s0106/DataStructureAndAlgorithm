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
*****************
Infix to Postfix Conversion
*****************
1)Print Operands as they arrive
2) If stack is empty or contains a left pranthesis '(' on top , push the incoming operator
onto the stack
3)if incoming symbol is '(' push it onto the stack
4)if incoming symbol is ')' pop the stack & print the operator until left parenthsis is found
5)incoming symbol has higher precenddence then top of the stack, push it on the stack
6)incoming symbol has lower precenddence then top of the stack, pop and print the top
then test the incoming operator against the new top of the stack
7)if incoming opeartor has equal precendece witht he top of the stack use associative rule
8)at end of the exprression pop all opearator from stack and print it
9)associativity rule -
  L -> R then pop & print the top of the stack and then push the incoming opearator
  R -> L then push the incoming operator
  eg. 1) A-B/C*D+E  --->  ABC/D*-E+
      2) x^y/(5*z)+2   ---- > xy^5z*/2+
'''


def convert_Infix_to_Postfix(expression):
    postfix_expression = ""
    operand = ['(', ')', '+', '*', '-', '/', '^']
    associative_rule = {'+-': 'LR', '-+': 'LR', '*/': 'LR', '/*': 'LR', '^^': 'RL', '++': 'LR', '--': 'LR', '**': 'LR',
                        '//': 'LR'}
    precedence_piority = {'(': 4, ')': 4, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

    s = Stack()
    i = 0
    length = len(expression)
    while i < length:
        char = expression[i]
        if char in operand:
            if s.top == None:
                s.push(char)
                i += 1
                continue
            if s.top.data == "(":
                s.push(char)
            elif char == "(":
                s.push(char)
            elif char == ")":
                while s.top.data != '(':
                    ele = s.pop()
                    postfix_expression += ele
                s.pop()
            elif precedence_piority[char] > precedence_piority[s.top.data]:
                s.push(char)
            elif precedence_piority[char] < precedence_piority[s.top.data]:
                while precedence_piority[char] < precedence_piority[s.top.data]:
                    postfix_expression += s.pop()
                    if s.top == None:
                        break
                continue
            elif precedence_piority[char] == precedence_piority[s.top.data]:
                data = char + s.top.data
                rule = associative_rule[data]
                if rule == "LR":
                    postfix_expression += s.pop()
                    s.push(char)
                elif rule == "RL":
                    s.push(char)
        else:
            postfix_expression += char
        i += 1

    while s.top != None:
        postfix_expression += s.pop()

    return postfix_expression


print("Infix to Postfix - "+convert_Infix_to_Postfix("K+L-M*N+(O^P)*W/U/V*T+Q"))

'''
*****************
Infix to Prefix Conversion
*****************
0)First Reverse the expression
1)Print Operands as they arrive
2) If stack is empty or contains a left pranthesis ')' on top , push the incoming operator
onto the stack
3)if incoming symbol is ')' push it onto the stack
4)if incoming symbol is '(' pop the stack & print the operator until right parenthsis ')' is found
5)incoming symbol has higher precenddence then top of the stack, push it on the stack
6)incoming symbol has lower precenddence then top of the stack, pop and print the top
then test the incoming operator against the new top of the stack
7)if incoming opeartor has equal precendece witht he top of the stack use associative rule
8)at end of the exprression pop all opearator from stack and print it
9)associativity rule -
  L -> R then push the incoming operator
  R -> L then pop & print the top of the stack and then push the incoming opearator
10) Reverse the Final Result
  eg. 1) A-B/C*D+E  --->  +-A*/BCDE
      2) x^y/(5*z)+2   ---- > +/^xy*5z2
'''


def convert_Infix_to_Prefix(expression):
    expression = expression[::-1]
    prefix_expression = ""
    operand = ['(', ')', '+', '*', '-', '/', '^']
    associative_rule = {'+-': 'LR', '-+': 'LR', '*/': 'LR', '/*': 'LR', '^^': 'RL', '++': 'LR', '--': 'LR', '**': 'LR',
                        '//': 'LR'}
    precedence_piority = {'(': 4, ')': 4, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

    s = Stack()
    i = 0
    length = len(expression)
    while i < length:
        char = expression[i]
        if char in operand:
            if s.top == None:
                s.push(char)
                i += 1
                continue
            if s.top.data == ")":
                s.push(char)
            elif char == ")":
                s.push(char)
            elif char == "(":
                while s.top.data != ')':
                    ele = s.pop()
                    prefix_expression += ele
                s.pop()
            elif precedence_piority[char] > precedence_piority[s.top.data]:
                s.push(char)
            elif precedence_piority[char] < precedence_piority[s.top.data]:
                while precedence_piority[char] < precedence_piority[s.top.data]:
                    prefix_expression += s.pop()
                    if s.top == None:
                        break
                continue
            elif precedence_piority[char] == precedence_piority[s.top.data]:
                data = char + s.top.data
                rule = associative_rule[data]
                if rule == "LR":
                    s.push(char)
                elif rule == "RL":
                    prefix_expression += s.pop()
                    s.push(char)
        else:
            prefix_expression += char
        i += 1

    while s.top != None:
        prefix_expression += s.pop()

    return prefix_expression[::-1]


print("Infix to Prefix - "+convert_Infix_to_Prefix("K+L-M*N+(O^P)*W/U/V*T+Q"))

