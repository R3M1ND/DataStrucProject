class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self,size,maxColl) -> None:
        self.item = [None]*size
        self.size = size
        self.maxColl = maxColl
        
    def isFull(self):
        if None in self.item:
            return False
        return True

    def insert(self,data:Data):
        sum = 0
        for i in data.key:
            sum += ord(i)
        
        if self.isFull():
            print("This table is full !!!!!!")
            return True
        index = sum % self.size 
        for i in range(1,self.maxColl+1):
            
            if self.item[index] == None:
                self.item[index] = str(data)
                return
            else:
                print(f"collision number {i} at {index}")
                index = sum%self.size + i**2
                index %= self.size
        print("Max of collisionChain")

    def __str__(self) -> str:
        s =""
        for i in range(self.size):
            s += f"#{i+1}	{self.item[i]}\n"
        return s + "---------------------------"
print(" ***** Fun with hashing *****")
inp = input('Enter Input : ').split('/')
size,maxcoll = [int(i) for i in inp[0].split()]
Hash = hash(size=size,maxColl=maxcoll)
for i in inp[1].split(','):
    key,value = [str(e) for e in i.split()]
    if Hash.insert(Data(key,value)):
        break
    print(Hash)