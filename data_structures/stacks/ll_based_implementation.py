class LinkedStack:
    class _Node:
        def __init__(self, value, next = None) -> None:
            self._value = value
            self._next = next
    
    def __init__(self) -> None:
        """Initializing empty stack"""
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        """Returns True if stack is empty"""
        return self._size == 0

    def push(self, value):
        """Pushes a value at the top of the stack. LIFO"""
        
        # --------------1st way to write-----------------
        # new_node = self._Node(value)
        # if self.is_empty():
        #     self._head = new_node
        # else:
        #     new_node._next = self._head
        #     self._head = new_node

        # --------------2nd way to write-----------------
        # new_node = self._Node(value)
        # if not self.is_empty():
        #     new_node._next = self._head
        # self._head = new_node
        # self._size += 1

        # --------------easiest way to write-----------------
        self._head = self._Node(value, self._head)
        self._size += 1
    
    def top(self):
        """Returns the element at the top of the Stack. Does not remove.
        
        Raise Exception if empty"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._head._value

    def pop(self):
        """Removes and returns element from the top of the Stack. LIFO

        Raise Exception if empty"""
        if self.is_empty():
            raise Exception("Stack is empty")           
        popped_node = self._head
        self._head = popped_node._next
        self._size -= 1
        return popped_node._value

    def print_stack(self):
        if self._head == None:
            print("Empty Stack")
        else:
            elements = list()
            curr_node = self._head
            while curr_node != None:
                elements.append(str(curr_node._value))
                curr_node = curr_node._next
            print(' <- '.join(elements))



my_stack = LinkedStack()
my_stack.push(10)                           # [10]
my_stack.push(2)                            # [10, 2]

print(f"size of stack: {len(my_stack)}")    # [10, 2]; o/p: size of stack: 2
my_stack.print_stack()

print(f"popped: {my_stack.pop()}")          # [10]; o/p: popped: 2
print(f"is empty: {my_stack.is_empty()}")   # [10]; o/p: is empty: False

my_stack.push(27)                           # [10, 27]
my_stack.push(98)                           # [10, 27, 98]
print(f"top: {my_stack.top()}")             # [10, 27, 98]; o/p: top: 98

