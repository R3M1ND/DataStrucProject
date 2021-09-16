def rod(row) :
    if row == 0:
        return
    i = row + 1
    print("|  ",end="")
    rod(row-1)        
    #rod(i-1)
    #print("|  ",end="")
    #print()
    
def move(n,a,c,b) : #(n,from rod,to rod,auxrod)
    if n == 1 :
        print(n, 'from', a,'to', c)
        

    else :       
        move(n-1,a,b,c) #from , aux , to                  
        print(n, 'from', a, 'to', c)
        move(n-1,b,c,a)#aux , to , from

n = int(input("Enter Input : "))
move(n,'A','C','B')
rod(n)