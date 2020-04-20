class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


class BST:
	def __init__(self):
		self.root = None

	def insert(self,data):
		if self.root == None:
			new_node = Node(data)
			self.root = new_node
			return
		else:
			prev = None
			temp = self.root
			while temp != None:
				if data < temp.data:
					prev = temp
					temp = temp.left
				else:
					prev = temp
					temp = temp.right
			if data < prev.data:
				prev.left = Node(data)
			else:
				prev.right = Node(data)

	def checkIsBST(self,prev,cur):
		if cur == None:
			return
		if cur.left != None or cur.right != None:
			return self.checkIsBST(cur,cur.left) and self.checkIsBST(cur,cur.right)
		else:
			if prev.left == cur:
				if cur.data < prev.data:
					return True
				else:
					return False
			else:
				if cur.data > prev.data:
					return True
				else:
					return False


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
print(t1.checkIsBST(None,t1.root))