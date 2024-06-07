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

def validate_bst(node, low=float('-inf'), high=float('inf')):
    if node is None:
        return True
    
    if not (low < node.value < high):
        return False
    
    return (validate_bst(node.left, low, node.value) and
            validate_bst(node.right, node.value, high))

def can_form_bst(arr):
    if not arr:
        return True

    root = TreeNode(arr[0])
    for value in arr[1:]:
        root = insert_into_bst(root, value)
    
    return validate_bst(root)


arr = [10, 7, 8, 9, 11, 12, 13, 15]
print(can_form_bst(arr))  
