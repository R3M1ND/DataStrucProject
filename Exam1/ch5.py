class MyInt() :
    def __init__(self,inp):
        self.inp = inp
    def toRoman(self) :
        deci = [1,4,5,9,10,40,50,90,100,500,900,1000]
        romans = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        i = 12
        roman = ''
        for j in range(self) :
            num = self//deci[i]
            num
        


print(" *** class MyInt ***")
a,b = map(int,input("Enter 2 number : ").split(" "))
print(a,b)