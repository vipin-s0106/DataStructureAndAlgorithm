#O(n^2) complexity
def insertion_sort(arr):
    length = len(arr)
    for i in range(1,length):
        temp = arr[i]
        j = i -1
        while (j >= 0 and arr[j] > temp):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        print(arr)
    return arr

print(insertion_sort([2,1,3,4,5,6,7,8,9]))
