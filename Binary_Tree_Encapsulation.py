class treenode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
    # @staticmethod
    def create_tree(data):
        if data is None:
            node = None
        elif isinstance(data,tuple)   and     len(data) == 3:
            node = treenode(data[1])
            node.left = treenode.create_tree(data[0])
            node.right = treenode.create_tree(data[2])
        else: 
            node = treenode(data)
        return node
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return treenode.to_tuple(self.left) , self.key , treenode.to_tuple(self.right)
    
    def __repr__(self):
        return "Binary Tree : {}".format(self.to_tuple())

    
    def traverse_tree(self):
        if self is None:
            return []
        return (treenode.traverse_tree(self.left)) + [self.key] + (treenode.traverse_tree(self.right))
        
data = ((1,3,None),2,((None,3,4),5,(6,7,8)))
tree = treenode.create_tree(data)
print(tree)
print(tree.traverse_tree())



