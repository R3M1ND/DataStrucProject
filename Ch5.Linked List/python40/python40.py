class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None
class Stack :
    def __init__(self) :
        self.item = None
    def isEmpty(self) :
        if self.item == None:
            return True
        else :
            return False
    def push(self,data) :
        if self.item is None :
            self.item = Node(data)
        else :
            newNode = Node(data)
            newNode.next = self.item
            self.item = newNode
    def pop(self) :      
        if self.isEmpty() :
            return None
        else :
            popnode = self.item
            self.item = self.item.next
            popnode.next = None
            return popnode

def isMatchedHtml(raw):
    s = Stack()
    balance = True
    index = 0

    while index < len(raw) and balance :
        symbol = raw[index]
        if symbol in "</"  :
            s.push(symbol)    
        else :
            if s.isEmpty() :
                balance = False
            else :
                s.pop()
        index = index + 1
    if balance and s.isEmpty() :
        return "This is match tag HTML"
    else :
        return "This is not match tag HTML"

raw = input("Enter HTML content : ")
print(isMatchedHtml(raw))
'''
if isMatchedHtml(raw):
    print("This is match tag HTML")
else:
    print("This is not match tag HTML")
'''