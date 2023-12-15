lst=[]
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    lst.append([from_rod,to_rod])
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
n=int(input())
TowerOfHanoi(n,1,3,2)
print(len(lst))
for i in lst:
    print(i[0],i[1])