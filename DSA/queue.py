# a queue is a linear data structure that follows FIFO (First In First Out) principle. The first element added to the queue is the first one to be removed.

# queue operations:
# 1. enqueue: add an element to the rear of the queue.
# 2. dequeue: remove and return the front element of the queue.
# 3. front(peek): view the front element without removing it.
# 4. is_empty: check if the queue is empty.
# 5. size: get the number of elements in the queue.

from typing import List, Any, Optional

class Queue:
    # first we'll initialize a queue
    def __init__(self) -> None:
        self.queue: List[Any] = [] # using a list to store elements.

    def get_current_queue_elements(self) -> List[Any]:
        return self.queue

    def enqueue(self, item: Any) -> None:
        """
        add an element to the REAR of the queue
        """
        self.queue.append(item)

    def is_empty(self) -> bool:
        """
        check if the queue is empty

        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0
    
    def dequeue(self) -> Optional[Any]:
        """
        remove and return the FRONT element of the queue

        Returns:
            the element dequeued from the front, or "Queue is empty!" if the queue is empty.
        """
        if self.is_empty():
            return "Queue is empty!"
        return self.queue.pop(0)
    
    def front(self) -> Optional[Any]:
        """
        return the FRONT element without removing it

        Returns:
            the front element of the queue, or "Queue is empty!" if the queue is empty.
        """
        if self.is_empty():
            return "Queue is empty!"
        return self.queue[0]
    
    def size(self) -> int:
        return len(self.queue)

queue = Queue()
queue.enqueue("*")
queue.enqueue("{")
queue.enqueue("}")
queue.enqueue("@")

print(f"\nCurrent Queue Elements: {queue.get_current_queue_elements()}")
print(f"Front Queue: {queue.front()}")
print(f"Initial Queue size: {queue.size()}\n")
print(f"Dequeued: {queue.dequeue()}")
print(f"Later Queue size: {queue.size()}\n")