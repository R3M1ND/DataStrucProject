class Queue() :
    def __init__(self) :
        self.data = []
    def __str__(self) :
        s = ''
        for i in self.data :
            s += str(i) + ' '
        return s        
    def enQueue(self,i) :
        self.data.append(i)
    def deQueue(self) :
        return self.data.pop()

def dup(inp) :
    q = Queue()
    if inp == 'E' :
        

inp = [str(i) for i in input("Enter numbers : ").split("/")]
dup(inp)
