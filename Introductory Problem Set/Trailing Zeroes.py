n=int(input())
cnt=0
while n>=5:
    n=(n//5)
    cnt+=n
print(cnt)
'''Time Complexity--O(logn)
    Space Complexity--O(1)'''