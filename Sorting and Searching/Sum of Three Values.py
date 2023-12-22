n,k=map(int,input().split())
arr=list(map(int,input().split()))
dic={}
for i in range(n):
    if arr[i] in dic:
        dic[arr[i]].append(i)
    else:
        dic[arr[i]]=[i]
arr.sort()
if n<3 or arr[-1]+arr[-2]+arr[-3]<k:
    print("IMPOSSIBLE")
else:
    lst=[]
    flag=0
    for i in range(n):
        if i>0 and arr[i]==arr[i-1]:
            continue
        l,r=i+1,n-1
        while l<r:
            threesum=arr[i]+arr[l]+arr[r]
            if threesum>k:
                r-=1
            elif threesum<k:
                l+=1
            else:
                print((dic[arr[i]].pop())+1,(dic[arr[l]].pop())+1,(dic[arr[r]].pop())+1)
                flag=1
                break
        if flag==1:
            break
    if flag==0:
        print("IMPOSSIBLE")

''' Time Complexity--O(n*n)
    Space Complexity--O(n)'''