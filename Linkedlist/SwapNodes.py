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

    '''
    1 -> 2 -> 3 -> 4
    '''
    def swap_nodes(self,node_no1,node_no2):
        temp = self.head
        if temp.next == None or temp == None:
            print("Swapping Not Possible less element in list")
            return
        count = 1
        if node_no1 == 1 and temp.next != None:
            temp2 = temp.next
            temp3 = temp2.next
            temp2.next = temp
            temp.next = temp3
            self.head = temp2
            return
        while count < (node_no1-1) and temp.next != None:
            temp = temp.next
            count += 1
        if temp.next != None or count == node_no1-1:
            temp1 = temp.next
            if temp1.next == None:
                print("Swapping Not Possible less element in list")
                return
            temp2 = temp1.next
            temp1.next = temp1.next.next
            temp.next = temp2
            temp2.next = temp1
            return
        else:
            print("Swapping Not Possible less element in list")
            return




l = Linkedlist()
l.add(1)
l.add(2)
l.print_list()
l.swap_nodes(1,2)
l.print_list()