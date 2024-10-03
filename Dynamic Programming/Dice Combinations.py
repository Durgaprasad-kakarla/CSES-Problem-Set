import sys
sys.setrecursionlimit(100000)
def dice_combinations(n,dp):
    if n==0:
        return 1
    if dp[n]!=-1:
        return dp[n]
    l=0
    for i in range(1,7):
        if n>=i:
            l+=dice_combinations(n-i,dp)%(10**9+7)
    dp[n]=l%(10**9+7)
    return dp[n]%(10**9+7)

def top_down(n):
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(1,n+1):
        for j in range(1,7):
            if i>=j:
                dp[i]=(dp[i]+dp[i-j])%(10**9+7)
    return dp[n]%(10**9+7)
    ''' Time Complexity--O(n)
        Space Complexity--O(n)'''

n=int(input())
print(top_down(n))