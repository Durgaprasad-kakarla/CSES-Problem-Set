import itertools
s=input()
s=list(s)
lst=list(set((itertools.permutations(s))))
print(len(lst))
lst.sort()
for i in lst:
    print("".join(i))


''' Time Complexity--O(n!)
    Space Complexity--O(n!)'''