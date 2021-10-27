'''
class Stack() :
    def __init__(self) :
        self.data = []
    def __str__(self) :
        s = ''
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
        if len(self.data) == 0 :
            return "True"
    def peek(self) :
        return self.data[-1] #ข้อมูลบนสุด ตัวหลัง
    def bottom(self) :
        return self.data[0] #ข้อมูลล่างสุด ตัวแรก

inp = input('Enter choice : ')
s = Stack()
if inp == '2':
    s.push(100)
    s.push(200)
    s.push(300)
    s.pop()
    print(s)
    print("Stack is Empty :", s.isEmpty())
elif inp == '1':
    s.push(10)
    s.push(20)
    print(s)
    s.pop()
    s.push(30)
    print("Peek of stack :", s.peek())
    print('Bottom of stack :', s.bottom())
else:
    s.push(11)
    s.push(22)
    s.push(33)
    s.pop()
    print(s)
    print('Stack size :', s.size())
 
class Queue :
    def __init__(self) :
        self.data = []
    def len(self) :
        return len(self.data)
    def enqueue(self,item) : 
        self.data.append(item)
    def isEmpty(self) :
        return len(self.data) == 0
    def dequeue(self) :
        return self.data.pop(0)
    def getQueue(self) :
        if(self.len() > 0) :
            return ', '.join(map(str,self.data))
        else :
            return "Empty"
s = Queue()
s.enqueue(4)
s.enqueue(5)
s.enqueue(6)
s.dequeue()
print(s.data)
'''
