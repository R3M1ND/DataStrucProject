'''
num = 5
col = (2*num)-6

for i in range(num) :
    for j in range(col):
        print(end=" ")
    col -=1
    for j in range(i+1) :
        print("$ ",end="")
    print()
'''
num = int(input())
col = num
for i in range(1,num+1) :
    for j in range(col-i):
        print(" ",end="")
    for j in range(2*i-1) :
        print("*",end="")
    print()