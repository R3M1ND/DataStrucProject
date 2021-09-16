def palindrome(inp) :
    if len(inp) < 1 :
        return True
    else :
        if inp[0] == inp[-1] : 
            return palindrome(inp[1:-1]) #ตัดตัวแรกกับตัวสุดท้าย
        else :
            return False

inp = input("Enter Input : ")
if palindrome(inp) == True :
    print("'{}'".format(inp) + " is palindrome")
else :
    print("'{}'".format(inp) + " is not palindrome")