'''print("*** Fun with countdown ***")
lst1 = list(map(int, input("Enter List : ").split()))
size = len(lst1)
idxlst = [idx + 1 for idx , val in enumerate(lst1) if val == 1 ]
res = [lst1[i:j] for i,j in zip([0] + idxlst,idxlst + 
        ([size] if idxlst[0] == size else []))]

for i in res :
    count = 0
    for j in range(len(i)-1,0,-1) :
        if(i[j-1] - i[j] != 1) :
            for k in range(len(i)-count-1):
                i.remove(i[0])
        else :
            count += 1

print("[{},".format(len(res)),str(res)+"]")

'''
objTuple = ("Python", "Java", "Kotlin")
objDict = {"name": "Nai", "country": "Bangkok"}

sep = ' '

print(sep.join(objTuple))   # Python+Java+Kotlin
print('-'.join(objDict))