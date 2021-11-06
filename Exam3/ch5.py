class TreeNode(object) :
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)
class BST() :
    def __init__(self):
        self.root = None
        self.s = []
    def insert(self,data) :
        nNode = TreeNode(data)
        if self.root == None :
            self.root = nNode
        else :
            r = self.root
            while True :
                if data < r.val :
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
    def preOrder(self,node) :
        if not node :
            return
        print(node.val,end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)
    def inOrder(self,node) :
        if not node :
            return        
        self.inOrder(node.left)        
        print(node.val,end=" ")
        self.inOrder(node.right)
    def postOrder(self,node) :
        if not node :
            return
        self.postOrder(node.left) 
        self.postOrder(node.right)
        print(node.val,end=" ")
    def levelOrder(self,node) :
        if node != None :
            if node.left != None :
                self.s.append(node.left)
            if node.right != None :
                self.s.append(node.right)
            print(node.val,end=" ")
            if len(self.s) > 0 :
                self.levelOrder(self.s.pop(0))
            else :
                return

print(" *** Binary Search Tree ***")
inp = [int(item) for item in input("Enter Input : ").split()]
T = BST()
for i in inp :
    sum = T.insert(i)
print()
print(" --- Tree traversal ---")
print("Level order : ",end="")
T.levelOrder(sum)
print()
print("Preorder : ",end="")
T.preOrder(sum)
print()
print("Inorder : ",end="")
T.inOrder(sum)
print()
print("Postorder : ",end="")
T.postOrder(sum)
