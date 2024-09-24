def lower_bound(arr,ele):
    n=len(arr)
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>=ele:
            r=mid-1
        else:
            l=mid+1
    return l
 
def LIS_BinarySearch(arr):
    n=len(arr)
    LIS=[arr[0]]
    for i in range(1,n):
        if LIS[-1]<arr[i]:
            LIS.append(arr[i])
        else:
            ind=lower_bound(LIS,arr[i])
            LIS[ind]=arr[i]
    return len(LIS)
 
n=int(input())
arr=list(map(int,input().split()))
print(LIS_BinarySearch(arr))
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
