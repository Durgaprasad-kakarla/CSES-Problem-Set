n=int(input())
nums=list(map(int,input().split()))
res = 0
prefixsum = 0
count = [1] + [0] * n
for a in nums:
    prefixsum = (prefixsum + a) % n
    res += count[prefixsum]
    count[prefixsum] += 1
print(res)