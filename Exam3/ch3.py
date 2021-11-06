def gcdfunc(num1,num2) :
    if num1  == 0 :
        return num2
    elif num2 == 0 :
        return num1
    else :       
        if num1 > num2 :
                return gcdfunc(num1%num1,1)
        return gcdfunc(num2%num1,1)
        

inp1,inp2 = map(int,input("Enter Input : ").split())
if inp2 < 0 :
    inp2 *= -1 
    print(gcdfunc(inp2,inp1))
elif inp1 < 0 :
    inp1 *= -1
    print(gcdfunc(inp1,inp2))
else :
    print(gcdfunc(inp1,inp2))

