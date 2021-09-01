class Stack :
    def __init__(self) :
        self.data = []
    def push(self,e) :
        return self.data.append(e)
    def pop(self) :
        return self.data.pop()
    def size(self) :
        return len(self.data)
    def getstack(self) :
        return self.data

def match(opn,cls) :
    __open__ = "([{"
    __close__ = ")]}"
    return __open__.index(opn) == __close__.index(cls)

def expr(num):
    s = Stack()
    i = 0
    while i < len(num) :
        temp = num[i]
        if temp in '([{' :
            s.push(temp)
        else :
            if temp in ')]}' :
                if(s.size() > 0):
                    if(not(match(s.pop(),temp))) :
                        return num + " Unmatch open-close"
                else :
                    return num + " close paren excess"
        i += 1
    if s.size()>0 :
        return num + " open paren excess   " + str(s.size())+" : "+''.join(map(str,s.getstack()))
    else :
        return num + " MATCH"

inp = input("Enter expresion : ")
print(expr(inp))
