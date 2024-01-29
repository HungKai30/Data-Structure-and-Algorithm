class _StackNode:
    # ngăn xếp này không có gì
    def __init__(self,item):
        self.item = item
        self.next = None
        
class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
    
    def isEmpty(self):
        return self._top is None
    
    def length(self):
        return self._size
    
    def getTop(self):
        assert not self.isEmpty(), "Cannot get top because it is empty"
        return self._top.item
    def pop(self):
        assert not self.isEmpty(),"Cannot get top because it is empty" 
        node =self._top
        self._top = self._top.next
        self._size -= 1
        return node.item
    
    def push(self,item):
        newNode = _StackNode(item)
        newNode.next = self._top
        self._top = newNode
        self._size += 1

def change(n, base):
    stack = Stack()

    while n > 0:
        remainder = n % base
        stack.push(remainder)
        n //= base

    result = ""
    while not stack.isEmpty():
        result += str(stack.pop())

    return result

# Example usage:
number = int(input("Enter a positive integer: "))
new_base = int(input("Enter the base to convert to: "))

converted_number = change(number, new_base)
print(f"{number} in base {new_base}: {converted_number}")