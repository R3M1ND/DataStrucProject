lst = []
num = -1
while num !=0 :
    num = int(input())
    lst.append(num)
    if num == 0 :
        lst.remove(num)
sot = input()
if sot.upper() == "MIN":
    lst.sort()
else :
    lst.sort(reverse = True)
print(' '.join(map(str,lst)))
