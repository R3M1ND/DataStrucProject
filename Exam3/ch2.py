def maxfunc(num,n) :
    if n == 1:
        return num[0]
    return max(num[n-1],maxfunc(num,n-1))

inp = list(map(int,input("Enter Input : ").split()))
n = len(inp)
print("Max : {}".format(maxfunc(inp,n)))