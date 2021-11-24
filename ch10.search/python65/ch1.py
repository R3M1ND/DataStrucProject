# BinarySearch
def bi_search(l, r, arr, x):
    found = False
    if l>r:
        return found
    mid = (l+r)//2
    if x == arr[mid]:
        l = r
        found = True
        return found
    elif x < arr[mid]:
        found = bi_search(l,mid-1,arr,x)
    else:
        found = bi_search(mid+1,r,arr,x)
    return found

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))