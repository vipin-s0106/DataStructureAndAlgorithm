#O(n) complexity
def bubble_sort(arr,length):
    for i in range(0,length-1):
        change_flag = False
        for j in range(0,length-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                change_flag = True
        if not change_flag:
            break
    return arr

print(bubble_sort([2,1,3,4,5,6,7,8,9],9))