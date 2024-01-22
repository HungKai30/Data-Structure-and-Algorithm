class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
#ta hiểu rằng lệnh này sẽ giúp ta tạo ra 1 con trở
class Linkedlist():
    def __init__(self,head = None):
        self.head = head
        self.len = 0
    def traversal(self):
        temp= self.head