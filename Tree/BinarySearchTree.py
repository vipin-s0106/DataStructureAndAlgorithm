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


    def search_node(self,root,data):
        if root == None:
            return False
        if root.data == data:
            return True
        return self.search_node(root.left,data) or self.search_node(root.right,data)

    def delete_node(self,root,data,prev=None):
        if root == None:
            return False
        if root.data == data:
            if root == self.root:
                self.root = None
            else:
                if prev.left == root:
                    prev.left = None
                else:
                    prev.right = None
            return True
        return self.delete_node(root.left,data,root) or self.delete_node(root.right,data,root)

    def inorder_traversal(self,root):
        if root == None:
            return
        self.inorder_traversal(root.left)
        print(root.data,end=" ")
        self.inorder_traversal(root.right)

'''
           5  -->root 
       /       \ 
      2          8 
    /   \       /  \ 
   1    3      7    9
                     \
                     12
'''
t = BST()
t.insert(5)
t.insert(2)
t.insert(8)
t.insert(1)
t.insert(3)
t.insert(7)
t.insert(9)
t.insert(12)
t.inorder_traversal(t.root)
print("\nSearch Element Found - "+str(t.search_node(t.root,1)))

print("Given Node deleted - "+str(t.delete_node(t.root,12)))
t.inorder_traversal(t.root)








