def divide(num) :
    j = 0
    if num == 0 :
        print("{} is OUT of range !!!".format(num))
    else :
        print("Output ==> ",end="")
        for i in range(1,num+1) :
            if num % i == 0 :
                j +=1
                print(i,end=" ")
        print()
        print("Total ==>",j)
        
print(" *** Divisible number ***")
inp = int(input("Enter a positive number : "))
divide(inp)