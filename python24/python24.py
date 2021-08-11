def splitlst(lst1,ct):
    return lst1[:ct]

print("*** Fun with countdown ***")
lst1 = list(map(int, input("Enter List : ").split()))
lst2 = []
lst3 = []
count = 0

for i in range(len(lst1)) :
    count = lst1.count(1)
    if count == 1 :
        lst2 = splitlst(lst1,count+1)
        lst2.sort(reverse=True)
        lst3.append(lst2)
        count = 0
print(lst3)
#print(count)


