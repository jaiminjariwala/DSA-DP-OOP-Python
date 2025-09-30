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
# A BST is a binary tree where each node's left subtree contains values less than the node's value, and the right subtree contains values greater than or equal to the node's value. This property enables efficient searching, insertion, and deletion.
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


class BST:
    """Class for Binary Search Tree operations"""
    def __init__(self):
        """
        When you create a BST, it starts empty.
        self.root (pointer) will point to the very first node when you insert the first value.
        """
        self.root = None

    def insert(self, value):
        """
        This is the public method you call to insert a new value into the BST.
        It calls the helper function '_insert_recursive', starting at the root node.
        Why recursive? Because to insert, you may need to go down multiple levels until you find the right spot.
        """
        self.root = self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """
        Helper method for recursive insertion.
        Python doesn't enforce strict privacy like Java or C++ but...
        Underscore before the method name,tells other programmers: Don't call this directly - it's a helper method!
        """
        if not node:
            return Node(value)  # base case: found empty spot, create new Node
        if value < node.value:  # if node exists & value less than node.value
            node.left = self._insert_recursive(node.left, value)    # node.left means left side of root
        else:
            node.right = self._insert_recursive(node.right, value)
        return node
    
    def search(self, value):
        """Search for a value in the BST"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper method for recursive search"""
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value):
        """Delete a value from the BST"""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """Helper method for recursive deletion"""
        # When deleting a node in a BST you find the node first, then handle one of three cases:
            # 1. Node is a leaf (no children) -> remove it (return None to parent).
            # 2. Node has 1 child -> replace the node with its single child (return that child to parent).
            # 3. Node has 2 children -> find the successor (smallest node in the right subtree), copy the successor's value into the node, then delete the successor from the right subtree. (_find_min helps find the successor.)

        # Step-1: Find node
        if not node:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)    # (node.left == value) means we found the node
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)  # (node.right == value) means we found the node
        else:
            # Step-2: Check children
            # Case 1: No children or one child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            # Case 2: Two children
            # We have to make the smallest element in the right subtree as the root if self.root == value, because the smallest element in the right subtree will still be bigger than the elements in left subtree
            successor = self._find_min(node.right)
            node.value = successor.value
            # delete successor in right subtree, as it still exists even though we made that smallest element from right subtree as the root element.
            node.right = self._delete_recursive(node.right, successor.value)
        return node
    
    def _find_min(self, node):
        """Find the minimum value node in a subtree."""
        # Start at node (self.root), keep going left until there is no left child. That leftmost node is the smallest value in that subtree.
        current = node
        while current.left:
            current = current.left
        return current