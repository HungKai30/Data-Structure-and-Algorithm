
n = int(input("Nhập giá trị n: "))

def factorial(n):
    if (n==1 or n ==0):
        return 1
    else:
        return (n * factorial(n-1))
# ta có thể thấy factorial được gọi lại 1 lần
#giả sử n=3 , nó sẽ duyệt về n=2 chẳng hạn và ví dụ...

num =5
print("number: ", num)
print("Factorial:",factorial(num))