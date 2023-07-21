class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
def tree_tuple(data):
    
    if isinstance(data,tuple)  and  len(data) == 3:
        node =  TreeNode(data[1])
        node.left = tree_tuple(data[0])
        node.right = tree_tuple(data[2])
    elif data == None:
        node = None
    else:
        node = TreeNode(data)
    return node


data = ((1,3,None),2,((None,3,4),5,(6,7,8)))
Tree = tree_tuple(data)

######## Traverse  a Binary Tree ####################
 
def traverse_inorder(node):
    if node is None:
        return []
    return(traverse_inorder(node.left) + [node.key] + traverse_inorder(node.right))

print(traverse_inorder(Tree))

######## Height  a Binary Tree ####################

def height_tree(node):
    if node is None:
        return 0
    return 1 + max(height_tree(node.left),height_tree(node.right))  
print(height_tree(Tree))


######## Size  a Binary Tree ####################

def size_tree(node):
    if node is None:
        return 0
    return 1 + size_tree(node.left) + size_tree(node.right)

print(size_tree(Tree))


 


