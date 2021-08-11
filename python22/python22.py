def permute(num) :
    resultp = [[]]
    for i in num :
        nper = []
        for permu in resultp :
            for j in range(len(permu) + 1) :
                nper.append(permu[:j] + [i] + permu[j:])
                resultp = nper
    return resultp

print("*** Fun with permute ***")
n = list(map(int, input("input : ").split(",")))
print("Original Cofllection: ",n)
print("Collection of distinct numbers:\n",permute(n)) 
