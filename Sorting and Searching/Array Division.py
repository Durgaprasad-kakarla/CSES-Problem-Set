n, k = map(int, input().split())
nums = list(map(int, input().split()))
 
def func(nums,ele):
    sm,n,cnt=0,len(nums),0
    for i in range(n):
        if sm+nums[i]<=ele:
            sm+=nums[i]
        else:
            cnt+=1
            sm=nums[i]
    if sm>0:
        cnt+=1
    return cnt
 
def array_division(nums,k):
    n=len(nums)
    l,r=max(nums),sum(nums)
    while l<=r:
        mid=(l+r)//2
        if func(nums,mid)<=k:
            r=mid-1
        else:
            l=mid+1
    return l
 
print(array_division(nums,k))
