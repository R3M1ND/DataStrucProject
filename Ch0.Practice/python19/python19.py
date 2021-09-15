'''
class Personalt :
    #Attributes = พวกตัวแปร
    color = "No like color"
    year = 0
    nickname = "No name"

    #constructor = เป็น defalut ใน python เอาไว้เรียกตัวแปรที่เราจะเรียกใช้ในคลาส
    def __init__(self,nickname,year,color) :
        self.__nickname = nickname
        self.__year = year
        self.__color = color

    #Method = function ที่จะให้ตัวแปรดำเนินการ
    def getNickname(self) : #getterfunction
        return self.__nickname

    def getYear(self) : #getterfunction
        return self.__year

    def getColor(self) : #getterfunction
        return self.__color
    
    def setNickname(self,n) : #setterfunction
        self.__nickname = n

    def setYear(self,y) : #setterfunction
        self.__year = y

    def setColor(self,c) : #setterfunction
        self.__color = c
    
    def printData(self) :
        print("Nickname :",self.__nickname)
        print("Old :",self.__year)
        print("Color you like :",self.__color)
    #destructor
    def __del__(self) :
        print("Object was destroyed")
#Inheritance
class College(Personalt) :
    def __init__(self, nickname, year, color): #contribute
        super().__init__(nickname, year, color)   
    def setCollege(self,college) :
        self.__college = college
    def getCollege(self) :
        return self.__college
    #Method Overriding
    def setNickname(self,n,s):
        super().setNickname(n)
        self.__surname = s
    def getSurname(self) :
        return self.__surname

#Creat Object
personal1 = College("khim",20,"black")
personal1.printData()
personal1.setYear(19)
print("Change old :",personal1.getYear())
personal1.setNickname("khim","Aw")
print("Name :",personal1.getNickname() + ' '+ personal1.getSurname())
personal1.setCollege("KMITL")
print("College :",personal1.getCollege())
del personal1
#personal1.setColor("blue")
#print("Change color :",personal1.getColor)
'''
class Node: 
    
    # Class to create nodes of linked list 
    # constructor initializes node automatically 
    def __init__(self,data): 
        self.data = data 
        self.next = None
    
class Stack: 
      
    # head is default NULL 
    def __init__(self): 
        self.head = None
      
    # Checks if stack is empty 
    def isempty(self): 
        if self.head == None: 
            return True
        else: 
            return False
      
    # Method to add data to the stack 
    # adds to the start of the stack 
    def push(self,data): 
          
        if self.head == None: 
            self.head=Node(data) 
              
        else: 
            newnode = Node(data) 
            newnode.next = self.head 
            self.head = newnode 
      
    # Remove element that is the current head (start of the stack) 
    def pop(self): 
          
        if self.isempty(): 
            return None
              
        else: 
            # Removes the head node and makes  
            #the preceeding one the new head 
            poppednode = self.head 
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data 
      
    # Returns the head node data 
    def peek(self): 
          
        if self.isempty(): 
            return None
              
        else: 
            return self.head.data 
      
    # Prints out the stack      
    def display(self): 
          
        iternode = self.head 
        if self.isempty(): 
            print("Stack Underflow") 
          
        else: 
              
            while(iternode != None): 
                  
                print(iternode.data,"->",end = " ") 
                iternode = iternode.next
            return
          
# Driver code 
MyStack = Stack() 
  
MyStack.push(11)  
MyStack.push(22) 
MyStack.push(33) 
MyStack.push(44) 
  
# Display stack elements  
MyStack.display() 
  
# Print top element of stack  
print("\nTop element is ",MyStack.peek()) 
  
# Delete top elements of stack  
MyStack.pop() 
#MyStack.pop() 
  
# Display stack elements 
MyStack.display() 
  
# Print top element of stack  
print("\nTop element is ", MyStack.peek())  
  
# This code is contributed by Mathew George 

        


