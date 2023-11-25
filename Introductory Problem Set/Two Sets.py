n=int(input())
tot=(n*(n+1))//2
lst1=[]
x=n
if tot&1==1:
    print("NO")
else:
    print("YES")
    half=tot//2
    while half!=0:
        lst1.append(n)
        half=half-n
        n-=1
        if half<=n and half!=0:
            lst1.append(half)
            break
    print(len(lst1))
    for i in lst1:
        if i!=0:
            print(i,end=" ")
    print()
    print(x-len(lst1))
    if len(lst1)==1:
        for i in range(1, lst1[-1]):
            print(i, end=" ")
    else:
        for i in range(1,lst1[-2]):
            if i!=lst1[-1]:
                print(i,end=" ")
''' Time Complexity--O(n)
    Space Complexity--O(n//2)'''