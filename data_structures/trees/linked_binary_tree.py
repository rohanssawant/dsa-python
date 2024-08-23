from binary_tree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Linked representation of Binary tree"""
    
    class _Node:
        def __init__(self, element, parent=None, left=None, right=None) -> None:
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    
    class Position(BinaryTree.Position):
        """Abstraction representing the location of a single element. A public wrapper around Node."""

        def __init__(self, container, node) -> None:
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other: object) -> bool:
            if type(other) is type(self) and other._node is self._node:
                return True
            return False
    
    def _validate(self, p) -> _Node:
        """Return associated Node if Position `p` is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p is not a Position type")
        return p._node

    def _make_position(self, node) -> Position:
        """Create and return Position for a node"""

        if node is not None:
            return self.Position(self, node)
        return None
    
    #--------binary tree constructor--------   

    def __init__(self) -> None:
        """Create an empty binary tree"""

        self._root = None
        self._size = 0

    #--------public accessor methods--------

    def __len__(self):
        """Return total number of elements in T"""
        return self._size

    def root(self):
        """Return root Position of T
        
        None if T is empty"""

        return self._make_position(self._root)
    
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        node = self._validate(p)        
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)        
        return self._make_position(node._right)
    
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    #--------non public update methods--------
    def _add_root(self, e):
        """Place element e at the root of the T
        
        Raises ValueError if root already exists"""

        if self._root is not None:
            raise ValueError("Root already exists")
        
        self._root = self._Node(e)
        self._size += 1
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        """Create new left child for Position `p` storing `e`
        
        Return Position of new Node
        Raise ValueError is `p` is invalid or `p` already has left child"""

        parent_node = self._validate(p)
        if parent_node._left is not None:
            raise ValueError("Left child already exists")
        
        new_node = self._Node(e, parent_node)
        parent_node._left = new_node
        self._size += 1
        return self._make_position(new_node)

    def _add_right(self, p, e):
        """Create new right child for Position `p` storing `e`
        
        Return Position of new Node
        Raise ValueError is `p` is invalid or `p` already has right child"""

        parent_node = self._validate(p)
        if parent_node._right is not None:
            raise ValueError("Right child already exists")
        
        new_node = self._Node(e, parent_node)
        parent_node._right = new_node
        self._size += 1
        return self._make_position(new_node)

    def _replace(self, p, e):
        """Replace the element at Position `p` with element `e`
        
        Return old element"""

        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position `p` and replace with its child, if any
        
        Return element that had been stored at `p`
        Raise ValueError if `p` is invalid or `p` has two children"""


        old_node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("Position has two children")
        
        child = old_node._left if old_node._left is not None else old_node._right
        # if old_node._left is not None:
        #     child = old_node._left
        # elif old_node._right is not None:
        #     child = old_node._right

        # Child's grandparents become parent
        child._parent = old_node._parent

        if self._root is old_node:
            self._root = child
        else:
            parent = old_node._parent

            if old_node is parent._left:
                parent._left = child
            elif old_node is parent._right:
                parent._right = child
        
        self._size -= 1

        old_node._parent = old_node         # convention for deprecated node

        return child._element





    

    

        