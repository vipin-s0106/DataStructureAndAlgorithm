import copy
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

    def check_linkedlist_palindrome(self):
        length = self.linkedlist_length()  # N/2
        mid = length // 2 + 1
        temp = self.head
        count = 1
        while count != mid:                # N/2
            temp = temp.next
            count += 1
        # if length % 2 != 0:
        #     temp = temp.next
        l2 = Linkedlist()
        while temp != None:                #N/2
            l2.add(temp.data)
            temp = temp.next
        l2.reverse_linked_list()           #N/2
        temp = self.head
        temp1 = l2.head
        while temp1 != None:               #N/2
            if temp.data != temp1.data:
                return False
            temp1 = temp1.next
            temp = temp.next
        return True

    #Comlexity = N+N+N/2 = 5/2 N

    '''
    def checkPalindrom(self,node):
        temp = self.head
        temp1 = node
        if temp1 == None:
            return
        self.checkPalindrom_recursion(node.next)
        if temp1.data == temp.data:
            temp = temp.next
            return
        else:
            temp = temp.next
            return False
    '''

    def form_reverse_linkedlist(self,l2,node):
        if node == None:
            return
        self.form_reverse_linkedlist(l2,node.next)
        l2.add(node.data)
        return


    def CheckPalindrome(self):
        l2 = Linkedlist()
        self.form_reverse_linkedlist(l2,self.head)
        temp = self.head
        temp1 = l2.head
        while temp != None:
            if temp.data != temp1.data:
                return False
            temp = temp.next
            temp1= temp1.next
        return True

    #Complexity = 2N







l = Linkedlist()
l.add(1)
l.add(3)
l.add(5)
l.add(3)
l.add(1)
print("Original List - ",end=" ")
l.print_list()

print(l.check_linkedlist_palindrome())
print(l.CheckPalindrome())




