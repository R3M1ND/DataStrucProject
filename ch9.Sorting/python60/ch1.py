# bubble sort
def bubblesort(arr) :
    n = len(arr)
    step = 1
    
    for laststep in range(len(arr) -1,-1,-1) :
        swap = False
        temp = None
        for i in range(laststep):
                if arr[i] > arr[i+1] :
                    temp = arr[i]
                    arr[i],arr[i+1] = arr[i+1],arr[i]
                    swap = True
        if swap:
            if step == len(arr) -1:
                print("last step : {} move[{}]".format(arr,temp))
                return
            else :
                print("{} step : {} move[{}]".format(step,arr,temp))
            step += 1
        else :
            print("last step : {} move[{}]".format(arr,temp))
            return
            
inp = list(map(int,input("Enter Input : ").split()))
bubblesort(inp)
