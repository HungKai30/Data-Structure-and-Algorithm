def bubble_sort(arr):
    n = len(arr)

    # Lặp qua tất cả các phần tử trong dãy
    for i in range(n):
        # Dãy đã được sắp xếp, nếu không có sự đổi chỗ nào trong một vòng lặp, thoát
        sorted_flag = True

        # Lặp qua tất cả các phần tử từ 0 đến n-i-1
        for j in range(0, n - i - 1):
            # So sánh các phần tử liền kề và đổi chỗ nếu cần thiết
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted_flag = False

        # Nếu không có sự đổi chỗ nào, dãy đã được sắp xếp và có thể thoát
        if sorted_flag:
            break

        # In dãy số sau mỗi lần lặp
        print(f"Lần lặp thứ {i + 1}: {arr}")

# Ví dụ sử dụng
my_list = [4,7,0,9 ,2 ,5 ,3 ,1 ,8, 6]
print("Dãy số trước khi sắp xếp:", my_list)
bubble_sort(my_list)
print("Dãy số sau khi sắp xếp:", my_list)

# in hello wworld
