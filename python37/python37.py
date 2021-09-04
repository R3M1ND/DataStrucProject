class Queue :
    def __init__(self) :
        self.data = []
    def enqueue(self,item) : #append
        self.data.append(item)
    def dequeue(self) :
        return self.data.pop()
    def size(self) :
        return len(self.data)


def secretCode(c,h) :
    q = Queue()
    valh = ord(h)
    num = valh - ord(c[0])

    for i in range(len(c)) :
        valc = ord(c[i])
        q.enqueue(chr(valc+num)) 
        print(q.data)

code,hint = [i for i in input("Enter code,hint : ").split(",")]
secretCode(code,hint)