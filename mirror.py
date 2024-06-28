class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root1=Node(10)
root1.left = Node(3)
root1.right = Node(8)

root2=Node(10)
root2.left = Node(8)
root2.right = Node(3)

def are_mirrored(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return(root1.data == root2.data) and are_mirrored(root1.left,root2.right) and are_mirrored(root1.right,root2.left)
print("Tree is mirrored" if are_mirrored(root2,root2)else "tree is not mirrored" )