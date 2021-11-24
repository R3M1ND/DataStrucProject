# select sort
def selectSort(inp,n) :
    if n == 0 :
        return inp
    else :
        temp = max(inp[:n+1])
        inp[inp.index(temp)] = inp[n]
        a = inp[n]
        if temp != inp[n] :
            print('swap {} <-> {} : '.format(inp[n],temp),end='')
        inp[n] = temp
        if temp != a :
            print(inp)
    selectSort(inp,n-1)

inp = list(map(int,input("Enter Input : ").split()))
selectSort(inp,len(inp)-1)
print(inp)
