# This implementation does not use sentinels
    

class DoublyLinkedList():
    class _Node():
        def __init__(self, value, prev = None, next = None):
            self.value = value
            self.prev = prev
            self.next = next
        
    def __init__(self) -> None:
        self.head = None
        self.tail = self.head
        self.size = 0

    def __len__(self):
        return self.size
    
    def print(self):
        if self.head == None:
            print('Empty')
        else:
            values = []
            curr_node = self.head
            while curr_node != None:
                values.append(str(curr_node.value))     #convert to str before appending
                curr_node = curr_node.next
            print(' <-> '.join(values))
        
    def append(self, value):
        new_node = self._Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail           # link prev of newnode to tail
            self.tail.next = new_node           # link tail node's(existing last going to be 2nd last) 
                                                # next to new_node(soon last node in list)
            self.tail = new_node                # point tail to new_node
        self.size += 1
    
    def prepend(self, value):
        new_node = self._Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def insert(self, value, pos):
        # at start
        if pos == 0:
            self.prepend(value)
        # at end
        elif pos >= self.size:
            self.append(value) #if pos > size then we insert at the end
        # somewhere in middle
        else:
            new_node = self._Node(value)
            curr_node = self.head
            for i in range(pos - 1):
                curr_node = curr_node.next
            new_node.prev = curr_node
            new_node.next = curr_node.next
            curr_node.next = new_node
            new_node.next.prev = new_node
            self.size += 1
        
    def delete(self, node: _Node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
