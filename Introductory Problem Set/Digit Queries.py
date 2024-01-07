powers=[1]*19
for i in range(1,19):
    powers[i]=powers[i-1]*10
t=int(input())
for i in range(t):
    n=int(input())
    numDig=0
    digits=0
    prevDig=0
    for i in range(1,19):
        digits+=(powers[i]-powers[i-1])*i
        if digits>=n:
            numDig=i
            break
        prevDig=digits
    low=powers[numDig-1]
    high=powers[numDig]-1
    ans=0
    startPosAns=0
    while low<=high:
        mid=(low+high)//2
        startPos=(mid-powers[numDig-1])*numDig+prevDig+1
        if startPos<=n:
            if mid>ans:
                ans=mid
                startPosAns=startPos
            low=mid+1
        else:
            high=mid-1
    number=str(ans)
    print(number[n-startPosAns])
'''Time Complexity--O(logn)
   Space Complexity--O(1)'''