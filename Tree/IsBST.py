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

	def checkIsBST(self,node,upper,lower):
		if node == None:
                        return True
                if node.data <= lower or node.data >= upper:
                        return False
                return check_tree(node.left,node.data,lower) and check_tree(node.right,upper,node.data)


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
print(t1.checkIsBST(t1.root,100000,-100000))
