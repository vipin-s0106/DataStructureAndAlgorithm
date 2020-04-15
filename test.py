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
			return False
		else:
			prev = None
			temp = self.head
			while (temp.next != None):
				prev = temp
				temp = temp.next
			if temp == self.head and temp.data < data:
				new_node.next = temp.next
				self.head = new_node
				return True
			elif temp.data < data:
				prev.next = new_node
				return True
			else:
				temp.next = new_node
				return False
	def print_list(self):
		temp = self.head
		while (temp != None):
			print(temp.data, end=" ")
			temp = temp.next
		print("")

T = int(input())
for j in range(T):
	l = Linkedlist()
	arr1 = input().split(' ')
	N = int(arr1[0])
	K = int(arr1[1])
	arr = input().split(' ')
	for num in arr:
		flag = l.add(int(num))
		if flag == True:
			K = K -1
	while K != 0:
		temp = l.head
		prev = None
		flag = False
		while temp.next != None:
			if temp.next.next != None:
				if temp.data < temp.next.data:
					if prev == None:
						l.head = temp.next.next
					else:
						temp.next = temp.next.next
					K =K-1
					flag = True
					break
			prev = temp
			temp = temp.next
		if flag == False:
			prev.next = None
			K = K -1

	l.print_list()
