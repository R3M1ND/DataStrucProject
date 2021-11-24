def bubble_sort(arr) :
    n = len(arr)
    step = 1
    lst = []
    for laststep in range(len(arr) -1,-1,-1) :
        swap = False
        temp = None
        for i in range(laststep):
                if arr[i] > arr[i+1] :
                    temp = arr[i]
                    arr[i],arr[i+1] = arr[i+1],arr[i]
                    swap = True
        if swap:
            step += 1
    for i in range(1,step+1) :      
        compare = n - i    
        # print(compare,"com")
        lst.append(compare)
    print()
    print(arr)
    print("Data comparison =",sum(lst))

print(" *** Bubble sort ***")    
input_string = input("Enter some numbers : ")

A=[]

for n in input_string.split():
	A.append(int(n))
        
bubble_sort(A)
# print()
# print(A)
# print("Data comparison =", count)

