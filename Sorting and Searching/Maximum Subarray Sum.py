n=int(input())
arr=list(map(int,input().split()))
maxi,sm=0,0
cnt=0
for i in range(n):
    sm+=arr[i]
    if maxi<sm:
        maxi=sm
    if arr[i]>0:
        cnt+=1
    if sm<0:
        sm=0
if cnt==0:
    print(max(arr))
else:
    print(maxi)
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
