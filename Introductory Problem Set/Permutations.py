n=int(input())
even,odd=[],[]
if n==1:
    print(1)
elif n<4:
    print("NO SOLUTION")
else:
    for i in range(1,n+1):
        if i&1==0:
            even.append(i)
        else:
            odd.append(i)
    final=[]
    for i in range(len(odd)-1,-1,-1):
        final.append(odd[i])
    for i in range(len(even)-1,-1,-1):
        final.append(even[i])
    for i in final:
        print(i,end=" ")
''' Time Complexity--O(n)
    Space Complexity--O(n)'''