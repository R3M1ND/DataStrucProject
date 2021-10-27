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
        self.dummy = prev
    def indexOf(self,data) :
        q = self.dummy.next
        for i in range(len(self)) :
            if q.data == data :
                return i 
            q = q.next
        return -1
    def isIn(self,data) :
        return self.indexOf(data) >= 0
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
    def delete(self,i) :
        self.removeNode(self.nodeAt(self.indexOf(i)))
def mainfunc(num) :
    l = DoublyLinkedlist()
    k = 0
        
    for i in num :
        if (i.split())[0] == 'A' :
            l.append(int((i.split())[1]))                
            print("linked list :",l)
            l.reverse()
            print("reverse :",l)
            l.reverse()

        if (i.split())[0] == 'Ab' :           
            l.insert(l.nodeAt(0),int((i.split())[1]))           
            print("linked list :",l)
            l.reverse()                       
            print("reverse :",l)
            l.reverse()    

        if (i.split())[0] == 'R' :
            if l.isEmpty() and int((i.split())[1]) == 0 :
                print("Not Found!")
                print("linked list :",l)
                l.reverse()                       
                print("reverse :",l)
                l.reverse()
            elif l.isIn(int((i.split())[1])) == False :
                print("Not Found!")
                print("linked list :",l)
                l.reverse()                       
                print("reverse :",l)
                l.reverse()
            else :
                print("removed : {} from index : {}".format(int((i.split())[1]),l.indexOf(int((i.split())[1]))))
                l.delete(int((i.split())[1]))
                print("linked list :",l)
                l.reverse()                       
                print("reverse :",l)
                l.reverse()
            
        if (i.split())[0] == 'I' :
            if l.isEmpty() and int((((i.split())[1]).split(":"))[0]) != 0 :                
                print("Data cannot be added")
                print("linked list :",l)
                l.reverse()                       
                print("reverse :",l)
                l.reverse()
            elif int((((i.split())[1]).split(":"))[0]) < 0 :
                print("Data cannot be added")
                print("linked list :",l)
                l.reverse()                       
                print("reverse :",l)
                l.reverse()
            elif len(l) < int((((i.split())[1]).split(":"))[0]) :
                print("Data cannot be added")
                print("linked list :",l)
                l.reverse()                       
                print("reverse :",l)
                l.reverse()
            else :
                l.insert(l.nodeAt(int((((i.split())[1]).split(":"))[0])),int((((i.split())[1]).split(":"))[1]))
                print("index = {} and data = {}".format(l.indexOf(int((((i.split())[1]).split(":"))[1])),int((((i.split())[1]).split(":"))[1])))                
                print("linked list :",l)
                l.reverse()                       
                print("reverse :",l)
                l.reverse()
    
num = [i for i in input("Enter Input : ").split(",")]
mainfunc(num)
