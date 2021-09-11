class funString():
    def __init__(self,string = ""):
        self.string = string

    def size(self) :
        print(len(str1))

    def changeSize(self):
        case =''
        for i in range(len(str1)) :
            if str1[i].isupper():
                case += chr(ord(str1[i])+32) # ord() method returns the Unicode code of a specific character
            else:
                case += chr(ord(str1[i])-32)
        print(case)

    def reverse(self):
        rstr = str1[::-1]
        print(rstr)

    def deleteSame(self):
        case = ''
        for i in range(len(str1)) :
            if str1[i] not in case:
                case += str1[i]
        print(case)

str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :   res.size()

elif str2 == "2":  res.changeSize()

elif str2 == "3" : res.reverse()

elif str2 == "4" : res.deleteSame()