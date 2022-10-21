a=['try','why','apple','is']
ans=[]
for i in a:
    for j in range(0,len(i)):
        if i[j] in 'aeiou':
            break
    else:
        ans+=[i]
print(ans)
