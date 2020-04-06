arr = [4,2,8,7,6,1,3]

def search(ele):
    for num in arr:
        if num == ele:
            return True
    return False

print(search(21))
