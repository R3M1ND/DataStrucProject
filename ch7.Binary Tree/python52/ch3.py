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
            
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def inorder(self,node) :
        s = []
        if not node :
            return s
        s = self.inorder(node.left)
        s.append(node.data)
        s = s +  self.inorder(node.right)
        return s

T = BST()
inp,inp2 = [ str(i) for i in input('Enter Input : ').split("/")]
inp = map(int,inp.split())
for i in inp:
    root = T.insert(i)

T.printTree(root)
print("--------------------------------------------------")
count = 0 
findMin = T.inorder(root)
for i in range(len(findMin)) :
    if findMin[i] <= int(inp2) :
        count += 1
print(count)