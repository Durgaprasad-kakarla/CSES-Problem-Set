n=int(input())
nums=[]
for i in range(1,n+1):
    nums.append(i)
while len(nums)>1:
    for i in range(1,len(nums),2):
        print(nums[i],end=" ")
    lst=[]
    for i in range(0,len(nums),2):
        lst.append(nums[i])
    if len(nums)%2!=0:
        lst.insert(0,lst.pop())
    nums=lst.copy()
print(nums[0])