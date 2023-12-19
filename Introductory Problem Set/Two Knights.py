n=int(input())
print('0')
for i in range(2,n+1):
    print(((i*i)*(i*i-1))//2-4*(i-1)*(i-2))
# def func(row,col,n,vis,h):
#     cnt=0
#     tot=n*n
#     vis[row][col]=1
#     if row-1>=0 and col-2>=0 and not vis[row-1][col-2]:
#         cnt+=1
#     if row+1<n and col-2>=0 and not vis[row+1][col-2]:
#         cnt+=1
#     if row-1>=0 and col+2<n and not vis[row-1][col+2]:
#         cnt+=1
#     if row+1<n and col+2<n and not vis[row+1][col+2]:
#         cnt+=1
#     if row-2>=0 and col-1>=0 and not vis[row-2][col-1]:
#         cnt+=1
#     if row+2<n and col-1>=0 and not vis[row+2][col-1]:
#         cnt+=1
#     if row-2>=0 and col+1<n and not vis[row-2][col+1]:
#         cnt+=1
#     if row+2<n and col+1<n and not vis[row+2][col+1]:
#         cnt+=1
#     return tot-cnt-h
# for k in range(1,x+1):
#     tot = 0
#     h=0
#     n=k
#     vis=[[0 for i in range(n)] for j in range(n)]
#     for i in range(n):
#         for j in range(n):
#             y=func(i,j,n,vis,h+1)
#             h=h+1
#             tot+=y
#     print(tot)