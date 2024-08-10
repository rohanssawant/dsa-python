class Empty(Exception):
    """new exception class when attempting to access element in an empty Stack"""
    pass

class ArrayStack():
    """Stack LIFO implementation using Python List. Begins with an empty List and expands as needed."""

    def __init__(self):
        self._data = []   # initialise empty stack
    
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self.__len__() == 0  # True is stack is empty
    
    def push(self, value):
        self._data.append(value)
    
    def top(self):
        """Raises exception if stack is empty else only returns the top element."""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        """Raises exception if stack is empty else executes pop."""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()
    
    def print(self):
        """LIFO so we print in reverse order ie Last element will print first"""
        for i in range(self.__len__() - 1, -1, -1):
            print(self._data[i])
    
my_stack = ArrayStack()
my_stack.pop()
my_stack.push(10)                           # [10]
my_stack.push(2)                            # [10, 2]

print(f"size of stack: {len(my_stack)}")    # [10, 2]; o/p: size of stack: 2
my_stack.print()

print(f"popped: {my_stack.pop()}")          # [10]; o/p: popped: 2
print(f"is empty: {my_stack.is_empty()}")   # [10]; o/p: is empty: False

my_stack.push(27)                           # [10, 27]
my_stack.push(98)                           # [10, 27, 98]
print(f"top: {my_stack.top()}")             # [10, 27, 98]; o/p: top: 98