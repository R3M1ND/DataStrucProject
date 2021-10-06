print("*** Fun with Drawing ***")
num = int(input("Enter input : "))
x = 3*(num-1)+num
a = x
b = 0
c = int((x/2))

for i in range(x) :
    if i % 2 == 0 :
        print("#." * b + "#" * a + ".#" * b) # * b means print b round  
        if i < c :
            a -= 4 
            b += 1
    else :
        print("#." * b + "." * a + ".#" * b)
        if i > c :   
            a += 4 
            b -= 1 