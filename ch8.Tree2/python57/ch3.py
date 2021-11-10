
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.lst = []

    def __str__(self):
        s = ''
        for i in self.lst:
            s += str(i.data)
        return '[ ' + str(s) +' ]'

    def size(self):
        return len(self.lst)

    def isEmpty(self):
        return self.size() == 0

    def enQ(self, data):
        self.lst.append(data)

    def deQ(self):
        return self.lst.pop(0)

class AVL_Tree:
    def __init__(self):
        self.root = Node(0)

    def insert(self, inputList, nodeAmount):    
        queue = Queue()
        queue.enQ(self.root)
        index = 0
        count = 1   #
        for i in range(nodeAmount):
            currentNode = queue.deQ()

            if currentNode.left is None:

                if count >= len(inputList) - 1:
                    currentNode.left = Node(inputList[index])   
                    index += 1  
                else :
                    currentNode.left = Node(0)                  
                count += 1  
                queue.enQ(currentNode.left)

            if currentNode.right is None:
                if count >= len(inputList) - 1:
                    currentNode.right = Node(inputList[index])  
                    index += 1  
                else:
                    currentNode.right = Node(0)                
                count += 1  
                queue.enQ(currentNode.right)
            if count == nodeAmount:     
                break
        return self.root

    def recurNode(self, node):     
        if node.left is None and node.right is None:    
            return node.data                        

        left = self.recurNode(node.left)
        right = self.recurNode(node.right)

        if left > right:        
            lessValue = right
        else:
            lessValue = left
        node.data = lessValue   
        node.right.data = node.right.data - lessValue   
        node.left.data = node.left.data - lessValue   
        return lessValue

    def calcurateNumber(self):       
        queue = Queue()
        queue.enQ(self.root)
        count = 0
        while not queue.isEmpty():
            currentNode = queue.deQ()
            count += currentNode.data   
            if currentNode.left is not None:
                queue.enQ(currentNode.left)
            if currentNode.right is not None:
                queue.enQ(currentNode.right)
        print(count)
    
    def printTree90(self,node, level = 0):
        if node != None:
            self.printTree90(node.right, level + 1)
            print('     ' * level, node)
            self.printTree90(node.left, level + 1)

myTree = AVL_Tree() 
root = None

inp,inp2 = input('Enter Input : ').split("/")
inp = int(inp)
inp2 = [int(i) for i in inp2.split()]

if len(inp2) != (inp//2) + 1 :
    print("Incorrect Input")
else :    
    root = myTree.insert(inp2, inp)   
    myTree.recurNode(root)
    myTree.calcurateNumber()
''''''
