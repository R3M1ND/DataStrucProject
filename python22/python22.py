#from itertools import permutations
import itertools

lst = []
lst2 =[]
print("*** Fun with permute ***")
n = list(map(int, input("Enter List : ").split(",")))
print("Original Cofllection:",n)
n.sort(reverse = True)
print("Collection of distinct numbers:") 
print(list(itertools.permutations(n)))