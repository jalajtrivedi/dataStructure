class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    
    return root

def find_height(node):
    if node is None:
        return -1  
    
    left_height = find_height(node.left)
    right_height = find_height(node.right)
    
    return max(left_height, right_height) + 1


arr = [10, 7, 8, 9, 11, 12, 13, 15]
root = None
for value in arr:
    root = insert_into_bst(root, value)

height = find_height(root)
print("Height of the BST:", height)  