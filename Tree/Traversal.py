#===================================================
#              Depth First Traversals
#==================================================


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

    def preorder_traversal(self,root):
        if root == None:
            return
        print(root.data, end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)


    def postorder_traversal(self,root):
        if root == None:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.data, end=" ")


t = Tree()
t.root = Node(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.left.right = Node(5)
t.root.right.left = Node(6)
t.root.right.right = Node(7)

'''
           1 
         /   \ 
        2      3 
     /    \    /  \ 
   4      5   6     7
'''
print("Inorder Traversal - ")
t.inorder_traversal(t.root)
print("\nPreorder Traversal -")
t.preorder_traversal(t.root)
print("\nPostorder Traversal - ")
t.postorder_traversal(t.root)
