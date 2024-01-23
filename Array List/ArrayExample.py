#commitmain
class Node:
    def __init__(self,values):
        self.values = values
        self.next = None

class Linkedlist:
    def __init__(self,head=None):
        self.head = head
        self.len = 0
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
                while current:
                    if current.value == value:
                        break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None
    def insert(self, new_element, position):
             count=1
             current = self.head
             if position == 1:
                    new_element.next = self.head
                    self.head = new_element
             while current:
                if count+1 == position:
                    new_element.next =current.next
                    current.next = new_element
                    return
                else:
                    count+=1
                    current = current.next
                # break

             pass
    def print(self):
            current = self.head
            while current:
                print(current.value)
                current = current.next

e1 = Node(1)
e2 = Node(2)
l1 = Linkedlist(e1)
Linkedlist.insert(l1,2,1)
print(l1)
print(l1)