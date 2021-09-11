class Stack:
    def __init__(self):
        self.data = []
    def push(self, value):
        return self.data.append(value)
    def pop(self):
        return self.data.pop
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return len(self.data) == 0
    def getStack(self) :
        return self.data
    def reverse(self) :
        return self.data.reverse

def colorCrush(inp) :
    s = Stack()
    l = inp.split()
    combo = 0
    ncombo = 0
    state = True
    while(state) :
        for i in l:
            if inp.count(i) != 3 and (i not in s.data) :
                combo += 1
                s.push(i)
                state = False
            if inp.count(i) >= 3  :     
                ncombo += 1 
                for _ in range(3) :        
                    l.pop(l.index(i))
                    state = True
            if len(l) == 0 :
                state = False                  
    l.reverse()
    if s.isEmpty() :
        print(s.size())
        print("Empty")
        if ncombo >= 2 :
            print("Combo : {} ! ! !".format(ncombo))
    elif ncombo >= 2 :
        print(ncombo)
        print(''.join(l))
        print("Combo : {} ! ! !".format(ncombo))
    else :
        print(len(l))    
        print(''.join(l))                  

lst1 = input('Enter Input : ')
colorCrush(lst1)


