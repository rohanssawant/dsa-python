from tree import Tree

class BinaryTree(Tree):
    """Abstract Base class for binary tree structure"""
    
    def left(self, p):
        """Return the position of the left child of p. 
        
        None if no left child"""
        raise NotImplementedError("should be implemented by subclass")

    def right(self, p):
        """Return the position of the right child of p. 
        
        None if no right child"""
        raise NotImplementedError("should be implemented by subclass")

    #--------concrete methods implemented here--------
    def sibling(self, p):
        """Return the position of the sibling of p.
        
        None if no sibling"""
        # check if `p` is root. if its root then no sibling and no parent
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        """Generate iterations of positions of `p`"""
        if self.left(p) is not None:
            yield self.left(p)            
        elif self.right(p) is not None:
            yield self.right(p)