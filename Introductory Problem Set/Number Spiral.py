t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>y:
        if x%2!=0:
            print((x-1)*(x-1)+y)
        else:
            print(x*x-y+1)
    else:
        if y%2==0:
            print((y-1)*(y-1)+x)
        else:
            print(y*y-x+1)

