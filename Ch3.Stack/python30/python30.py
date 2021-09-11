class stack :
    def __init__(self) :
        self.data = []
        self.__len__ = 0
    def __len__(self) :
        return len(self.data)
    def push(self,e) :
        self.data.append(e)
        self.__len__ += 1 
        return "Add = {} and Size = {}".format(e,self.__len__)
    def pop(self) :
        self.tmpstack = self.data.copy() 
        if(self.__len__ > 0 ) :
            self.temp = self.data.pop()
            self.__len__ -= 1
            return "Pop = {} and Index = {}".format(self.temp,self.tmpstack.index(self.temp))
        else :
            return "-1"
    def getStack(self) :
        if(self.__len__ > 0):
            return "Value in Stack = "+' '.join(map(str,self.data))
        else :
            return "Value in Stack = Empty"

def mainfunc(lst) :
    s = stack()
    for i in lst :
        if i[0] == 'A' :
            print(s.push(int((i.split())[1])))
        if i[0] == 'P' :
            print(s.pop())
    print(s.getStack())

lst1 = [i for i in input("Enter Input : ").split(",")]
mainfunc(lst1)

