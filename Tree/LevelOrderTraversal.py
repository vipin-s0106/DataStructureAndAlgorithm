'''
Level Order Traversal
1) print the node value
2) check left node is not None then again call the same function
3) check right node is not None then again call the same function
4)
'''

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class Tree:

	def __init__(self):
		self.root = None

	def getHeightTree(self,node):
		if node == None:
			return 0
		return 1 + max(self.getHeightTree(node.left) ,self.getHeightTree(node.right))

	def level_order_traversal(self,node):
		height = self.getHeightTree(node)
		for i in range(1,height+1):
			self.printing_level(node,i)



	def printing_level(self,node,level):
		if node == None:
			return
		if level == 1:
			print(node.data,end=" ")
		else:
			self.printing_level(node.left,level-1)
			self.printing_level(node.right,level-1)

t1 = Tree()
t1.root = Node(1)
t1.root.left = Node(2)
t1.root.right = Node(3)
t1.root.left.left = Node(4)
t1.root.left.right = Node(5)
t1.root.right.left = Node(6)
t1.root.right.right = Node(7)
'''
           1 
         /   \ 
        2      3 
     /    \    /  \ 
   4      5   6     7
   
   size = 7
'''
t1.level_order_traversal(t1.root)
