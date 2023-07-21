
class tree_node:
    def  __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def create_tree(data):
        if data is None:
            node = None
        elif isinstance(data,tuple)     and     len(data) == 3:
            node = tree_node(data[1])
            node.right = tree_node.create_tree(data[2])
            node.left = tree_node.create_tree(data[0])
        else:
            node = tree_node(data)
        return node
    
    def to_tuple(self):
        if self is None:
            return None
        elif self.right is None   and   self.left is None:
            return self.key
        else:
            return tree_node.to_tuple(self.left), self.key , tree_node.to_tuple(self.right)
    
    def __repr__(self):
        return "Binary Tree = {}".format(self.to_tuple())
    
    def traverse_tree(self):
        if self is None:
            return []
        return tree_node.traverse_tree(self.left) + [self.key] + tree_node.traverse_tree(self.right)
    
    def BST(self):
        BST = self.traverse_tree()
        print(BST)
        
        flag = 0
        element = 1
        while element < len(BST):
            if BST[element] < BST[element-1]:
                flag = 1
            element += 1
        if flag == 0:
            print('Binary Search Tree')
        else:
            print('Not a Binary Search Tree')
        
# data = ((1,3,None),2,((None,3,4),5,(6,7,8)))
data = ((2,4,(5,7,8)),9,(None,11,(14,15,None)))
tree = tree_node.create_tree(data)
print(tree)
tree.BST()
# print(tree.traverse_tree())
