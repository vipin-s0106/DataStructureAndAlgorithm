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

    def form_loop(self):
        temp = self.head
        loop_node = None
        while temp.next != None:
            if temp.data == 2:
                loop_node = temp
            temp = temp.next
        temp.next = loop_node

    #way 1 to detect the loop hashing techniqe used due to set  O(n)
    def detect_loop(self):
        node_list = set()
        temp = self.head
        while temp not in node_list and temp != None:
            node_list.add(temp)
            temp = temp.next

        if temp != None:
            return True
        return False

    #way 2 to detect the loop Floyd Algorithm   O(n)
    def detect_loop1(self):
        prev = self.head
        temp = self.head
        while prev != None and temp != None and temp.next != None:
            prev = prev.next
            temp = temp.next.next
            if prev == temp:
                return True
        return False

    def find_length_of_loop(self):
        prev = self.head
        temp = self.head
        while prev != None and temp != None and temp.next != None:
            prev = prev.next
            temp = temp.next.next
            if prev == temp:
                current = temp.next
                count = 1
                while prev != current:
                    count += 1
                    current = current.next
                return count
        return False


l = Linkedlist()
l.add(1)
l.add(2)
l.add(3)
l.add(5)
l.add(6)
l.add(7)
l.add(8)
l.form_loop()
print(l.detect_loop1())
print(l.find_length_of_loop())


