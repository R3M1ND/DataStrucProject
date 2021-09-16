def minfunc(inp,n) :
    if n == 1:
        return inp[0]
    return min(inp[n-1],minfunc(inp,n-1))

num = list(map(int,input("Enter Input : ").split()))
n = len(num) 
print("Min :",minfunc(num,n))