class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root = None
        self.s = []
    def insert(self, data):
        nNode = Node(data)
        if self.root == None :
            self.root = nNode
        else :
            r = self.root
            while True :
                if data < r.data :
                    '''data less the root pai left'''
                    if r.left == None:
                        r.left = nNode
                        break
                    r = r.left
                else :
                    if r.right == None :
                        r.right = nNode
                        break
                    r = r.right
        return self.root
    def preoder(self,node) :
        if node == None :
            return         
        print(node.data,end=" ")       
        self.preoder(node.left)
        self.preoder(node.right)
    def inorder(self,node) :
        if node == None :
            return
        self.inorder(node.left)
        print(node.data,end=" ")
        self.inorder(node.right)
    def postorder(self,node) :
        if node == None :
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data,end=" ")
    def breadth(self,node) :
        if node != None :
            if node.left != None :
                self.s.append(node.left)
            if node.right != None :
                self.s.append(node.right)
            print(node.data,end=" ")
            if len(self.s) > 0 :
                self.breadth(self.s.pop(0))
            else :
                return

        
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Preorder : ",end="")
T.preoder(root)
print()
print("Inorder : ",end="")
T.inorder(root)
print()
print("Postorder : ",end="")
T.postorder(root)
print()
print("Breadth : ",end="")
T.breadth(root)