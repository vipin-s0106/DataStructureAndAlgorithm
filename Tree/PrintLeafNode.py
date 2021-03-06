class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class Tree:

	def __init__(self):
		self.root = None

	def inorder_traversal(self,root):
		if root == None:
			return
		self.inorder_traversal(root.left)
		print(root.data,end=" ")
		self.inorder_traversal(root.right)

	def printLeafNode(self,node):
		if node == None:
			return
		if node.left == None and node.right == None:
			print(node.data,end=" ")
			return None
		self.printLeafNode(node.left)
		self.printLeafNode(node.right)



t1 = Tree()
t1.root = Node(1)
t1.root.left = Node(2)
t1.root.right = Node(3)
t1.root.left.left = Node(4)
t1.root.left.right = Node(5)
t1.root.right.left = Node(6)
t1.root.right.right = Node(7)
t1.root.right.right.left = Node(8)

'''
           1 
         /   \ 
        2      3 
     /    \    /  \ 
   4      5   6     7
                   /
                  8

'''

t1.printLeafNode(t1.root)