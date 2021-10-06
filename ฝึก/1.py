'''
n = list(map(int,input("List : ").split(",")))
print("First :",n)
print("Second :"," ".join(map(str,n)))

dic = {}
text = "AAABBBCCCDDDE"

for i in text :
    if i in dic.keys() :
        dic[i] += 1
    else :
        dic[i] = 1 #start at 1

print(dic.items())

n = int(input())
for i in range(n+1) :
    for j in range(i) :
        print("*",end="")
    print(" ")
  
n = int(input())
x = (n*2)+2
a = (x//2)-n
b = 1

for i in range(x) :
    if i == 0 :
        print("*" * a + " " * n*2 + "*" * a)
        b+=1
    elif i % 2 == 0 :
        print("*" * x)
        b+=1
    else : 
        print("*" * b + " " * n + "*" * b)

n = 2
for i in range(-n, n+1):
    for j in range(1,(n+1)-abs(i)+1):
        print("*",end="")
    for j in range(1,(2)*abs(i)+1):
        print(" ",end="")
    for j in range(1,(n+1)-abs(i)+1):
        print("*",end="")
    print("\r")

def factor_list(num):
    out = list()
    for i in range(1, num+1):
        if num % i == 0:
            out.append(i)
    return out

print(' *** Perfect Number Verification ***')
number = int(input('Enter number : '))
lst = factor_list(number)
print('Factors :', lst)

def palindome(s) :
    if s == s[::-1] : #reverse
        return True
    else :
        return False

inp = input("Input : ")
if palindome(inp) == True :
    print("Palindome")
else :
    print("Not palindome")

n = 2
for i in range(2,0,-1):
    for j in range(0,i) :
        print("*",end="")
    print(" ")

n = 2
for i in range(1,n+1):
    for j in range(i) :
        print("*",end="")
    print(" ")
'''