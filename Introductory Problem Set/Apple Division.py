import sys

n=int(input())
arr=list(map(int,input().split()))

def func(ind,sm,arr,target):
    if ind==0:
        return abs((target-sm)-sm)
    return min(func(ind-1,sm+arr[ind],arr,target),func(ind-1,sm,arr,target))

print(func(n-1,0,arr,sum(arr)))
