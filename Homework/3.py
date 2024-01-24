class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

def change(n, base):
    stack = Stack()

    while n > 0:
        remainder = n % base
        stack.push(remainder)
        n //= base

    result = ""
    while not stack.is_empty():
        result += str(stack.pop())

    return result

# Example usage:
number = int(input("Enter a positive integer: "))
new_base = int(input("Enter the base to convert to: "))

converted_number = change(number, new_base)
print(f"{number} in base {new_base}: {converted_number}")
