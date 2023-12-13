t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if (a==0 and b!=0) or (b==0 and a!=0):
        print("NO")
    else:
        if (a+b)%3!=0  or (2*a)<b or (2*b)<a:
            print("NO")
        else:
            print("YES")