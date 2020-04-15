#Complexity O(n^2s)

def selection_sort(arr):
    length = len(arr)
    for i in range(0,length-1):
        min_elem = arr[i]
        k = i
        for j in range(i+1,length):
            if min_elem >= arr[j]:
                min_elem = arr[j]
                k = j
        temp = arr[i]
        arr[i] = min_elem
        arr[k] = temp
        print(arr)

    return arr

print(selection_sort([7,4,10,8,3,1]))