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

    def reverse_linked_list(self):
        prev = None
        current = None
        fast = self.head
        while fast != None:
            current = fast
            fast = fast.next
            current.next = prev
            prev = current
        self.head = current

    def reverseLinkedList_recursion(self,prev,cur):
        if cur == None:
            return
        self.reverseLinkedList_recursion(cur,cur.next)
        if cur.next == None:
            self.head = cur
        cur.next = prev



l = Linkedlist()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(6)
l.print_list()
l.reverse_linked_list()
l.print_list()
l.reverseLinkedList_recursion(None,l.head)
l.print_list()



