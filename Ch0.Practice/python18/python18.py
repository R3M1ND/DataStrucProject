txt = input()
countUpper = 0
countLower = 0

for i in txt :
    if i >= 'a' and i <= 'z' :
        countLower = countLower + 1
    if  i >= 'A' and i <= 'Z' :
        countUpper = countUpper + 1

print("UPPER:"+str(countUpper))
print("LOWER:"+str(countLower))