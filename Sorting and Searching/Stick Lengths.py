n=int(input())
nums=list(map(int,input().split()))
nums.sort()
if n&1==1:
    ele=nums[n//2]
else:
    ele=(nums[n//2]+nums[n//2-1])//2
cost=0
for i in range(n):
    cost+=abs(ele-nums[i])
print(cost)
'''Time Complexity--O(nlogn)
   Space Complexity--O(1)'''