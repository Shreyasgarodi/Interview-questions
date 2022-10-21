l1 = [1, 2, 5, "HAI", "Hello",4+10j]
l2 = [3, "GOOD", "HAVE",
"A", "NICE", "DAY"]
if type(l1[0])==int and type(l2[0])==int:
    for i in l2:
        l1+=[i]
    print(l1)
else:
    print(id(l1),id(l2))
