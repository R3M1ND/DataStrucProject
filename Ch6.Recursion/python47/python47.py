def power(a,b):
    if b == 0 :
        return 1 
    elif a == 0 :
        return 0 
    elif b == 1 :
        return a
    else :
        return a*power(a,b-1)
num,pow = [int(x) for x in input("Enter Input a b : ").split()]
print(power(num,pow))