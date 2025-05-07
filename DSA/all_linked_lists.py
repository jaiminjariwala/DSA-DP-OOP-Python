class Node:
    """
    Universal Node class that supports different linked list types by utilizing optional prev and next pointers
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class BaseLinkedList:
    """
    Base class for all linked list implementations
    Provides common methods and basic structure
    """
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        """Check if the list is empty"""
        return self.head is None
    
    def length(self):
        """Calculate the length of the linked list"""
        count = 0
        current = self.head     # current variable for linkedlist traversal
        while current:
            count += 1
            current = current.next
            if current == self.head:    # handle circular cases
                break
        return count
    
    def search(self, value):
        """
        Search a value in the list
        Returns the position of the first occurrence(in case if there exists more occurrences of each element), -1 if not found!
        """
        current = self.head     # current variable for traversal
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1

            if current == self.head:    # to handle circular linkedlist cases
                break
        return -1
    
class SinglyLinkedList(BaseLinkedList):
    """Singly Linked List implementation"""

    def insert(self, data, position=None):
        """
        Insert a node at a specific position
        If position is None, insert at the end
        If position if 0, insert at the beginning
        """
        new_node = Node(data)

        # INSERT AT THE BEGINNING
        if position == 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return  # terminate the function, as the task has been achieved
        
        # INSERT AT THE END OR SPECIFIC POSITION
        current = self.head
        current_position = 0

        # if inserting at the end (we can assume, that user has not inputted the position, hence position is None)
        if position is None:
            while current.next:
                current = current.next
            current.next = new_node
            return
        
        # insert at a specific position
        # traverse to node before insertion point
        while current and current_position < position-1:
            print(f"Current: {current}\nCurrent.next: {current.next}\nCurrent_Position: {current_position}")
            current = current.next
            current_position += 1
        if not current:
            raise IndexError("Position out of range")
        new_node.next = current.next
        current.next = new_node

    def delete(self, position=None, value=None):
        """Delete a node by position or value"""
        
        # base-case: cannot delete from empty list
        if not self.head:
            return None
        
        # DELETE BY POSITION
        if position is not None:
            
            # 1. delete first node
            if position == 0:
                deleted_data = self.head.data
                self.head = self.head.next
                return deleted_data
            
            current = self.head # current variable for traversal
            current_position = 0

            # traverse to node before deletion point
            while current and current_position < position - 1:
                current = current.next
                current_position += 1
            # ensure valid position
            if not current or not current.next: # if current or current.next is None then raise IndexError
                raise IndexError("Position out of range!")
            
            deleted_data = current.next.data
            current.next = current.next.next
            return deleted_data
        
        