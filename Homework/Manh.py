class Stack:
    def __init__(self, maxSize):            #Khởi tạo một ngăn xếp rỗng
        self._size = 0
        self._top = -1                      #Chỉ số của phần tử đầu tiên trong ngăn xếp.
        self._stackArray = [None]*maxSize

    def isEmpty(self):                      #Khởi tạo hàng đợi rỗng dựa vào số phần tử của ngăn xếp
        return self._size == 0
    
    def isFull(self):                       #Kiểm tra ngăn xếp đầy
        return self._size == len(self._stackArray)
    
    def length(self):                       #Trả về số phần tử của ngăn xếp
        return self._size
    
    def getTop(self):                       #Trả về số phần tử đầu ngăn xếp
        return self._stackArray[self._top]
    
    def push(self, item):                   #Thêm một phần tử mới vào ngăn xếp
        assert not self.isFull(), "ngan xep day, khong the them"
        self._top = self._top + 1
        self._stackArray[self._top] = item
        self._size += 1

    def pop(self):            #Loại bỏ và trả về giá trị của phần tử đầu tiên trong ngăn xếp
        assert not self.isEmpty(), "ngan xep rong, khong the xoa phan tu"
        item = self._stackArray[self._top]
        self._top = self._top - 1
        self._size -= 1
        return item
    
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
number = int(input("Nhập số bất kỳ: "))
new_base = int(input("Hệ mấy: "))

converted_number = change(number, new_base)
print(f"{number} in base {new_base}: {converted_number}")
# stack = stack(10)

# stack.push(1)
# stack.push(2)
# stack.push(3)

# print(stack.getTop())
# # 3
# stack.pop()
# print(stack.getTop())
# # 2
# print(stack.isEmpty())
# # False
# print(stack.isFull())
# # False
