st=input()
cnt=1
maxi=0
n=len(st)
if n==1:
    print(1)
else:
    for i in range(1,n):
        if st[i]==st[i-1]:
            cnt+=1
        else:
            maxi=max(maxi,cnt)
            cnt=1
    print(max(maxi,cnt))
''' Time Complexity--O(n)
    Space Complexity--O(1)'''