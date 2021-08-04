'''
num = int(input())

for i in range(num) :
    if i==0 or i==num-1 :
        for j in range(num) :
            print("#",end="")
    if i >= 1 and i <= num-2 :
        for j in range(num) :
            if j == 0 or j == num-1 :
                print("#",end="")
            elif j >= 1 and j <= num-2 :
                print(" ",end="")
    print()

'''
a = int(input())
b = int(input())
if 0 <= a <= 10**9 and 0 <= b <= 10**9 :
    print(a+b)
