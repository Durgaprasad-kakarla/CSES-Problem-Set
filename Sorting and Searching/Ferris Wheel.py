n,target=map(int,input().split())
arr=list(map(int,input().split()))
sm=0
cnt=0
arr.sort()
l,r=0,n-1
while l<r:
    if arr[l]+arr[r]<=target:
        cnt+=1
        l+=1
        r-=1
    else:
        cnt+=1
        r-=1
if l==r:
    print(cnt+1)
else:
    print(cnt)
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''