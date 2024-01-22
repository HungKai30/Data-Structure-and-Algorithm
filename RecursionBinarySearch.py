def binary_search(arr,min,max,target):
    if(max>=min):
        mid = (max+min)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr,min,mid -1 ,target)
        else:
            return binary_search(arr,mid +1,max,target)
    
    return print("Not found")
arr = [1,4,10,20,30,52,60]
x = 20

result = binary_search(arr,0,len(arr)-1, x)
print(result)
#thuật toán này là đệ quy tìm kiếm nhị phân .
# sử dụng các vị trí ở trong hàm
#vị trí bắt đầu sẽ lafd vị trí 0
#min ám chỉ cho vị trí nhỏ nhất và max chỉ vị trí lớn nhất
#mid giúp chia đôi vị trí