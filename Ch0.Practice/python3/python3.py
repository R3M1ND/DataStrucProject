n = int(input())
sum = 1
if 0<n<100 :
    for i in range(1,n+1) :
        sum = sum * i      
    print(sum)
else :
    print("1")
