def harmonic_sum(n) :
    if n == 1 :
        print(n,end=" ")
        return 1 
    else :
        sum = harmonic_sum(n - 1) + 1/n
        print('+ 1/{}'.format(n),end =" ")
        return sum        
        
print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : "))
print("= %.8f" %(harmonic_sum(num)))
