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
'''

t2 = Tree()
t2.root = Node(1)
t2.root.left = Node(2)
t2.root.right = Node(3)
t2.root.left.left = Node(4)
t2.root.left.right = Node(5)
t2.root.right.left = Node(6)   # here difference is created
t2.root.right.right = Node(7)

'''
           1 
         /   \ 
        2      3 
     /    \    /  \ 
   4      5   8     7
              ^
              |
              difference
'''

def isSame(root1,root2):
    if root1 == None and root2 == None:
        return True
    elif root1.data != root2.data:
        return False
    return isSame(root1.left,root2.left) and isSame(root1.right,root2.right)


print("Is Given two binary tree same - "+str(isSame(t1.root,t2.root)))