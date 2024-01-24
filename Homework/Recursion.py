#Câu 1. Cho công thức:
#𝑆(𝑛) = 1 × 3 × 5 × ... × (2𝑛 + 1)
#Hãy viết một thủ tục đệ qui tính giá trị 𝑆(𝑛) với n nhập vào từ bàn phím.
#Câu 2. .....
def recursion(n):
    if n == 0:
        return 1
    else:
        return recursion(n-1) * (2*n + 1)

print(recursion(3))