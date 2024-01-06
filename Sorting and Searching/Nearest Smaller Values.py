n=int(input())
arr=list(map(int,input().split()))
stack=[]
new=[]
for i in range(n):
    while stack and arr[stack[-1]]>=arr[i]:
        stack.pop()
    if stack:
        new.append(stack[-1]+1)
    else:
        new.append(0)
    stack.append(i)
for i in new:
    print(i,end=" ")
''' Time Complexity--O(n)
    Space Complexity--O(n)'''