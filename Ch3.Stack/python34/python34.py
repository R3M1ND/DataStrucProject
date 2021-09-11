class Stack :
    def __init__(self) :
        self.data = []
    def size(self) :
        return len(self.data)
    def push(self,i) :
        return self.data.append(i)
    def pop(self) :
        return self.data.pop()

def dec2bin(decnum) :
    s = Stack()
    nbin = ''

    while decnum != 0 :
        newNum = decnum%2
        decnum = decnum // 2
        s.push(newNum)
    while s.size() != 0 :
        nbin = nbin + str(s.pop())
    return nbin

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : {}".format(dec2bin(int(token))))