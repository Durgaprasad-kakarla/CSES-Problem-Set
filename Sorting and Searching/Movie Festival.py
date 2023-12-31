n=int(input())
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])
cnt=0
maxi=0
arr=sorted(arr,key=lambda x:x[1])
end=-1
for i in range(n):
    if end<=arr[i][0]:
        end=arr[i][1]
        cnt+=1
print(cnt)
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''