def sizeofUpper(inp) :
    lstl = ''
    lsts = ''
    lst1 = []
    lst2 = []
    l = 0  
    s = 0
    for i in inp :
        if i.isupper() :
            l += 1
            if i not in lstl :
                lstl += i + '  ' 
        elif i.islower() :
            s += 1
            if i not in lsts :
                lsts += i + '  ' 

    lst1 = lstl.split()
    lst1.sort()
    lst2 = lsts.split()
    lst2.sort()
    print("No. of Upper case characters :",l)
    print("Unique Upper case characters :",*lst1)
    print("No. of Lower case Characters :",s)
    print("Unique Lower case characters :",*lst2)


print(" *** String count ***")
inp = input("Enter message : ")
sizeofUpper(inp)
