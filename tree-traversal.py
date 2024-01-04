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


def iterative_preorder(root):
    stack = [root]
    p = root
    while len(stack) > 0:
        if p:
            print(p.value)
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            p = p.right


def recursive_postorder(node):
    if node:
        recursive_postorder(node.left)
        recursive_postorder(node.right)
        print(node.value)


if __name__ == "__main__":
    root = create_tree()
    # print("Recursive preorder: ")
    # recursive_preorder(root)
    # print("Iterative preorder: ")
    # iterative_preorder(root)
    print("Recursive postorder: ")
    recursive_postorder(root)
