n=int(input())
nums=list(map(int,input().split()))
lst=[]
for i in range(n):
    lst.append([nums[i],i])
lst.sort()
ans=1
for i in range(1,n):
    if lst[i][1]<lst[i-1][1]:
        ans+=1
print(ans)
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''