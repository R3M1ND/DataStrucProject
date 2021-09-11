class Personalt :
    #Attributes = พวกตัวแปร
    color = "No like color"
    year = 0
    nickname = "No name"

    #constructor = เป็น defalut ใน python เอาไว้เรียกตัวแปรที่เราจะเรียกใช้ในคลาส
    def __init__(self,nickname,year,color) :
        self.__nickname = nickname
        self.__year = year
        self.__color = color

    #Method = function ที่จะให้ตัวแปรดำเนินการ
    def getNickname(self) : #getterfunction
        return self.__nickname

    def getYear(self) : #getterfunction
        return self.__year

    def getColor(self) : #getterfunction
        return self.__color
    
    def setNickname(self,n) : #setterfunction
        self.__nickname = n

    def setYear(self,y) : #setterfunction
        self.__year = y

    def setColor(self,c) : #setterfunction
        self.__color = c
    
    def printData(self) :
        print("Nickname :",self.__nickname)
        print("Old :",self.__year)
        print("Color you like :",self.__color)
    #destructor
    def __del__(self) :
        print("Object was destroyed")
#Inheritance
class College(Personalt) :
    def __init__(self, nickname, year, color): #contribute
        super().__init__(nickname, year, color)   
    def setCollege(self,college) :
        self.__college = college
    def getCollege(self) :
        return self.__college
    #Method Overriding
    def setNickname(self,n,s):
        super().setNickname(n)
        self.__surname = s
    def getSurname(self) :
        return self.__surname

#Creat Object
personal1 = College("khim",20,"black")
personal1.printData()
personal1.setYear(19)
print("Change old :",personal1.getYear())
personal1.setNickname("khim","Aw")
print("Name :",personal1.getNickname() + ' '+ personal1.getSurname())
personal1.setCollege("KMITL")
print("College :",personal1.getCollege())
del personal1
#personal1.setColor("blue")
#print("Change color :",personal1.getColor)


        


