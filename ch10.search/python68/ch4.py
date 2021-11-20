class Hash:

    def __init__(self,size,threshold,maxColl) -> None:
        self.item = list([None]*size)
        self.size = size
        self.threshold = threshold
        self.maxColl = maxColl
        self.nonspace = 0
        print("Initial Table :\n"+self.__str__())

    def nearDoublePrime(self):
        for i in range(self.size*2,self.size+40):
            for j in range(2,i):
                if i % j == 0:
                    break
                if i-1 == j:
                    return i
    def rehash(self,l:list):
        self.item = [None]*self.nearDoublePrime()
        self.nonspace = 0
        self.size = len(self.item)
        for i in l:
            if i != None:
                self.insert(i)
    def insert(self,value):
        index = int(value) % self.size 
        while True:
            for i in range(1,self.maxColl+1):
                if  int(((self.nonspace+1)/self.size) * 100 )> self.threshold:
                    print("****** Data over threshold - Rehash !!! ******")
                    return True
                if self.item[index] == None:
                    self.item[index] = str(value)
                    self.nonspace += 1
                    return
                else:
                    print(f"collision number {i} at {index}")
                    if i >= self.maxColl :
                        print("****** Max collision - Rehash !!! ******")
                        return True
                    index =value%self.size + i**2
                    index %= self.size

    def __str__(self) -> str:
        s =""
        for i in range(self.size):
            s += f"#{i+1}\t{self.item[i]}\n"
        return s + "----------------------------------------"

print(' ***** Rehashing *****')
inp = input('Enter Input : ').split('/')
size,maxColl,Threshold = [int(e) for e in inp[0].split()]
hash = Hash(size,Threshold,maxColl)
store = []
for i in inp[1].split():
    store.append(int(i))
    print(f"Add : {int(i)}")
    if hash.insert(int(i)):
        hash.rehash(store)
    print(hash)