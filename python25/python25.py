class translator:

    def deciToRoman(self, num):
        nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ["I","IV","V","IX","X","XL","L","XC","C","CD"
                ,"D","CM","M"]
        i = 12
        while num:
            divide = num // nums[i]
            num %= nums[i]

            while divide:
                print(roman[i],end="")
                divide -=1
            i -= 1

    def romanToDeci(self, s):
        print("\n{}".format(num))

num = int(input("Enter number to translate : "))
translator().deciToRoman(num)
translator().romanToDeci(num)