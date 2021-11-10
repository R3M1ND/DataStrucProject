
class TreeNode(object): 
    def __init__(self, val,pos,name): 
        self.val = val 
        self.left = None
        self.right = None
        self.pos = pos
        self.name = name

    def __str__(self):
        return str(self.val)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

class AVL_Tree: 
    def __init__(self):
        self.root = None
    
    def insert(self,root,key,pos,name = 0) :
        if not root :
            self.root = TreeNode(key,pos,name)
            return 

        if pos == root.pos*2+1 :
            root.left = TreeNode(key,pos,name)
            return root
        if pos == root.pos*2+2 :
            root.right = TreeNode(key,pos,name)
            return root
        if root.left :
            root.left = self.insert(root.left,key,pos,name)
        if root.right :
            root.right = self.insert(root.right,key,pos,name)
        return root
    
    def booking(self, name):
        q = Queue()
        self.root.name += name
        temp = self.root 
        if self.root.left :
            q.enqueue(self.root.left)
        if self.root.right :
            q.enqueue(self.root.right)


        heap = []

        while not q.is_empty():
            node = q.dequeue()
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

            if temp and temp.name < node.name:
                temp.left = temp.right = None
                heap.append(temp)
                temp = None

            if temp and temp.name == node.name:
                if temp.val < node.val:
                    temp.left = temp.right = None
                    heap.append(temp)
                    temp = None

            node.left = node.right = None
            heap.append(node)

        if temp:
            heap.append(temp)
        self.root = None

        return heap
    
    def printTree90(self,node, level = 0):
        if node != None:
            self.printTree90(node.right, level + 1)
            print('     ' * level, node)
            self.printTree90(node.left, level + 1)

myTree = AVL_Tree() 

inp = [i for i in input('Enter Input : ').split("/")]

for name in range(int(inp[0])):
        myTree.insert(myTree.root, int(name) + 1, int(name))

for cus, data in enumerate(inp[1].split()):
    print(f'Customer {cus + 1} Booking Van {myTree.root} | {data} day(s)')
    new_heap = myTree.booking(int(data))
    for name in new_heap:
        myTree.insert(myTree.root, name.val, new_heap.index(name), name.name)
''''''
