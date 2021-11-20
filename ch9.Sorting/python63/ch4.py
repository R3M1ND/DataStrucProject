def findAlpha(txt:str):
    if txt == "":
        return
    alphabet = findAlpha(txt[1:]) 
    if txt[0].isalpha():
        return txt[0]
    return alphabet

def insert(l:list,l2:list,index=0):
    if index >= len(l):
        l.append(l2)
        return
    if ord(l[index][0]) > ord(l2[0]):
        l.insert(index,l2)
    else:
        insert(l,l2,index+1)
    return

inp = input('Enter Input : ').split()
item = []
for i in inp:
    c = findAlpha(i)
    insert(item,[c,i])
    
for i in item:
    print(i[-1],end=" ")