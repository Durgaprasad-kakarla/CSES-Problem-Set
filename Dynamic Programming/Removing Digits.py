def top_down(n):
    dp=[float('inf')]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        mini=float('inf')
        for j in str(i):
            mini=min(mini,1+dp[i-int(j)])
        dp[i]=mini
    return dp[n]

print(top_down(int(input())))
''' Time Complexity--O(n)
    Space Complexity--O(n)'''