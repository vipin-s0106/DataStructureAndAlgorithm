'''
The topmost node is called root of the tree. The elements that are directly under an element are called its children.
The element directly above something is called its parent. For example, ‘a’ is a child of ‘f’, and ‘f’ is the parent of ‘a’.
Finally, elements with no children are called leaves.

tree
      ----
       j    <-- root
     /   \
    f      k
  /   \      \
 a     h      z    <-- leaves

2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays).
3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists).
'''


# Python program to introduce Binary Tree

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # create root


root = Node(1)
''' following is the tree after above statement 
        1 
      /   \ 
     None  None'''

root.left = Node(2);
root.right = Node(3);

''' 2 and 3 become left and right children of 1 
           1 
         /   \ 
        2      3 
     /    \    /  \ 
   None None None None'''

root.left.left = Node(4);
'''4 becomes left child of 2 
           1 
       /       \ 
      2          3 
    /   \       /  \ 
   4    None  None  None 
  /  \ 
None None'''

'''
1) The maximum number of nodes at level ‘l’ of a binary tree is 2^(l-1).
  eg for 2nd level - 2(2-1) = 2
  
2) Maximum number of nodes in a binary tree of height ‘h’ is 2^(h) – 1.
'''