def memoization(n):
    sm=(n*(n+1))//2
    if sm%2!=0:
        return 0
    else:
        target=sm//2
        dp=[[0 for i in range(target+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(1,target+1):
                l=dp[i-1][j]%(10**9+7)
                r=0
                if j>=i:
                    r=dp[i-1][j-i]%(10**9+7)
                dp[i][j]=(l+r)
        return (dp[n][target]//2)%(10**9+7)

n=int(input())
print(memoization(n))
''' Time Complexity--O(n*sum(arr)//2)
    Space Complexity--O(n*sum(arr)//2)'''