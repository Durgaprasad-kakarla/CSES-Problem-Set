def money_sums(arr):
    n=len(arr)
    target=sum(arr)
    dp=[[False for i in range(target+1)] for j in range(n)]
    dp[0][arr[0]]=True
    for i in range(n):
        dp[i][0]=True
    for i in range(1,n):
        for j in range(1,target+1):
            l=dp[i-1][j]
            r=False
            if j>=arr[i]:
                r=dp[i-1][j-arr[i]]
            dp[i][j]=l or r
    return dp[-1]

n=int(input())
arr=list(map(int,input().split()))
dp=(money_sums(arr))
distinct_sums=[]
for i in range(len(dp)):
    if i!=0 and dp[i]==True:
        distinct_sums.append(i)
print(len(distinct_sums))
for i in distinct_sums:
    print(i,end=" ")

'''Time Complexity--O(n*target)
    Space Complexity---O(n*target)'''