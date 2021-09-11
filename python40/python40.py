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

def find(opn,cls) :
    __open__ ="</"
    __close__ = ">"
    return __open__.index(opn) == __close__.index(cls)

def isMatchedHtml(raw):
    s = Stack()
    i = 0
    while i <len(raw) :
        temp = raw[i]
        if temp in '</' :
            s.push(temp)
        else:
            if temp in '>' :
                if s.size() > 0 :
                    if(not(find(s.pop(),temp))) :
                        return "This is match tag HTML"
                else:
                    return "This is not match tag HTML" 
        i += 1
    if s.size() < 0 :
        return "This is match tag HTML"
    else :
        return "This is not match tag HTML"
'''
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag) 
        else:
            if S.isEmpty(): 
                return False
            if tag[1:] != S.pop(): 
                return False
        j = raw.find('<' , k+1) 
    return S.isEmpty()
'''
raw = input("Enter HTML content : ")
print(isMatchedHtml(raw))
'''
if isMatchedHtml(raw):
    print("This is match tag HTML")
else:
    print("This is not match tag HTML")
'''