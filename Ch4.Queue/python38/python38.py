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
        if self.isEmpty() or not self.find(item[0]) :
            self.enqueue(item)
        else:
            for i in range(self.len()-1,-1,-1) :
                if self.data[i][0] == item[0] :
                    self.data.insert(i+1,item)
                    return
            self.enqueue(item)
    def isEmpty(self) :
        return self.len() <= 0
    def dequeue(self) :
        if self.isEmpty() :
            return -1
        else :
            return self.data.pop(0)
    def find(self,dep) :
        for i in self.data :
            if dep == i[0]:
                return True 
        return False     
def func(lst) :
    q = Queue() 
    splst  = lst[0].split(",") #ก่อน /
    splat2 = lst[1].split(",") #หลัง /
    canteen = dict()

    for i in splst :
        dp,id1 = i.split()
        canteen[id1] = dp
    
    #print(canteen)
    #print(splst)
    #print(splat2)
    
    for j in splat2 :
        if len(j) == 1:
            if q.isEmpty() :
                print("Empty")
            else :
                print(q.dequeue()[1])       
        else :
            lst2 = j.split()
            val = lst2[1]
            q.eq2((canteen[val],val))

lst1 = [i for i in input("Enter Input : ").split("/")]
#print(lst1)
func(lst1)