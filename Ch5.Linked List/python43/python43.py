class Node :
    def __init__(self,data = None,Next = None) :
        self.data = data
        self.next = Next

class Linkedlist :
    def __init__(self) :
        self.head = None
        self.tail = None
        self.__size = 0
    def push(self,item) :
        temp = self.head
        self.head = Node(item)
        self.head.next = temp
        self.__size += 1    
    def size(self) :
        return self.__size    
    def len(self) :
        temp = self.head
        count = 0
        while temp : #while current is not null
            count += 1
            temp = temp.next
        return count           
    def iterate_item(self) :
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

def intotheWood(num) :
    l = Linkedlist()
    
    for i in num :
        if i[0] == 'A' :
            l.push(int((i.split())[1]))
        if i[0] == 'B' :           
            node = l.head           
            if node == None :
                count = 0
            else :
                count = 1         
                highest = node.data
                while node.next != None :               
                    if node.next.data > highest :
                        highest = node.next.data
                        count += 1
                    node = node.next
            print(count)

num = [i for i in input("Enter Input : ").split(",")]
intotheWood(num)
