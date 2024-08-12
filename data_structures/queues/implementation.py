class LinkedQueue():
    class _Node():
        def __init__(self, value, next = None) -> None:
            self._value = value
            self._next = next
        
    def __init__(self) -> None:
        """Initializes empty Queue based on LinkedList."""
        self._head = None
        self._tail = self._head
        self._size = 0

    def __len__(self):
        """Returns length of the Queue"""
        return self._size

    def is_empty(self):
        """Returns true if the Queue is empty"""
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._head._value
    
    def enqueue(self, value):
        """Add an element to the end of the queue"""
        new_node = self._Node(value)
        if self.is_empty():
            self._head = new_node
            self._tail = self._head
        else:
            self._tail._next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return first element in the queue.
        
        Raises Exception if queue is empty"""
        if self.is_empty():
            raise Exception("Q is empty")
        popped_node = self._head
        self._head = popped_node._next
        self._size -= 1
        if self.is_empty():
            self._tail = self._head
        return popped_node._value

