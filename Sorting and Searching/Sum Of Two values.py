def sum_of_two_values(nums,target):
    arr = []
    for i, x in enumerate(nums):
        arr.append([x, i])
    arr.sort()  # Sort arr in increasing order by their values.

    left, right = 0, len(arr) - 1
    while left < right:
        sum2 = arr[left][0] + arr[right][0]
        if sum2 == target:
            return [arr[left][1]+1, arr[right][1]+1]
        elif sum2 > target:
            right -= 1  # Try to decrease sum2
        else:
            left += 1  # Try to increase sum2
    return []
n,x=map(int,input().split())
arr=list(map(int,input().split()))
lst=sum_of_two_values(arr,x)
lst.sort()
if lst==[]:
    print("IMPOSSIBLE")
else:
    print(lst[0],lst[1])