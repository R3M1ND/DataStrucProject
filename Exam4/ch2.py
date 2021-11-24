# AVl บ่าย kuy rai mai ru yak ship hai ai sus
class Node(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)

class AVLTree(object):
    def __init__(self) :
        self.root = None

    def insert(self,key) :
        if not self.root :
            return Node(key)
        elif key < self.root.val :
            self.root.left = self.insert(self.root.left,key)
        else: 
            self.root.right = self.insert(self.root.right,key)
        self.root.height = 1+ max(self.getheight(self.root.left),self.getheight(self.root.right))
        
        balance  = self.getBalance(self.root)
        #left left
        if balance > 1 and key < self.root.left.val :
            print("Not Balance, Rebalance!")
            return self.rRotate(self.root)
        #right right
        if balance < -1 and key >= self.root.right.val :
            print("Not Balance, Rebalance!")
            return self.lRotate(self.root)
        #left right
        if balance > 1 and key >= self.root.left.val :
            self.root.left = self.lRotate(self.root.left)
            print("Not Balance, Rebalance!")
            return self.rRotate(self.root)
        #right left
        if balance < -1 and key < self.root.right.val :
            self.root.right = self.rRotate(self.root.right)
            print("Not Balance, Rebalance!")
            return self.lRotate(self.root)
        return self.root
    
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

    def getheight(self) :
        if not self.root :
            return 0 
        return self.root.height
    
    def getBalance(self) :
        if not self.root:
            return 0 
        return self.getheight(self.root.left) - self.getheight(self.root.right)
    
    def printTree90(self,node, level = 0):
        if node != None:
            self.printTree90(node.right, level + 1)
            print('     ' * level, node)
            self.printTree90(node.left, level + 1)
    def print_inorder(self,node) :
        if not node:
            return      
        print(node.val)
        self.print_inorder(node.left) 
        self.print_inorder(node.right)
    def print_preorder(self,node) :
        if not node:
            return         
        self.print_preorder(node.left)
        print(node.val)
        self.print_preorder(node.right)    
    def print_postorder(self,node) :
        if not node:
            return      
        self.print_postorder(node.right)
        print(node.val)
        self.print_postorder(node.left) 
        


print(" *** AVL Tree ***")    

input_string = input("Enter some numbers : ")

bst = AVLTree()

for n in input_string.split():

	bst.insert(int(n))

bst.print_inorder()

bst.print_preorder()

bst.print_postorder()