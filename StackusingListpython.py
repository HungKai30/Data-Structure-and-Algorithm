class Stack:

    def __init__(self):
        self.stackList = list()

    def isEmpty(self):
        return len(self.stackList) == 0

    def length(self):
        return len(self.stackList)

    def getTop(self):
        assert not self.isEmpty(), "Ngan xep rong! Khong the tra ve phan tu o dinh"
        return self.stackList[-1]

    def pop(self):
        assert not self.isEmpty(), "Ngan xep rong! Khong the loai bo phan tu"
        return self.stackList.pop()

    def push(self, item):
        self.stackList.append(item)
