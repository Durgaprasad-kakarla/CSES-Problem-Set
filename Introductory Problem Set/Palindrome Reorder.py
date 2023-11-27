from collections import Counter
st=input()
dic=Counter(st)
s=""
cnt=0
x=""
for i in dic.keys():
    if dic[i]%2==0:
        s+=(i*(dic[i]//2))
    else:
        x=dic[i]*i
        cnt+=1
    if cnt==2:
        print("NO SOLUTION")
        break
if cnt<2:
    s+=x
    for i in list(dic.keys())[::-1]:
        if dic[i]%2==0:
            s+=(i*(dic[i]//2))
print(s)
'''Time Complexity--O(n)
   Space Complexity--O(n)'''
