def print_as_letter(num):
    ascii_a = 97
    assert num < 27, "not enough letters in the alphabet"
    letter = chr(num+ascii_a-1) # -1 since you start your nodes at 1
    print(letter)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def printInorder(root):
    if root:
        printInorder(root.left)
        print_as_letter(root.val)
        printInorder(root.right)
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print_as_letter(root.val)
def printPreorder(root):
    if root:
        print_as_letter(root.val)
        printPreorder(root.left)
        printPreorder(root.right)
root = Node(1)
root.right = Node(2)
root.right.right = Node(3)
root.right.right.right = Node(4)
root.right.right.right.right = Node(5)
root.right.right.right.right.right = Node(6)
root.right.right.right.right.right.right = Node(7)
print ("Preorder")
printPreorder(root) 
print ("In-order")
printInorder(root)
print ("Post-order")
printPostorder(root)