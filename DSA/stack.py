from typing import Union

class Stack:
    def __init__(self):
        # initialize an empty list as a stack
        self.stack = []

    def current_stack_elements(self):
        return self.stack

    def push(self, item: Union[int, float, str, chr]):
        """
        Add an element to the top of the stack
        
        Args:
            item: The element to be pushed onto the stack.
                  Can be an integer, float, string or character.
        """
        self.stack.append(item)
        print(f"Pushed: {item}")

    def is_empty(self) -> bool:
        """
        check whether stack is empty before attempting to pop an element
        """
        return len(self.stack) == 0

    def pop(self):
        """
        Remove and return the top element of the stack
        """
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        """
        Return the top element without removing it
        """
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        """
        Return the number of elements in the stack
        """
        return len(self.stack)

stack = Stack()
stack.push(20)
stack.push(10)
stack.push("(")
stack.push(")")
stack.push("$")
print(f"\nTop Element: {stack.peek()}")
print(f"Popped: {stack.pop()}")
print(f"Current Stack elements: {stack. current_stack_elements()}")
print(f"Stack size: {stack.size()}")
print(f"Is stack empty? {stack.is_empty()}\n")
