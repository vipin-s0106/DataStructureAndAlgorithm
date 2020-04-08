class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = new_node

    def print_list(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end=" ")
            temp = temp.next
        print("")

    def linkedlist_length(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def getNodeValueFromTail(self,index_position):
        length = self.linkedlist_length()
        if index_position >= length:
            return None
        index_position = length - index_position -1
        temp = self.head
        i = 0
        while index_position != i:
            temp = temp.next
            i += 1
        return temp.data



l = Linkedlist()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.print_list()
print("Value - ",l.getNodeValueFromTail(0))

