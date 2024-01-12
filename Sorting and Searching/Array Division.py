n,k=map(int,input().split())
nums=list(map(int,input().split()))
l,r = max(nums), sum(nums)
while l < r:
    mid = (l+r)//2
    tot, cnt = 0, 1
    for num in nums:
        if tot+num<=mid:
            tot += num
        else:
            tot = num
            cnt += 1
    if cnt>k:
         l= mid+1
    else:
        r= mid
print(r)
'''Time Complexity--o(nlogn)
   Space Complexity--O(1)'''
'''Time Limit Exceeded in CSES but worked in Codeforces'''
