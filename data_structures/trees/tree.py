class Tree:
    """Abstract Base Class representing tree data structure"""

    class Position:
        """Abstraction representing position of a single element"""

        def element(self):
            """Return element stored at this position"""
            raise NotImplementedError('Should be implemented by the subclass')
        
        def __eq__(self, other: object) -> bool:
            """Return True if other position represents same location"""
            raise NotImplementedError('Should be implemented by the subclass')
        
        def __ne__(self, other: object) -> bool:
            """Return True if other position does not represent the same location"""
            return not(self == other)
    
    def root(self):
        """Return position of root of T or None if empty"""
        raise NotImplementedError('Should be implemented by the subclass')

    def parent(self, p):
        """Return position of the parent of position p or None if p is root"""
        raise NotImplementedError('Should be implemented by the subclass')
    
    def num_children(self, p):
        """Return number of children of p"""
        raise NotImplementedError('Should be implemented by the subclass')

    def children(self, p):
        """Generate iteration of the children of p"""
        raise NotImplementedError('Should be implemented by the subclass')

    def __len__(self):
        """Return number of elements contained in T"""
        raise NotImplementedError('Should be implemented by the subclass')
    
    def is_root(self, p):
        """Return True if `p` is the root of the T"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if `p` does not have any children"""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if T is empty """
        return len(self) == 0
