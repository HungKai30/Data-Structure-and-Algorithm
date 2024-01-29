class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current.next and current.next.value != value:
                current = current.next
            if current.next:
                current.next = current.next.next

    def insert(self, new_node, position):
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 1
            while current and count < position - 1:
                current = current.next
                count += 1
            if current:
                new_node.next = current.next
                current.next = new_node

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

e1 = Node(1)
e2 = Node(2)
e3 = Node(10)
l1 = LinkedList(e1)
l1.insert(e2, 1)
l1.append(e3)
l1.print()

