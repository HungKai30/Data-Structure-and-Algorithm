class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)


def is_palindrome(input_str):
    input_queue = Queue()

    # Enqueue each character into the queue
    for char in input_str:
        input_queue.enqueue(char)

    # Dequeue characters from the queue and compare with the original string
    while not input_queue.is_empty():
        if input_queue.dequeue() != input_str[0]:
            return False
        else:
            input_str = input_str[1:]

    return True


# Example usage:
user_input = input("Nhập chuỗi cần kiểm tra palindrome: ")
if is_palindrome(user_input):
    print("Chuỗi là palindrome.")
else:
    print("Chuỗi không phải là palindrome.")
