# monstand
class TreeNode(object): 
    def __init__(self, val,pos = 0): 
        self.val = val 
        self.left = None
        self.right = None
        self.pos = pos

    def __str__(self):
        return str(self.val)

class AVL_Tree: 
    def __init__(self):
        self.root = None
    
    def insert(self,root,key,pos) :
        if not root :
            self.root = TreeNode(key,pos)
            return 

        if pos == root.pos*2+1 :
            root.left = TreeNode(key,pos)
            return root
        if pos == root.pos*2+2 :
            root.right = TreeNode(key,pos)
            return root
        if root.left :
            root.left = self.insert(root.left,key,pos)
        if root.right :
            root.right = self.insert(root.right,key,pos)
        return root
    
    def sumR(self,root) :
        if not root :
            return 0
        sum = self.sumR(root.left)
        sum += self.sumR(root.right) + int(root.val)
        return sum

    def findSum(self,root) :
        if not root :
            return 0 
        sum = 0
        if root.left :
            sum += self.findSum(root.left)
        if root.right :
            sum += self.findSum(root.right)
        return sum + root.val
    
    def pow_at(self, root, pos):
        if not root:
            return 0
        if pos == root.pos:
            return self.findSum(root)

        data = self.pow_at(root.left, pos)
        if data :
            return data
        data = self.pow_at(root.right, pos)   
        return data

    def printTree90(self,node, level = 0):
        if node != None:
            self.printTree90(node.right, level + 1)
            print('     ' * level, node)
            self.printTree90(node.left, level + 1)
    


inp = input('Enter Input : ').split('/')

mon = AVL_Tree()
data = list(map(int, inp[0].split()))

for pos, name in enumerate(data):
    mon.insert(mon.root, name, pos)

print(mon.sumR(mon.root))
for data in inp[1].split(','):
    data = data.split()
    a, b = mon.pow_at(mon.root, int(data[0])), mon.pow_at(mon.root, int(data[1]))     
    oper = '='
    if a > b:
        oper = '>'
    if a < b:
        oper = '<'
    print(f'{str(data[0])}{oper}{str(data[1])}')
    
