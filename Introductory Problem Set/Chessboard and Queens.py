board=[input() for i in range(8)]
col=[0]*8
d1=[0]*15
d2=[0]*15
global count
count=0
def solve(y):
    global col,d1,d2,count
    if y==8:
        count+=1
        return
    for x in range(8):
        if col[x] or d1[x+y] or d2[x-y+7] or board[y][x]=='*':
            continue
        col[x]=d1[x+y]=d2[x-y+7]=1
        solve(y+1)
        col[x]=d1[x+y]=d2[x-y+7]=0
solve(0)
print(count)
''' Time Complexity--O(8!)
    Space Complexity--O(1)'''