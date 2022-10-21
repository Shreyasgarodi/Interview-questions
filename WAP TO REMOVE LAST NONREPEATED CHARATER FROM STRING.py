a='hello how is the class'
di={}
r,ans='',''
for i in a:
    if i in di and i!=' ':
        l=di[i]
        di[i]=l+1
    elif i!=' ':
        di[i]=1
small=999
for i in di:
    if di[i]<=small:
        small=di[i]
        ans=i
print(ans)
