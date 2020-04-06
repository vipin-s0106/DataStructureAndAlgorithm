class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def inorder_traversal(self, root):
        if root == None:
            return
        self.inorder_traversal(root.left)
        print(root.data, end=" ")
        self.inorder_traversal(root.right)

    def getHeightTree(self,root):
        if root == None:
            return 0
        return 1 + max(self.getHeightTree(root.left),self.getHeightTree(root.right))

    def getDepthTree(self,root):
        pass


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

   height = 4  - no of nodes present in the longest path
'''
print("Height of Tree - "+str(t1.getHeightTree(t1.root)))
# print("Depth of Tree - "+str(t1.getDepthTree(t1.root)))