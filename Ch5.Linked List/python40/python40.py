class Stack :
    def __init__(self,list = None) :
        if list == None :
            self.item = []
        else :
            self.item = list()
    def isEmpty(self) :
        return len(self.item) == 0
    def push(self,i) :
        return self.item.append(i)
    def pop(self) :
        return self.item.pop()
    def size(self) :
        return len(self.item)

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