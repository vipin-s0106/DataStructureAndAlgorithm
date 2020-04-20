class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class Tree:

	def __init__(self):
		self.root = None

	def getRootToLeafSum(self,node,sum):
		if node == None and sum == 0:
			return True
		elif node == None and sum != 0:
			return False
		return self.getRootToLeafSum(node.left,sum-node.data) or self.getRootToLeafSum(node.right,sum-node.data)



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
just checking the given sum is available or not in the given trre from root to leaf
           1 
         /   \ 
        2      3 
     /    \    /  \ 
   4      5   6     7
                   /
                  8
   
   size = 7
'''
print(t1.getRootToLeafSum(t1.root,8))