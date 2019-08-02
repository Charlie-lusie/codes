def Partition(input, low, high):
    temp = input[low] #选取第一个为枢纽元素，存到temp里面
    while (low < high):
        while (low<high and input[high] >= temp): high -= 1
        input[low] = input[high] # 这时候high、low位置的元素值是重复的，等待下次覆盖
        while (low < high and input[low] <= temp): low += 1
        input[high] = input[low]
    input[low] = temp #覆盖low位置为枢纽元素
    return input, low

def QSort(input, low, high):
    if (low < high):
        input, privot = Partition(input, low, high)
        input = QSort(input, low, privot - 1)
        input = QSort(input, privot + 1, high)
    return input

def QuickSort(input):
    return QSort(input, 0, len(input) - 1)

print(QuickSort([3,2,6,1,8,2,9,4]))


