myinput = int(input())
for i in range(myinput) :   
    for j in range(i+1) :
        print("*",end="")
        j+=1
    print()
    i+=1 