class LinkedList():

    class _Node():
        def __init__(self, val: str, next: str = None) -> None:
            self.value = val
            self.next = next
        def __str__(self) -> str:
            print(str(self.value))

    def __init__(self) -> None:
        self.head = None
        self.tail = self.head
        self.length = 0
    
    # insert at the tail O(1)
    def append(self, value):
        new_node = self._Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:    
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # insert at the head O(1)
    def prepend(self, value):
        new_node = self._Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    # print
    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            elements = list()
            curr_node = self.head
            while curr_node != None:
                elements.append(str(curr_node.value))
                curr_node = curr_node.next
            print(' -> '.join(elements))

    # search a node value O(n)
    def search_value(self, value):
        curr_node = self.head
        while curr_node != None:
            if curr_node.value == value:
                return True
            curr_node = curr_node.next
        return False
    
    # insert at a position. O(n)
    # if position is 0 ie at start then its prepend
    # if position is greater than length by 1 then append
    # if somewhere else then we get iterator node till (position - 1) then point its
    # next to our new_node and new_node's next to (position - 1)'s next
    def insert(self, position, value):
        if position == 0:
            self.prepend(value)
        elif position > self.length:
            return print(f"Cannot insert at position {position} as its greater than length of LL {self.length}")
        elif position == self.length:
            self.append(value)
        else:
            new_node = self._Node(value)
            curr_node = self.head
            for i in range(position - 1):
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node
            self.length += 1
            
    
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.print_list()

    linked_list.append(15)
    linked_list.append(10)
    linked_list.append(30)
    linked_list.append(2)
    linked_list.print_list()

    linked_list.prepend(23)
    linked_list.print_list()

    linked_list.search_value(2)

    linked_list.insert(0, 100)
    linked_list.insert(linked_list.length, 1000)
    linked_list.print_list()

