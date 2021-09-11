txt = input()
reverse1 = ''.join(reversed(str(txt)))

if reverse1 == txt:
    print(reverse1,"is a palindrome.")
else:
    print(txt,"is not a palindrome.")