# insertSort
def insertSort(arr , n) :
    if n <= 1 :
        return
    insertSort(arr,n-1)
    last = arr[n-1]   
    j = n - 2  
    j = loopRecur(arr, j, last)     
    arr[j+1] = last   
    if len(arr) != n:
        print("insert {} at index {} :".format(last,j+1), arr[:n], arr[n:])
    else:
        print("insert {} at index {} :".format(last,j+1), arr)

def loopRecur (arr,j,last) :
    if j < 0 or arr[j] < last :
        return j 
    arr[j+1] = arr[j]
    return loopRecur(arr,j-1,last)

inp = list(map(int,input("Enter Input : ").split()))
insertSort(inp,len(inp))
print("sorted")
print(inp)