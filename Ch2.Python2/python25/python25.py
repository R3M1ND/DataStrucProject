class translator:

    def deciToRoman(self, num):
        nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ["I","IV","V","IX","X","XL","L","XC","C","CD"
                ,"D","CM","M"]
        romandeci =''
        i = 12
        while num:
            divide = num // nums[i]
            num %= nums[i]

            while divide: 
                romandeci += roman[i]
                divide -= 1
            i -= 1
        return romandeci

    def romanToDeci(self,s):
        romans = {
            'M' : 1000,
            'CM': 900,
            'D' : 500,
            'CD': 400,
            'C' : 100,
            'L' : 50,
            'XL': 40,
            'X' : 10,
            'V' : 5,
            'IV': 4,
            'I' : 1
        }
        sum = 0       
        for i in range(len(s) - 1):
            left = s[i]
            right = s[i + 1]
            if romans[left] < romans[right]:
                sum -= romans[left]
            else:
                sum += romans[left]
        sum += romans[s[-1]] #last char
        #print(' '.join(map(str,romans.keys())))
        return sum
            
num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))