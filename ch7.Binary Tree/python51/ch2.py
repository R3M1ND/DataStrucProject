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
    def height(self,node) :
        if node == None:
            return 0 
        else :
            L = self.height(node.right)
            R = self.height(node.left)
            if L > R :
                return L + 1
            else :
                return R + 1 

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Height of this tree is : {}".format(T.height(root)-1))