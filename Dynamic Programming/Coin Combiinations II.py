n, target = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

dp = [0] * (target + 1)

dp[0] = 1

for coin in arr:
    if coin > target:
        break
    for j in range(coin, target + 1):
        dp[j] = (dp[j] + dp[j - coin]) % (10 ** 9 + 7)
print(dp[target])

''' Time Complexity--O(n*target)
    Space complexity--O(n)'''