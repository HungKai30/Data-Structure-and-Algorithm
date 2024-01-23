

def bubbleSort(array):
    
#sử dụng vòng lặp để duyệt qua toàn bộ phần tử của array
  for i in range(len(array)):
#sử dụng loop lồng vào trong để so sánh phần tử

    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
#so sánh hai vị trí cạnh nhau
#gán 1 bộ nhớ đệm cho j
#hiểu đơn giản nó là swap vị trí cho nhau nếu xảy ra trường hợp lớn hơn
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)