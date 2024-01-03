import queue

class Node:
    
    def __init__(self, value = None, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def create_tree():
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    root.right.left = Node("F")
    root.right.right = Node("G")
    return root

def recursive_preorder(node):
    if node:
        print(node.value)
        recursive_preorder(node.left)
        recursive_preorder(node.right)

if __name__ == "__main__":
    root = create_tree()
    recursive_preorder(root)