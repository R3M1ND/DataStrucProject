row = int(input())
col = row

for i in range(1,row+1):
    for j in range(col-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print("")
for i in range(row-1,-1,-1):
    for j in range(col-i+1,1,-1):
        print("",end=" ")
    for j in range(2*i-1):
        print("*",end="")
    print("")