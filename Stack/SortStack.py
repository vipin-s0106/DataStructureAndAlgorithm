class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self):
		self.top = None

	def push(self, data):
		new_node = Node(data)
		if self.top == None:
			self.top = new_node
		else:
			new_node.next = self.top
			self.top = new_node

	def pop(self):
		if self.top == None:
			return "Stack is Empty"
		temp = self.top
		self.top = temp.next
		return temp.data

	def print_stack(self):
		if self.top == None:
			print("Stack is Empty")
		else:
			temp = self.top
			while temp != None:
				print(temp.data, end=" ")
				temp = temp.next
			print("")

s = Stack()
s.push(1)
s.push(2)
s.push(5)
s.push(4)
s.push(3)
print("Before Sorting")
s.print_stack()

class Q:
	def __init__(self):
		self.end = None

	def enque(self,data):
		new_node = Node(data)
		if (self.end == None):
			self.end = new_node
		else:
			new_node.next = self.end
			self.end = new_node

	def deque(self):
		if self.end == None:
			print("Queue is Empty")
		elif self.end.next == None:
			data = self.end.data
			self.end =self.end.next
			return  data
		else:
			prev = self.end
			cur = self.end.next
			while cur.next != None:
				prev = cur
				cur = cur.next
			prev.next = None
			return cur.data
'''
Algorithm
1) pop the top element from main Stack push to other stack
2) then start poping element from main stack and get compare with top element of the other stack if it found less than current then pop the other stack element enque
into queue and push the element which is greater to that other stack
3)deque all the elemts from queue and push to main stack
4)at last change the referece of other stack with main stack
'''

def sort_stack(s):
	s1 = Stack()
	q = Q()
	while s.top != None:
		s1.push(s.pop())
		while s.top != None:
			ele = s.pop()
			if ele > s1.top.data:
				q.enque(s1.pop())
				s1.push(ele)
			else:
				q.enque(ele)
		while q.end != None:
			s.push(q.deque())
	s = s1
	return s
s = sort_stack(s)
print("After Sorting")
s.print_stack()