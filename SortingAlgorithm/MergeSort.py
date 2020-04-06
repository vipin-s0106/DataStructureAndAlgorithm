#O(nLog(n)) complexity

def merge_sort(arr,lb,ub):
    if lb < ub:
        mid = (lb+ub)//2
        merge_sort(arr,lb,mid)
        merge_sort(arr,mid+1,ub)
        merge(arr,lb,mid,ub)


def merge(a,lb,mid,ub):
    pass