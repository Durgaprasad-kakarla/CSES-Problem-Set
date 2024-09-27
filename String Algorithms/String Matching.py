def lps_of_a_string(s):
    n=len(s)
    lps=[0]*n
    i,length=1,0
    while i<n:
        if s[i]==s[length]:
            lps[i]=length+1
            length+=1
            i+=1
        else:
            if length!=0:
                length=lps[length-1]
            else:
                lps[i]=0
                i+=1
    return lps
 
def Knuth_Morris_Pratt_Algorithm(txt,pattern):
    n,m=len(txt),len(pattern)
    lps=lps_of_a_string(pattern)
    i,j,cnt=0,0,0
    while i<n:
        if txt[i]==pattern[j]:
            i+=1
            j+=1
        if j==m:
            cnt+=1
            j=lps[j-1]
        elif i<n and txt[i]!=pattern[j]:
            if j==0:
                i+=1
            else:
                j=lps[j-1]
    return cnt
 
txt=input()
pattern=input()
print(Knuth_Morris_Pratt_Algorithm(txt,pattern))
''' Time Complexity--O(n+m)
    Space Complexity--O(m)'''
