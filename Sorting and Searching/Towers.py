def upper_bound(arr,ele):
    n=len(arr)
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]<=ele:
            l=mid+1
        else:
            r=mid-1
    return l


n=int(input())
arr=list(map(int,input().split()))
lst=[]
for i in range(n):
    x=arr[i]
    y=upper_bound(lst,x)
    if y==len(lst):
        lst.append(x)
    else:
        lst[y]=x
print(len(lst))
'''Time Complexity--O(nlogn)
   Space complexity--O(n)'''
