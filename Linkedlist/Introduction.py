class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = new_node

    def insert(self, data, index):
        new_node = Node(data)
        temp = self.head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        if temp == None and index > 0:
            print('Invalid Index Number')
        else:
            i = 0
            while i != index - 1 and temp != None:
                temp = temp.next
                i = i + 1
            if temp != None:
                new_node.next = temp.next
                temp.next = new_node
            else:
                print("Invalid Index Number - ", index)

    def delete(self, index):
        i = 0
        temp = self.head
        if index == 0:
            self.head = temp.next
            return
        while (temp.next != None and i < index - 1):
            temp = temp.next
            i += 1
        if temp.next != None:
            temp.next = temp.next.next
        else:
            print("Invalid index number to delete")

    def delete_by_given_key(self, key):
        prev = None
        temp = self.head
        if temp == None:
            return "Linked list is empty"
        if temp.data == key:
            self.head = temp.next
            return
        while temp != None:
            if temp.data == key:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
        return str(key) + " Key not found in the linked list"

    def print_list(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end=" ")
            temp = temp.next
        print("")

    def delete_the_linked_list(self):
        temp = self.head
        next = temp
        while temp != None:
            next = temp.next
            del temp.data
            temp = next

    def linkedlist_length(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    # recursion seraching a element in linkedlist
    def find_element(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.find_element(node.next, data)


l = Linkedlist()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(6)
l.print_list()
l.insert(5, 0)

l.print_list()
l.delete(2)
l.print_list()
l.delete_by_given_key(5)
l.print_list()
print("length of linked list " + str(l.linkedlist_length()))
print(l.find_element(l.head, 6))
