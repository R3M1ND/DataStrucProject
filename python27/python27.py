def mod_position(arr,num):
    lst = []
    for i in range(num-1,len(arr),num): #เริ่มนับที่ 1 เพิ่มขึ้นทีละ num
        lst.append(arr[i])
    return lst

print("*** Mod Position ***")
str1,num = input("Enter Input : ").split(",")
num = int(num)
print(mod_position(str1,num))
