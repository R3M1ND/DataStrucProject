class Queue :
    def __init__(self) :
        self.data = []
    def len(self) :
        return len(self.data)
    def enqueue(self,item) : 
        self.data.append(item)
    def isEmpty(self) :
        return len(self.data) == 0
    def dequeue(self) :
        return self.data.pop(0)
    def getQueue(self) :
        if(self.len() > 0) :
            return ', '.join(map(str,self.data))
        else :
            return "Empty"

def func(lst) :
    q = Queue()
    space = []
    j = 0
    for i in lst :
        if i[0] == 'E' :
            q.enqueue(int((i.split())[1]))
            print(', '.join(map(str,q.data)))
        if i[0] == 'D' :
            if q.isEmpty() :
                print("Empty")
            else :
                space.append(q.dequeue())
                print(space[j],"<- ",end="")
                j += 1
                if q.isEmpty() :
                    print("Empty")
                else :
                    print(q.getQueue(),sep=', ') #sep = เชื่อมกับอะไร
    if len(space) == 0 :
        print("Empty",end="")
    print(*space,sep=', ',end="")
    print(" : ",end="")
    print(q.getQueue(),end="")    
lst1 = [i for i in input("Enter Input : ").split(",")]
func(lst1)