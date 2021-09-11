class Queue :
    def __init__(self) :
        self.data = []
    def __str__(self) :
        empty = ""
        if not self.isEmpty():
            for data in self.data:
                empty += str(data) + ' '
        else:
            empty = 'Empty'
        return empty
    def len(self) :
        return len(self.data)    
    def enqueue(self,item) :
        self.data.append(item)
    def eq2(self,item) :
        if self.isEmpty() :
            self.enqueue(item)
        elif self.peek()[0] == 'EN' :
            self.data.insert(0,item)
        else:
            for i in range(self.len()) :
                if self.data[i][0] == 'EN' :
                    self.data.insert(i,item)
                    return
            self.enqueue(item)
    def isEmpty(self) :
        return self.len() <= 0
    def dequeue(self) :
        if self.isEmpty() :
            return -1
        else :
            return self.data.pop(0)
    def peek(self) :
        if self.isEmpty() :
            return -1
        else :
            return self.data[0]    
def func(lst) :
    q = Queue() 
    
    for i in lst :
        j = i.split()
        
        if len(j) == 1:
            if q.isEmpty() :
                print("Empty")
            else :
                print(q.dequeue()[1])       
        else :
            if j[0] == 'ES' :
                q.eq2((j[0],j[1]))            
            if j[0] == 'EN' :
                q.enqueue((j[0],j[1]))      

lst1 = [i for i in input("Enter Input : ").split(",")]
func(lst1)