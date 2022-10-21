a=['all','apples','ott','mass']
ans=[]
for i in a:
    if len(i)%2!=0 and i[0] in 'aeiou':
        ans+=[i]
print(ans)
