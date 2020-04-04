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

    #time complexity O(n)
    def remove_duplicates_from_sorted_list(self):
        temp = self.head
        prev = None
        while temp != None:
            if prev != None:
                if prev.data == temp.data:
                    current = temp
                    while current.data == prev.data:
                        current = current.next
                    prev.next = current
                    temp = current
                    continue
            prev = temp
            temp = temp.next

    #Hashing techniqe used here time complexity O(n)
    def remove_duplicates_from_unsorted_list(self):
        #hashing techiniqe used
        seen = set()
        temp = self.head
        prev = None
        while temp != None:
            if prev != None:
                if temp.data in seen:
                    prev.next = temp.next
                    prev = temp.next
                    temp = temp.next
                    continue
                else:
                    seen.add(temp.data)
            prev = temp
            temp = temp.next
            


l = Linkedlist()
l.add(1)
l.add(2)
l.add(3)
l.add(3)
l.add(4)
l.add(5)
l.add(5)
l.add(6)
l.print_list()
l.remove_duplicates_from_unsorted_list()
l.print_list()



