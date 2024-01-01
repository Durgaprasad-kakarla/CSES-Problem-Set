n=int(input())
nums=list(map(int,input().split()))
nums.sort()
pref=0
flag=0
if nums[0]>1:
    print(1)
else:
    for i in range(n-1):
        pref+=nums[i]
        if pref+1<nums[i+1]:
            print(pref+1)
            flag=1
            break
    if flag==0:
        print(pref+nums[n-1]+1)
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''