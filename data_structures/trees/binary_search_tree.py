from linked_binary_tree import LinkedBinaryTree

class BinarySearchTree(LinkedBinaryTree):
    """Binary Search Tree representation"""

    def __init__(self) -> None:
        """Create an empty binary search tree"""
        super().__init__()

    def insert(self, value):
        """Insert a value in a tree"""
        if len(self) == 0:
            self._add_root(value)
        else:
            # loop through all the nodes to find current position
            curr_position = self.root()
            while(True):
                # self.left(curr_position).element
                if value < curr_position.element():
                    # insert left 
                    if self.left(curr_position) is None:
                        self._add_left(curr_position, value)
                        return
                    # some left child is already present
                    curr_position = self.left(curr_position)
                else:
                    # insert right
                    if self.right(curr_position) is None:
                        self._add_right(curr_position, value)
                        return
                    curr_position = self.right(curr_position)
    
    def search(self, value):
        """Search a value in a tree"""
        if len(self) == 0:
            return False                                # Tree is empty
        curr_pos = self.root()
        while (True):
            if value < curr_pos.element():              # Go left
                curr_pos = self.left(curr_pos)
            elif value > curr_pos.element():            # Go right
                curr_pos = self.right(curr_pos)
            elif value == curr_pos.element():           # Found ele
                return True 
            else:                                       # Not found
                return False



bst = BinarySearchTree()
bst.insert("20")
bst.insert("2")
bst.insert("10")
print(bst.traverse(bst.root()))