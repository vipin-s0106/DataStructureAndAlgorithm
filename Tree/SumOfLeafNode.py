class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


class BST:
	def __init__(self):
		self.root = None

	def sumOfLeafNode(self,node):
		pass

'''
           20 
         /   \ 
        10      30 
     /    \    /  \ 
   5      15  25    35

'''
t1 = BST()
t1.root = Node(20)
t1.root.left = Node(10)
t1.root.right = Node(30)
t1.root.left.left = Node(5)
t1.root.left.right = Node(15)
t1.root.right.left = Node(25)
t1.root.right.right = Node(35)