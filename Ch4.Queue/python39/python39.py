class Queue :
    def __init__(self):
        self.data = []   
    def enqueue(self,item) :
        self.data.append(item)
    def isEmpty(self) :
        return len(self.data) <= 0
    def dequeue(self) :
        return self.data.pop(0)

class Stack:
    def __init__(self,ID):
        self.data = []
        self.item = []
        self.combo = 0
        self.count = 0
        self.fail = 0
        self.id = ID
    def push(self, value):
        self.data.append(value)
    def pop(self,i):
        return self.data.pop(i)
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return self.size() <= 0
    def getStack(self) :
        return self.data
    def reverse(self) :
        return self.data.reverse
    def count(self,i) :
        return self.data.count(i)
    
    def bombLeft(self):
        if self.isEmpty():
            if "RORRIM" in self.id:
                return "ytpmE"
            return "Empty"
        self.data.reverse()
        return ""+''.join(self.data)
    
    def colorCrush(self,q : Queue = None) :
        i = 0
        item = ""
        newlst = []

        if q == None :
            while i in range(len(self.data)-2) :
                if same(self.data[i],self.data[i+1],self.data[i+2]) :
                    self.count += 1
                    self.item.append(self.data[i])
                    self.data.pop(i)
                    self.data.pop(i)
                    self.data.pop(i)
                    i = -1
                i += 1
            
        if q != None :
                while i in range(len(self.data)-2) :
                    if not q.isEmpty() :
                        if same(self.data[i],self.data[i+1],self.data[i+2]) :                            
                            self.data.insert(i+2,q.dequeue())
                            item += self.data[i+2]          
                        if same(self.data[i],self.data[i+1],self.data[i+2]) :
                            self.fail += 1
                            self.data.pop(i)
                            self.data.pop(i)
                            self.data.pop(i)
                            i = -1
                        i += 1
                    else :          
                        if same(self.data[i],self.data[i+1],self.data[i+2]) :
                            self.count += 1
                            self.data.pop(i)
                            self.data.pop(i)
                            self.data.pop(i)
                            i = -1
                        i += 1
        if q == None:
            return self.item
    def result(self):
        if "NORMAL" in self.id:
            print("NORMAL :")
        else:
            print(": RORRIM")
        print(self.size())
        print(self.bombLeft())
        if "NORMAL" in self.id:
            print("{} Explosive(s) ! ! ! (NORMAL)".format(self.count))
        else:
            print("(RORRIM) ! ! ! (s)evisolpxE {}".format(self.count))
        if self.fail > 0:
            print("Failed Interrupted {} Bomb(s)".format(self.fail))

def same(x,y,z) :
    return x == y == z
    
''''''
def colorCrush2(normal,mirror) :
    mirrors = Stack(": RORRIM")
    mirrorq = Queue()
    for i in range(len(mirror)-1,-1,-1) :
        mirrors.push(mirror[i])
    for i in mirrors.colorCrush() :
        mirrorq.enqueue(i)
    normals = Stack(": NORMAL")    
    for j in range(len(normal)):
        normals.push(normal[j])
    normals.colorCrush(mirrorq)
    normals.result()
    print("------------MIRROR------------")
    mirrors.result()

lst1,lst2 = input('Enter Input (Normal, Mirror) : ').split()
colorCrush2(lst1,lst2)

