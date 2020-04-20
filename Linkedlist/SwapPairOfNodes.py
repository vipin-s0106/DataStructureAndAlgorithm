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

	def print_list(self):
		temp = self.head
		while (temp != None):
			print(temp.data, end=" ")
			temp = temp.next
		print("")

	def swap_pair_of_nodes(self):
		prev = None
		cur = None
		fast = self.head
		while fast != None:
			cur = fast
			fast = fast.next
			if fast == None:
				break
			cur.next = fast.next
			fast.next = cur
			if prev != None:
				prev.next = fast
			if cur == self.head:
				self.head = fast
			prev = cur
			fast = cur.next



l = Linkedlist()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
print("Before Swapping")
l.print_list()
print("After Swapping Pair of nodes")
l.swap_pair_of_nodes()
l.print_list()