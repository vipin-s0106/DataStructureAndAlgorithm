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
	recursion value
	'''
	def print_list_in_reverse(self,node):
		if node == None:
			return
		self.print_list_in_reverse(node.next)
		print(node.data,end=" ")
		return



l = Linkedlist()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.print_list()
l.print_list_in_reverse(l.head)