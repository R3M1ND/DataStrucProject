class Stack:
    def __init__(self) :
        self.data = []
    def push(self,i) :
        return self.data.append(i)

def intotheWood(num) :
    s = Stack()    
    for i in num :
        if i[0] == 'A' :
            s.push(int((i.split())[1]))
        if i[0] == 'B' :
            count = 0
            highest = -1
            for i in range(len(s.data)-1,-1,-1) :
                if s.data[i] > highest :
                    highest = s.data[i]
                    count += 1
            print(count)

num = [i for i in input("Enter Input : ").split(",")]
intotheWood(num)
