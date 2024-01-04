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
    stack = []
    p = root
    while (len(stack) > 0 or p):  # how long are repeating these steps?
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


def iterative_postorder(root):
    stack = []
    p = root
    while (len(stack) > 0 or p):
        if p:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            if p.value[0] == "-":
                print(p.value.strip("-"))
                p = stack.pop()
                p = p.right
            else:
                p.value = f"-{p.value}"
                stack.append(p)
                p = p.right



if __name__ == "__main__":
    root = create_tree()
    # print("Recursive preorder: ")
    # recursive_preorder(root)
    # print("Iterative preorder: ")
    # iterative_preorder(root)
    print("Recursive postorder: ")
    recursive_postorder(root)
    print("Iterative postorder: ")
    iterative_postorder(root)
