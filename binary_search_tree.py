# Node implementation of a binary tree
class Node():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


# binary search tree implementation
# A binary search tree is a binary tree such that, for each node, all values on the left are smallerthan or equal to the node value, 
# and all values on the right are larger than the node value.
class BST:
    
    def __init__(self):
        self.root = None
        
    def add(self, value):
        if self.root is None:
            # The root does exist yet, create it
            self.root = Node(value)
        else:
            # Find the right place and insert new value
            self._add_recursive(self.root, value)
            
    def _add_recursive(self, current_node, value):
        if value <= current_node.value:
            # Go to the left
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._add_recursive(current_node.left_child, value)
        else:
            # Go to the right
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._add_recursive(current_node.right_child, value)
                
    def _contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._contains(current_node.left_child, value)
        return self._contains(current_node.right_child, value)
    
    # Define new contains method here
    def contains(self, value):
        return self._contains(self.root, value)


bst = BST()
for value in [5, 3, 9, 1, 8, 10, 6]:
    bst.add(value)

