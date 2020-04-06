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
            return None
        temp = self.top
        self.top = temp.next
        return temp.data


def check_parenthisi(expression):
    s = Stack()
    parenthisis = {"(":")","{":"}","[":"]"}
    for char in expression:
        if char in parenthisis:
            s.push(char)
        else:
            ele = s.pop()
            if ele == None:
                return False
            else:
                if parenthisis[ele] == char:
                    continue
                else:
                    return False
    return True

print(check_parenthisi("{}[]"))
print(check_parenthisi("{([])}"))
print(check_parenthisi("}{"))
print(check_parenthisi("]({{"))
print(check_parenthisi("{(})"))