class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self,data=None) -> None:
        if data == None:
            self.head = None
        else:
            self.head = Node(data)
        self.size = 0
    def append(self,item):
        newNode = Node(item)
        self.size += 1
        if self.head == None:
            self.head = newNode
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = newNode
    def addhead(self,item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
    def remove(self,item):
        i = self.head
        before = self.head
        self.size -= 1
        while i != None:
            if item == i.data :
                if i == self.head:
                    self.head = i.next
                    break
                else:
                    before.next = i.next
            before = i
            i = i.next
    def __str__(self) -> str:
        i,s =self.head,str(self.head.data)
        while i.next != None:
            s += " -> " + str(i.next.data)
            i = i.next      
        return s
    def max_digit(self):
        i = self.head
        _max = -9999999999999
        round = 0
        while i != None:
            if(i.data > _max):
                _max = i.data
            i = i.next
        while _max >0:
            _max //= 10
            round += 1 
        return round+1 
    def get_digit(self,val,digit):
        for i in range(digit-1):
            val = int((val/10))
        if val > 0 :
            return val % 10
        else :
            return (10-val) % 10

    def copy(self):
        i = self.head
        this = LinkedList()
        while i != None:
            this.append(i.data)
            i = i.next
        return this

    def isEmpty(self):
        return self.size == 0

    def dequeue(self):
        temp = self.head
        min = 9999999999  
        while temp != None :
            #print("Arai wa")
            if temp.data < min :
                min = temp.data
            temp = temp.next 
        return min
    def radixSort(self):
        order = self.copy()
        stop = False
        time = 0
        q = [LinkedList() for e in range(10)]
        for i in range(1,self.max_digit()+1):           
            node = order.head
            print("------------------------------------------------------------")
            print("Round :",i)
            while node != None:
                if self.get_digit(node.data,i) == 0:
                    q[0].append(node.data)                  
                elif self.get_digit(node.data,i) == 1:
                    q[1].append(node.data)
                    #print("-",node.data)                  
                elif self.get_digit(node.data,i) == 2:
                    q[2].append(node.data)
                elif self.get_digit(node.data,i) == 3:
                    q[3].append(node.data)
                elif self.get_digit(node.data,i) == 4:
                    q[4].append(node.data)
                elif self.get_digit(node.data,i) == 5:
                    q[5].append(node.data)
                elif self.get_digit(node.data,i) == 6:
                    q[6].append(node.data)
                elif self.get_digit(node.data,i) == 7:
                    q[7].append(node.data)
                elif self.get_digit(node.data,i) == 8:
                    q[8].append(node.data)
                else: q[9].append(node.data)
                node = node.next
            
            order = LinkedList()
            for j in range(len(q)):
                
                print(str(j)+" : ",end="")
                if self.size == q[0].size :
                    stop = True
                while not q[j].isEmpty():                   
                    p = q[j].dequeue()
                    q[j].remove(p)
                    order.append(p)
                    print(p,end=" ")
                print()
            if stop == True :
                break
            time += 1
        print("------------------------------------------------------------")
        print(time,"Time(s)")            
        print("Before Radix Sort :",self)                        
        print("After  Radix Sort :",order)

inp = input("Enter Input : ")
seq = LinkedList()
s = ""
#split
for i in range(len(inp)):
    if inp[i] == ' ':
        seq.append(int(s))
        s = ""
    else:
        s += inp[i]
        if i == len(inp)-1:
            seq.append(int(s))
seq.radixSort()
