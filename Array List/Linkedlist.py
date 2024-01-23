class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
#ta hiểu rằng lệnh này sẽ giúp ta tạo ra 1 con trở
class Linkedlist():
    def __init__(self,head = None):
        self.head = head
        self.len = 0
  
    def unorderedSearch(head,target):
        curNode = head
        while curNode is not None and curNode.data !=target:
            curNode = curNode.next

    def traversal(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next
    
    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node


e1 = Node(1)
e2 = Node(2)
l1 = Linkedlist(e1)
Linkedlist.traversal(l1)



