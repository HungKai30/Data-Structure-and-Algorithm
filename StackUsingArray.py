class Stack:
    # Khởi tạo một ngăn xếp rỗng
    def __init__(self, maxSize):
        self._size = 0
        self._top = -1
        self._stackArray = [None]*maxSize

    # Kiểm tra hàng đợi rỗng dựa vào số phần tử của ngăn xếp
    def isEmpty(self):
        return self._size == 0

    # Kiểm tra ngăn xếp đầy
    def isFull(self):
        return self._size == len(self._stackArray)

    # Trả về số phần tử của ngăn xếp
    def length(self):
        return self._size
    
    # Trả về phần tử đầu của ngăn xếp.
    def getTop(self):
        return self._stackArray[self._top]

    # Thêm một phần tử mới vào ngăn xếp.
    def push(self, item):
        assert not self.isFull(), "ngăn xếp đầy, không thể thêm!"
        self._top = self._top + 1
        self._stackArray[self._top] = item
        self._size += 1

    # Loại bỏ và trả về giá trị của phần tử đầu tiên trong ngăn xếp.
    def pop(self):
        assert not self.isEmpty(), "ngăn xếp rỗng, không thể xoá phần tử."
        item = self._stackArray[self._top]
        self._top = self._top - 1
        self._size -= 1
        return item

