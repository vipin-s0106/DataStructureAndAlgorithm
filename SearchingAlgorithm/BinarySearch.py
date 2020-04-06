arr = [1,2,3,4,5,6,7,8,9]

#Binary Search Algorithm using recursion
def binary_search(ele,arr):
    length = len(arr)
    mid = length // 2
    if mid == 0:
        if arr[mid] == ele:
            return True
        return False
    if arr[mid] == ele:
        return True
    if ele < arr[mid]:
        return binary_search(ele,arr[0:mid])
    else:
        return binary_search(ele, arr[mid:length])


print(binary_search(1,arr))

arr = [1,2,3,4,5,6,7,8,9]
#Iterative Mode structure
def iterative_binary_search(ele,arr):
    length = len(arr)
    mid = length // 2
    while arr[mid] != ele and length > 1:
        if ele < arr[mid]:
            arr = arr[0:mid]
            length = length - mid - 1
        else:
            arr = arr[mid:length]
            length = length - mid

        mid = length // 2
    if arr[mid] == ele:
        return True
    return False

print(iterative_binary_search(10,arr))