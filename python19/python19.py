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

#Creat Object
personal1 = Personalt("khim",20,"black")
personal1.printData()
personal1.setYear(19)
print("Change old :",personal1.getYear())
#personal1.setColor("blue")
#print("Change color :",personal1.getColor)


        


