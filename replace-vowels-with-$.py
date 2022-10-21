a=[['a','hello'],['aeiou','this is python class']]
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        st=''
        for k in range(0,len(a[i][j])):
            if a[i][j][k] not in 'aeiou':
                st+=a[i][j][k]
            else:
                st+='$'
        a[i][j]=st
print(a)
