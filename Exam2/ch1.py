class Stack() :
    def __init__(self) :
        self.data = []
    def __str__(self) :
        s = 'Data in Stack is : '
        for i in self.data :
            s += str(i) + ' '
        return s
    def push(self,i) :
        self.data.append(i)
    def pop(self) :
        return self.data.pop()
    def size(self) :
        return len(self.data)
    def isEmpty(self) :
        if self.size() == 0 :
            return "True"
        else :
            return "False"
    def peek(self) :
        return self.data[-1]
    def bottom(self) :
        return self.data[0]

inp = int(input("Enter choice : "))
s1 = Stack()
if inp == 1 :
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())
if inp == 2 :
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())
if inp == 3 :
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())
