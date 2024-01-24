def calculate_s_iterative(n):
    s = 1
    for i in range(1, n + 1):
        s += 1 / (i * (i + 1))
    return s

# Nhập giá trị n từ bàn phím
n = int(input("Nhập giá trị n: "))

# Tính giá trị S bằng cách lặp
result = calculate_s_iterative(n)

# Hiển thị kết quả
print(f"Gia tri cua S voi n={n} la: {result}")

def calculate_S_recursive(n):
    if n == 0:
        return 1
    #đây là phần ta dùng để dừng lại giá trị đệ quy
    else:
        return 1/(n*(n+1)) + calculate_S_recursive(n-1)
#ta hiểu một khi ta gọi đệ quy
#giả sử n = 3 chẳng hạn đi
#n = 3 không bằng không, nó nhảy sang trường hợp else
#

n = int(input("Nhập giá trị của n: "))
print("Giá trị của S là:", calculate_S_recursive(n))
# Nhập giá trị n từ bàn phím
# Hiển thị kết quả
print(f"Gia tri cua S voi n={n} la: {result}")
