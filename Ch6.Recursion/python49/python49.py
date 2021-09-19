def underfunc(under) :
    if under == 0  :
        return                      
    if under < 0 : 
        print("_",end="")
        underfunc(under+1)
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
    elif inp > 0 :   
        underfunc(inp - 1)
        tagfunc(num - inp + 1)
        print()
        patternPositive(inp - 1,num)
    else :
        i = inp*-1
        underfunc(num-inp)       
        tagfunc(i)
        print("\n",end="")
        patternPositive(inp+1,num)

inp = int(input("Enter Input : "))
if inp == 0 :
    print("Not Draw!")
else :
    patternPositive(inp,inp)