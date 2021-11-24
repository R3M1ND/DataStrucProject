def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)
		i = j = k = 0
        
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
        
def printList(arr):
    print()
    print("Sorted -> ",end="")
    for i in range(len(arr)):		
        print(arr[i], end=" ")

print(" *** Merge sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
    A.append(int(n))
            
mergeSort(A)
printList(A)
