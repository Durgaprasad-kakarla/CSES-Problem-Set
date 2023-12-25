n,k=map(int,input().split())
arr=list(map(int,input().split()))
dic={0:1}
pref=0
cnt=0
for i in range(n):
    pref+=arr[i]
    rem=pref-k
    if rem in dic:
        cnt+=dic[rem]
    if pref in dic:
        dic[pref]+=1
    else:
        dic[pref]=1
print(cnt)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''