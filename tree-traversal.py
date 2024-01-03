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
    stack.append(root)
    print(root.value)
    while len(stack) > 0:
        node = stack[-1]
        if not (node.left or node.right):
            stack.pop()
            stack[-1].value = f"-{stack[-1].value}" 
            print([x.value for x in stack])
        if node.value[0] == "-":
            if node.right:
                print(node.right.value)
                stack.append(node.right)
        if node.left:
            print(node.left.value)
            stack.append(node.left)
        


if __name__ == "__main__":
    root = create_tree()
    #recursive_preorder(root)
    iterative_preorder(root)
