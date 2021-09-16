def rod(maxn = 0) :
    if maxn > 0 :
        if maxn == x :
            print("|  |  |")
        if len(A) > maxn: #print first row
            print(str(A[maxn]),end="  ")
        else :
            print("|",end="  ")
        if len(B) > maxn : #change rod
            print(str(B[maxn]),end="  ")
        else :
            print("|",end="  ")
        if len(C) > maxn :
            print(str(C[maxn]),end="  ")
        else :
            print("|",end="  ")
        print("")
        rod(maxn-1)
    
def move(n,a:list,c:list,b:list,maxn) : #(n,from rod -> list,to rod->list,auxrod->list,max = บรรทัด)
    if n == 1 :
        print('move',n, 'from ', a[0],'to', c[0])
        c.append(a.pop())
        rod(maxn)       
    else :       
        move(n-1,a,b,c,maxn) #from , aux , to                  
        print('move',n, 'from ', a[0], 'to', c[0])
        c.append(a.pop())
        rod(maxn)
        move(n-1,b,c,a,maxn)#aux , to , from

global x ;
global A,B,C
n = int(input("Enter Input : "))
x = n
A,B,C = ['A'],['B'],['C']
A.extend(range(n,0,-1))
rod(n)
move(n,A,C,B,n)
