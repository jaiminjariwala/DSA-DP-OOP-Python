from typing import List, Any, Optional

class Stack:
    def __init__(self) -> None:
        # initialize an empty list as a stack
        self.stack: List[Any] = []

    def current_stack_elements(self) -> List[Any]:
        return self.stack

    def push(self, item: Any) -> None:
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

    def pop(self) -> Optional[Any]:
        """
        Remove and return the top element of the stack
        """
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self) -> Optional[Any]:
        """
        Return the top element without removing it
        """
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self) -> int:
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