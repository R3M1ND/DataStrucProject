class Node():
    def __init__(self,data=None) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
class Stack():
    def __init__(self) -> None:
        self.stack = []
        self.size = 0
    def push(self,data):
        self.size += 1
        self.stack.append(data)
    def pop(self):
        self.size -= 1
        return self.stack.pop()
    def isEmpty(self):
        return self.size == 0
class BST():
    def __init__(self) -> None:
        self.root = None
        self.s = Stack()

    def insert(self,data):
        newNode = Node(data)
        if data in '+-*/':
            newNode.right = self.s.pop()
            newNode.left = self.s.pop()
        self.s.push(newNode)

    def printTree(self,node:Node,level=0):
        if node!= None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def printPre(self,node:Node):
        if node!= None:
            print(node,end="")
            self.printPre(node.left)
            self.printPre(node.right)
    def printIn(self,node:Node):
        if node!= None:
            if node.right != None:
                print('(',end="")
            self.printIn(node.left)
            print(node,end="")
            self.printIn(node.right)
            if node.left != None:
                print(')',end="")
T = BST()
inp = input("Enter Postfix : ")
for i in inp:
    T.insert(i)
T.root = T.s.pop()
print("Tree : ")
T.printTree(T.root)
print("--------------------------------------------------")
print("Infix : ",end="")
T.printIn(T.root)
print("\nPrefix : ",end="")
T.printPre(T.root)