n,m,k=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr1.sort()
arr2.sort()
i,j=0,0
cnt=0
while i<n and j<m:
    if arr1[i]>arr2[j]:
        if arr2[j]+k>=arr1[i] and arr2[j]-k<=arr1[i]:
            cnt+=1
            i+=1
            j+=1
        else:
            j+=1
    else:
        if arr1[i]+k>=arr2[j] and arr1[i]-k<=arr2[j]:
            cnt+=1
            i+=1
            j+=1
        else:
            i+=1
print(cnt)

''' Time Complexity--O(nlogn+mlogm)
    Space Complexity--O(1)'''