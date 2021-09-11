lst = []
count = 5
for i in range(count):
    num = int(input())
    lst.append(num)
    lst.sort(reverse=True)
for j in range(5):
    print(lst[j])