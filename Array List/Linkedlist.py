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
        current_Node = head
        while current_Node is not None and current_Node.data !=target:
            current_Node = current_Node.next
# tìm kiếm không có thứ tự
#current_Node trỏ vào head, nếu current_Node không phải None và current_Node không bằng target , nó sẽ tiếp tục vòng lặp cho tới khi nào tìm thấy thì thôi
    def traversal(self):
        current_Node = self.head
        while current_Node is not None:
            print(current_Node.data)
            current_Node = current_Node.next
#nó se
    #duyệt toàn bộ danh sách
    def append(self, new_node):
        current_Node = self.head
        if current_Node:
            while current_Node.next:
                current_Node = current_Node.next
            current_Node.next = new_node
        else:
            self.head = new_node


e1 = Node(1)
e2 = Node(10)
l1 = Linkedlist(e1)

l1.append(e2)
l1.traversal()



