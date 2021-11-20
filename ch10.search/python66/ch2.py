def bi_search(l, r, arr, x):
    if l>r:
        return "No First Greater Value"

    mid = (l+r)//2
    leastmax = arr[mid]

    if x < arr[mid]:
        temp = bi_search(l,mid-1,arr,x)
        if type(temp) == str:
            return leastmax
        if leastmax > temp:
            leastmax = temp
    else:
        leastmax = bi_search(mid+1,r,arr,x)
    return leastmax

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(map(int,inp[1].split()))
for i in k:
    print(bi_search(0, len(arr) - 1, sorted(arr), i))