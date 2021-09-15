
class DoublyLinkedlist :
    class Node:
        def __init__(self, data,prev = None,next = None):
            self.data = data
            self.next = next
            self.prev = prev
    def __init__(self) :
        self.dummy = self.Node(None,None,None)
        self.dummy.next = self.dummy.prev = self.dummy
        self.size = 0
    def __str__(self) :
        s = ''
        p = self.dummy.next
        for i in range(len(self)) :
            s += str(p.data)
            if i < len(self)-1 :
                s += '->'
            p = p.next
        return s
    def __len__(self) :
        return self.size
    def isEmpty(self) :
        return self.size == 0
    def reverse(self) :
        prev = None
        current = self.dummy
        while current != None :
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def index(self,data) :
        q = self.dummy.next
        for i in range(len(self)) :
            if q.data == data :
                return i 
            q = q.next
        return -1
    def nodeAt(self,i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p 
    def insert(self,q,data):
        p = q.prev
        x = self.Node(data,p,q)
        p.next = q.prev = x 
        self.size += 1
    def append(self,data) :
        self.insert(self.nodeAt(len(self)),data)
    def removeNode(self,q) :
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1 
    def delate(self,i) :
        if self.isEmpty():
            print("Not Found!",end="")
        else :
            self.removeNode(self.nodeAt(i))

def mainfunc(num) :
    l = DoublyLinkedlist()
    
    
    for i in num :
        if (i.split())[0] == 'A' :
            l.append(int((i.split())[1]))                
            print("linked list :",l)
            l.reverse()
            print("reverse :",l)

        if (i.split())[0] == 'R' :
            l.delate(int((i.split())[1]))
            print(l)

        if (i.split())[0] == 'Ab' :           
            l.insert(l.nodeAt(0),int((i.split())[1]))
            print("linked list :",l)
            #l.reverse()
            #print("reverse :",l)    
    

num = [i for i in input("Enter Input : ").split(",")]
mainfunc(num)
