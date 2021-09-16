def underfunc(under) :
    if under == 0  :
        return                   
    print("_",end="")
    underfunc(under-1)

def tagfunc(tag):
    if tag == 0:
        return
    print("#",end="")
    tagfunc(tag-1)

def patternPositive(inp,num) :
    if inp == 0 :
        return   
    underfunc(inp - 1)
    tagfunc(num - inp + 1)
    print()
    patternPositive(inp - 1,num)

def patternNegative(inp,num) :
    if inp == 0 :
        return
    i = inp*-1+1   
    underfunc(num-1)
    tagfunc(i-1)
    print("\n",end="")
    patternNegative(inp + 1,num+1)

inp = int(input("Enter Input : "))
if inp > 0 :
    patternPositive(inp,inp)
elif inp < 0:
    patternNegative(inp,1)
else :
    print("Not Draw!")