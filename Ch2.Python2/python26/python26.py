def weirdSubtract(num,sub):			
	for i in range(sub) :
		if num % 10 ==0 :
			num //= 10 # หารเอาเลขลงตัวำม่เอาเศษ
		else :
			num -= 1
	return num
	
num,sub = input("Enter num and sub : ").split()
print(weirdSubtract(int(num),int(sub)))
