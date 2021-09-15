class Node :
    def __init__(self,data = None,Next = None) :
        self.data = data
        self.next = Next
    def __str__(self):
	    return str(self.data)
class Linkedlist :
    def __init__(self):
        self.head = None
    def push(self,item) :
        temp = self.head
        self.head = Node(item)
        self.head.next = temp
    def isEmpty(self) :
        if self.head == None:
            return True
        else :
            return False
    def peek(self) :
        if self.isEmpty() :
            return None
        else :
            return self.head.data
    def pop(self) :      
        if self.isEmpty() :
            return None
        else :
            popnode = self.head
            self.head = self.head.next
            popnode.next = None
            return popnode.data
    def __str__(self) :
        current = self.head
        result = ""
        while current != None :          
            result += str(current)
            current = current.next
        return result
    def reverse(self) :
        prev = None
        current = self.head
        while current != None :
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev