# Basic Tree Node and Binary Tree:
# A binary tree is a tree where each node has at most 2 children (left and right).
# A Node class represents a tree node with a value and pointers to left and right children.

# Tree Traversals:
# Tree Traversals are methods to visit all nodes in a tree. Common traversals for binary trees are:
    # 1. Pre-order (perfect anti-clockwise): Visit root, then left subtree, then right subtree.
    # 2. In-order (clockwise): Visit left subtree, then root, then right subtree (useful for BSTs to get sorted order).
    # 3. Post-order: Visit left subtree, then right subtree, then root. 
    # 4. Level-order: Visit nodes level by level (using queue).
# Recursive implementations are straightforward for pre-order, in-order, and post-order.
# Level-order traversal uses a queue to process nodes breath-first.
# Each traversal will print node values to demonstrate the order of visitation.

# Binary Search Tree (BST):
# A BST is a binary tree where each node's left subtree contains values less than the node's value, and the right subtree contains values greater than the node's value. This property enables efficient searching, insertion, and deletion.
    # Search: Recursively or iteratively find a value by comparing it with the current node and moving left or right.
    # Insertion: Insert a new value by traversing to the appropriate leaf position.
    # Deletion: Handle three cases (node with no children, one child, or two children) and maintain BST properties.
    # In-order traversal of a BST yields values in sorted order.

class Node:
    """class for representing a node in a tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 # used for AVL tree balancing

class BinaryTree:
    """class for basic binary tree operations"""
    def __init__(self):
        self.root = None
    
    def create_sample_tree(self):
        """create a sample binary tree for testing"""
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)

    def preorder(self, node):
        """pre-order traversal: root, left, right"""
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)    # goes into the left subtree (node=2, node=4)
            self.preorder(node.right)
        # When recursive call is made, the current function is paused at that line.
        # Only when the recursive call finishes, the function resumes from the next line.

    def inorder(self, node):
        """in-order traversal: left, root, right"""
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)
    
    def postorder(self, node):
        """post-order traversal: left, right, root"""
        if node:
            self.preorder(node.left)
            self.preorder(node.right)
            print(node.value, end=" ")
        
    def levelorder(self):
        """
            Level-order traversal usese queue to explore the tree level by level (also called breadth-first traversal). It's not recursive!
        """
        if not self.root:
            return
        queue = [self.root]         # start with root in the queue
        while queue:                # loop until queue is empty
            node = queue.pop(0)     # remove the front element of the queue
            print(node.value, end=" ")
            if node.left:           # if left child exists, enqueue it
                queue.append(node.left)
            if node.right:          # if right child exists, enqueue it
                queue.append(node.right)


