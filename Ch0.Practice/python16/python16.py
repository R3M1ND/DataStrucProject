
firstnum = int(input())
plus = input()
secondnum = int(input())
reverse1 = ''.join(reversed(str(firstnum)))
reverse2 = ''.join(reversed(str(secondnum)))
reverse1 = int(reverse1)
reverse2 = int(reverse2)

print(reverse1,"+",reverse2 ,"=",(reverse1+reverse2))
