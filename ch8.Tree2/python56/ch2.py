
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)

class AVL_Tree(object): 
    def insert(self,root,key) :
        if not root :
            return TreeNode(key)
        elif key < root.val :
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key)
        root.height = 1+ max(self.getheight(root.left),self.getheight(root.right))
        
        balance  = self.getBalance(root)
        #left left
        if balance > 1 and key < root.left.val :
            print("Not Balance, Rebalance!")
            return self.rRotate(root)
        #right right
        if balance < -1 and key >= root.right.val :
            print("Not Balance, Rebalance!")
            return self.lRotate(root)
        #left right
        if balance > 1 and key >= root.left.val :
            root.left = self.lRotate(root.left)
            print("Not Balance, Rebalance!")
            return self.rRotate(root)
        #right left
        if balance < -1 and key < root.right.val :
            root.right = self.rRotate(root.right)
            print("Not Balance, Rebalance!")
            return self.lRotate(root)
        return root
    
    def lRotate(self,z) :
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))
        return y
    
    def rRotate(self,z) :
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1+max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1+max(self.getheight(y.left),self.getheight(y.right))
        return y

    def getheight(self,root) :
        if not root :
            return 0 
        return root.height
    
    def getBalance(self,root) :
        if not root:
            return 0 
        return self.getheight(root.left) - self.getheight(root.right)
    
    def printTree90(self,node, level = 0):
        if node != None:
            self.printTree90(node.right, level + 1)
            print('     ' * level, node)
            self.printTree90(node.left, level + 1)

myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, int(e))
    myTree.printTree90(root)
    print("===============")