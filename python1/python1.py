'''myinput = int(input())
for i in range(myinput) :   
    for j in range(i+1) :
        print("*",end="")
        j+=1
    print()
    i+=1 
'''
list1 = ["c", "b", "d", "a"]
list2 = [2, 3, 1, 4]

zipped_lists = zip(list1, list2)
sorted_pairs = sorted(zipped_lists)

tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]
print(list1)
print(list2)